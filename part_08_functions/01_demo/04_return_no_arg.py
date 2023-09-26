def get_today_date():
    import datetime
    return datetime.date.today()

def get_time():
    import datetime
    return datetime.datetime.now()

print(get_today_date())
print(get_time())