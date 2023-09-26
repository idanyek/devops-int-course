
array = [10,20,30,40,50]

after_filter = filter(lambda x: x >= 30, array)
print(after_filter)
print(type(after_filter))

print(list(after_filter))

server_json = [
    {'task_name': 'Learn python', 'status': "In progress"},
    {'task_name': 'Learn Java', 'status': "Done"},
    {'task_name': 'Learn typeScript', 'status': "Done"},
    {'task_name': 'Learn DevOps', 'status': "New"},
]

after_filter = list(filter(lambda x: x['status'] == 'Done', server_json))
print(after_filter)

after_filter = list(filter(lambda x: x['status'] == 'In progress' or x['status'] == 'New', server_json))
print(after_filter)

after_filter = list(filter(lambda x: "python" in x['task_name'], server_json))
print(after_filter)