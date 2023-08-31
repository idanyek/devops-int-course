emails = {}

emails["ashley"] = "ashely@gmail.com"
emails["craig"] = "craig@gmail.com"
emails["elizabeth"] = "elizabeth@gmail.com"

print(f"{emails= }")

del emails["craig"]

print(f"{emails= }")

emails["dalton"] = "dalton@gmail.com"

print(f"{emails= }")

users = list(emails.keys())
print(f"{users= }")

email_lists = list(emails.values())
print(f"{email_lists= }")

pairs = list(emails.items())
print(f"{pairs= }")