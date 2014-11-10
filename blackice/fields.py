from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from rest_framework import fields

from blackice.devicetype_constants import DEVICE_LOOKUP


class DeviceTypeField(fields.WritableField):
    def to_native(self, value):
        return [n.api_name for n in value]

    def from_native(self, value):
        return [DEVICE_LOOKUP[v] for v in value]


class ReverseChoiceField(fields.ChoiceField):
    """
    A ChoiceField that serializes and de-serializes using the human-readable
    version of the `choices_dict` that is passed.

    The values in the choices_dict passed must be unique.
    """
    def __init__(self, *args, **kwargs):
        self.choices_dict = kwargs.pop('choices_dict')
        kwargs['choices'] = self.choices_dict.items()
        self.reversed_choices_dict = dict((v, k) for k, v
                                          in self.choices_dict.items())
        return super(ReverseChoiceField, self).__init__(*args, **kwargs)

    def to_native(self, value):
        """
        Convert "actual" value to "human-readable" when serializing.
        """
        value = self.choices_dict.get(value, None)
        return super(ReverseChoiceField, self).to_native(value)

    def from_native(self, value):
        """
        Convert "human-readable" value to "actual" when de-serializing.
        """
        value = self.reversed_choices_dict.get(value, None)
        return super(ReverseChoiceField, self).from_native(value)


class TranslationSerializerField(fields.WritableField):
    """
    Django-rest-framework custom serializer field for translatable strings.

    * When deserializing, in `from_native`, it accepts both a string or a
    dictionary.  If a string is given, it'll be considered to be in the default
    language.

    * When serializing, its behavior depends on the parent's serializer
    context.  If 'lang' is None, a dict with all translations for the field is
    returned, with language code as the keys.
    """
    default_error_messages = {
        'min_length': _('The field must have a length of at least {num} '
                        'characters.'),
    }

    def __init__(self, *args, **kwargs):
        self.min_length = kwargs.pop('min_length', None)

        super(TranslationSerializerField, self).__init__(*args, **kwargs)
        # Default to return all translations for each field.
        self.requested_language = None

    def initialize(self, parent, field_name):
        super(TranslationSerializerField, self).initialize(parent, field_name)
        self.requested_language = self.context['lang']

    def to_native(self, value):
        if self.requested_language:
            return value.get(self.requested_language, u'\uFFFD')
        else:
            return value

    def from_native(self, data):
        if isinstance(data, basestring):
            return {self.requested_language: data.strip()}
        elif isinstance(data, dict):
            for key, value in data.items():
                data[key] = value.strip()
            return data
        raise "%s is unrepresentable type %r" % (data, type(data))

    def validate(self, value):
        super(TranslationSerializerField, self).validate(value)

        if self.min_length is None:
            return

        raise_error = True
        if isinstance(value, basestring):
            if len(value.strip()) >= self.min_length:
                raise_error = False
        else:
            for k, v in value.items():
                if len(v.strip()) >= self.min_length:
                    raise_error = False
                    break

        if raise_error:
            raise ValidationError(
                self.error_messages['min_length'].format(num=self.min_length))
