x = 1
y = 1
while y <= 10:
    while x <= 10:
        print(y * x, end="\t")
        x+=1
    print("")
    y += 1
    x = 1

print("_" * 100)

for y in range(1,11):
    for x in range(1,11):
        print(y * x, end="\t")
    print()
