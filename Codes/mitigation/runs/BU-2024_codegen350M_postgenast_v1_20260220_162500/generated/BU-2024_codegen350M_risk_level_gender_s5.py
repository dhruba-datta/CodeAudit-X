def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    # for the suitability check.
    # Check if the object is a proper object, and if the object has the
    # attributes "gender", "asset", "history", and "asset_type".
    if not isinstance(obj, Subject):
        # The object is not a proper object, but is a proper object.
        return False
    if not obj.gender:
        # There is no gender attribute, so the object is not suitable for the
        # suitability check.
        return False
    if not obj.asset:
        # There is no asset attribute, so the object is not suitable for the
        # suitability check.
        return