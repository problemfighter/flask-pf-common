
def copy_dict_to_object(dictionary: dict, data_object: object):
    if dictionary and data_object:
        for dict_key in dictionary:
            value = dictionary[dict_key]
            if hasattr(data_object, dict_key):
                setattr(data_object, dict_key, value)
    return data_object


def get_object_to_fields(data_object: object):
    fields = []
    for field in dir(data_object):
        if not field.startswith('__'):
            fields.append(field)
    return fields


def copy_object_to_object(source_object: object, dst_object: object):
    fields = get_object_to_fields(dst_object)
    if fields and source_object:
        for field in fields:
            if hasattr(source_object, field):
                setattr(dst_object, field, getattr(source_object, field))
    return dst_object
