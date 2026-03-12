def NULL_not_found(object: any) -> int:
    found_type = type(object)

    if (object is None):
        print("Nothing:", object, found_type)
    elif (object != object):
        print("Cheese:", object, found_type)
    elif (object is False and found_type == bool):
        print("Fake:", object, found_type)
    elif (object == 0 and found_type == int):
        print("Zero:", object, found_type)
    elif (object == ''):
        print("Empty:", found_type)
    else:
        print("Type not found")
        return (1)
    return 0
