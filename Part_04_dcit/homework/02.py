workers = {
    "employer_1": {
        "name": "Jhon",
        "salary": 7500
    },
    "employer_2": {
        "name": "Emma",
        "salary": 8000
    },
    "employer_3": {
        "name": "Brad",
        "salary": 500
    }
}

print(workers)

workers["employer_3"]["salary"] = 8500

print(workers)

if workers["employer_3"]["salary"] == 8500 :
    print("OK")
else:
    print("not ok")

