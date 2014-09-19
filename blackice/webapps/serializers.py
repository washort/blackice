from drf_compound_fields.fields import ListField
from rest_framework import serializers

from blackice.constants import (ADDON_WEBAPP_TYPES_LOOKUP, ADDON_PREMIUM_API,
                                CATEGORY_CHOICES)
from blackice.fields import (DeviceTypeField, ReverseChoiceField,
                             TranslationSerializerField)


class AppSerializer(serializers.Serializer):

    # Required fields.

    categories = ListField(serializers.ChoiceField(choices=CATEGORY_CHOICES),
                           required=True)

    # Writable, not required.

    #banner_regions = serializers.Field()  # XXX What goes here?
    device_types = DeviceTypeField()
    description = TranslationSerializerField(required=False)
    id = serializers.IntegerField(required=False)
    homepage = TranslationSerializerField(required=False)
    name = TranslationSerializerField(required=False)
    premium_type = ReverseChoiceField(
        choices_dict=ADDON_PREMIUM_API, required=False)
    #previews = PreviewSerializer(many=True, required=False)
    price = serializers.CharField(required=False)
    #privacy_policy = LargeTextField(view_name='app-privacy-policy-detail',
    #                                required=False)
    slug = serializers.CharField(required=False)
    support_email = TranslationSerializerField(required=False)

    support_url = TranslationSerializerField(required=False)

    # Read-only fields.

    # upsold = serializers.HyperlinkedRelatedField(
    #     view_name='app-detail', source='upsold.free',
    #     required=False, queryset=Webapp.objects.all())
    app_type = serializers.ChoiceField(
        choices=ADDON_WEBAPP_TYPES_LOOKUP.items(), read_only=True)
    author = serializers.CharField(read_only=True)
    banner_message = TranslationSerializerField(read_only=True)
    # content_ratings = serializers.SerializerMethodField('get_content_ratings')
    created = serializers.DateField(read_only=True)
    current_version = serializers.CharField(read_only=True)
    default_locale = serializers.CharField(read_only=True)
    is_offline = serializers.BooleanField(read_only=True)
    is_packaged = serializers.BooleanField(read_only=True)
    manifest_url = serializers.CharField(read_only=True)
    modified = serializers.DateField(read_only=True)
    package_path = serializers.CharField(read_only=True)
    # payment_account = serializers.SerializerMethodField('get_payment_account')
    # payment_required = serializers.SerializerMethodField('get_payment_required')
    public_stats = serializers.BooleanField(read_only=True)
    # price_locale = serializers.SerializerMethodField('get_price_locale')
    # regions = RegionSerializer(read_only=True, source='get_regions')
    ratings = serializers.IntegerField(read_only=True)
    resource_uri = serializers.HyperlinkedIdentityField(view_name='app-detail')
    # release_notes = TranslationSerializerField(read_only=True)
    status = serializers.IntegerField(read_only=True)
    # supported_locales = serializers.SerializerMethodField(
    #     'get_supported_locales')
    # tags = serializers.SerializerMethodField('get_tags')
    # upsell = serializers.SerializerMethodField('get_upsell')
    # user = serializers.SerializerMethodField('get_user_info')
    # versions = serializers.SerializerMethodField('get_versions')
    # weekly_downloads = serializers.SerializerMethodField(
    #     'get_weekly_downloads')
