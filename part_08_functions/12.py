def dedupe_V1(list1: list):
    new_list = []
    for elem in list1:
        if not elem in new_list:
            new_list.append(elem)
    return new_list

def dedupe_V2(list1: list):
    return list(dict.fromkeys(list1))


a = [1, 2, 3, 4, 3, 2, 1]

print(dedupe_V1(a))
print(dedupe_V2(a))