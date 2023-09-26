month = int(input("enter the month number 1-12: "))

match month:
    case 1:
        print("January")
    case 2:
        print("feb")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("june")
    case 7:
        print("july")
    case 8:
        print("aug")
    case 9:
        print("sep")
    case 10:
        print("oct")
    case 11:
        print("nov")
    case 12:
        print("dec")
    case _:
        print("Invalid month number")

