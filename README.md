Like Zamboni, but a thinner layer.

The intent for this project is to provide an implementation of the Marketplace
API that can be used with both a fake datastore (like flue) and a real database
(like zamboni). It uses REST Framework to provide the API views but doesn't tie
them directly to Django models; instead, calls will be made to an abstract model
API that doesn't rely on database or ORM specifics.

The current code sketch here provides a fragment of the webapp API with a
fake-data backend.
