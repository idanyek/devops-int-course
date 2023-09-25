numbers = [12, 75, 150, 180, 145, 525, 50]

for n in numbers:
    if n % 5 == 0:
        if n > 150:
            continue
        elif n > 500:
            break
        print(n)