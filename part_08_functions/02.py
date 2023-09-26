names = ["Yoav", "Ron", "Aviva","Ronen", "Dan" ,"Galit"]

print(list(map(lambda name: len(name),names)))
print(list(filter(lambda name: len(name) > 4,names)))
