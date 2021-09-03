# converts string to str, int, float,bool
def convert_str_to_any(value, toType):
    default_value = "Unable to make Conversation"
    type_of_value = {
        "str": value,
        "int": int(value),
        "float": float(value),
        "bool": bool(value) #On convertion it will be true
    }
    return type_of_value.get(toType, default_value)
