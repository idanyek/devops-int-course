input = input("enter a text: ")

#print first char
print("first char: ", input[0])

#print last char
print("last char: ", input[-1])

#print middle char
print("middle char: ", input[round(len(input) / 2)])

#print odd char
print("odd char: ", input[1::2])

#print even char
print("even char: ", input[::2])

#print reverse
print("reverse: ", input[::-1])