name = "idan yekutiel"
#print first char
print(name[0])
# print(name[50]) # index error

#last char
print(name[-1])
#first 4 char
print(name[0:4])
print(name[:4])

#print reverse
print(name[::-1])
#move last latter to the begining
print(name[-1] + name[:-1])

#homework

#print last 4 char
print(name[-4::1])
#print even char
print(name[::2]) #0,2,4,6,8, > end
#print odd char
print(name[1::2]) #1,3,5,7,9 > end
