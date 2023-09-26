def check_sum(*numbers: int):
    suummery = sum(numbers)
    if suummery >= 50:
        return f"{suummery} - verification passed"
    else:
        return f"{suummery} - Not Enough"


print(check_sum(8,11))
print(check_sum(10,10,10,10,9))
print(check_sum(20,20,10))
