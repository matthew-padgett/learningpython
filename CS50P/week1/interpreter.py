def main():
    operand_one, operator, operand_two = get_user_expression()
    operation = get_operator_and_operate(operator)
    answer = operation(operand_one, operand_two)
    print(answer)

def get_user_expression():
    operand_one, operator, operand_two = input("Expression: ").split()
    operand_one = float(operand_one)
    operand_two = float(operand_two)
    return operand_one, operator, operand_two

def get_operator_and_operate(operator):
    if operator == "+":
        return add
    elif operator == "-":
        return subtract
    elif operator == "*":
        return multiply
    elif operator == "/":
        return divide
    else:
        return None

def add(operand_one, operand_two):
    answer = operand_one + operand_two
    return answer

def subtract(operand_one, operand_two):
    answer = operand_one - operand_two
    return answer

def multiply(operand_one, operand_two):
    answer = operand_one * operand_two
    return answer

def divide(operand_one, operand_two):
    answer = operand_one / operand_two
    return answer

if __name__ == "__main__":
    main()