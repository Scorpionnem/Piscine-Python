def all_thing_is_obj(object: any) -> int:
    found_type = type(object)

    if (found_type == list):
        print("List :", found_type)
    elif (found_type == tuple):
        print("Tuple :", found_type)
    elif (found_type == set):
        print("Set :", found_type)
    elif (found_type == dict):
        print("Dict :", found_type)
    elif (found_type == str):
        print(object, "is in the kitchen :", found_type)
    else:
        print("Type not found")
    return 42
