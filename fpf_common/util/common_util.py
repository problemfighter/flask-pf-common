import uuid


def get_uuid() -> str:
    unique_id = str(uuid.uuid1())
    return unique_id.upper()
