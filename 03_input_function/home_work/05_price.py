pencils = int(input("input number how many pencils: "))
pens = int(input("input number how many pens: "))
markers = int(input("input number how many markers: "))

pencil_price = 3
pen_price = pencil_price + 2
marker_price = pen_price + 7

total = (pencils * pencil_price) + (pens * pen_price) + (markers * marker_price)
print(f"the total cost is: {total}$")
