def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y): return x * y  # E701: multiple statements on one line

def divide(x, y):
    if y == 0:
        print("Cannot divide by zero")  # W1201: Use logging instead of print
        return None
    return x / y

def main():
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(5, 3))
    print("Division:", divide(5, 0))

main()
