from config.permissions import Permission

# Generate the dictionary
permissions_enum = {value: member for member, value in Permission.__members__.items()}
def maybe_get_permission_from_str(permission_name: str):
    return permissions_enum[permission_name]

