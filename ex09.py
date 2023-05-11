result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input('>>> ')
    if wait_for_number:
        try:
            operand = float(user_input)
        except ValueError:
            print(f'\'{user_input}\' is not a number. Try again')
            continue
        else:
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            elif operator == '/':
                if operand == 0:
                    print('Division by zero. Try again')
                    continue
                else:
                    result /= operand
            elif operator is None:
                result = operand
            wait_for_number = False
    else:
        if user_input == '+' or user_input == '-' or user_input == '*' or user_input == '/':
            operator = user_input
            wait_for_number = True
        elif user_input == '=':
            break
        else:
            print(f'{user_input} is not a \'+\' or \'-\' or \'/\' or \'*\' or \'=\'. Try again')

print(f'Result: {result}')

# Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "], результат 18.0
# Друга: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0