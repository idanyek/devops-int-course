def _add(x: float, y: float):
    return x + y


def _subtract(x: float, y: float):
    return x - y


def _multiply(x: float , y: float):
   return x * y


def _divide(x: float, y: float):
        return x / y



def calculate(x: float, y: float, operator: str):
    match operator:
        case "+":
            return _add(x,y)
        case "-":
            return _subtract(x,y)
        case "*":
            return _multiply(x,y)
        case "/":
            return _divide(x,y)
        case _:
            raise ValueError(f"Invalid operator '{operator}, enter one of the following oprators: (+,-,*,/)")


def run_calculator():
    try:
        num1, operator, num2 = input("enter the math request with spaces as separate (sample: 12 + 25): ").split()
        return f"{num1} {operator} {num2} = {calculate(float(num1), float(num2), operator)}"
    except ValueError as error:
        return f"\tERROR: {error}.\n\t\tplease try again...\n"
    except ZeroDivisionError:
        return f"{num1} {operator} {num2} = Cannot divide by 0. please try again..."


