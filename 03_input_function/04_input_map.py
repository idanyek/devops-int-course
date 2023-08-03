score1, score2, score3, score4 = map(int,input("please enter your scores: ").split())

print(f"score1: {score1} - type: {type(score1)}")
print(f"score2: {score2} - type: {type(score2)}")
print(f"score3: {score3} - type: {type(score3)}")
print(f"score4: {score4} - type: {type(score4)}")

sum = score1 + score2 + score3 + score4
print(sum)

string = input("please enter your scores: ")
print (string)
string_split = string.split()
print(string_split)
print(map(int,string_split))
