sum = 0

while sum <= 100:
    user_input = input(">>> ")
    if user_input == '.':
        print(sum)
        break
    try:
        sum += float(user_input)
    except ValueError:
        print(f"{user_input} isn't a number. Try again")
else:
    print("else")