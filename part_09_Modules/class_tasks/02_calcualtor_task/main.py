from calculator_module import calculate


def __main__():
    num1, operator, num2 = input( "enter the math request with spaces as separate: " ).split()

    try:
        print( calculate( int( num1 ), int( num2 ), operator ) )
    except ValueError:
        print( f"Invalid request: {num1} {operator} {num2}" )


while True:
    __main__()
