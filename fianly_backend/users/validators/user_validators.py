register_schema = {
    "username": {"type": "string", "required": True},
    "password": {"type": "string", "required": True},
    "first_name": {"type": "string", "required": True},
    "last_name": {"type": "string", "required": True}
}

auth_schema = {
    "user": {"type": "string", "required": True},
    "password": {"type": "string", "required": True}
}
