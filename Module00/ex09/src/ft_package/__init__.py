def count_in_list(list : list, i) -> int:
    res : int = 0
    for item in list:
    	if item == i:
            res += 1
    return res
