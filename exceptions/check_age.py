from invalid_age_error import InvalidAgeError

def check_age(age):
    if age < 18 or age > 65:
        raise InvalidAgeError(age)
    else:
        print(f'Age {age} is valid!')

try:
    age_input = int(input("Enter you age: "))
    check_age(age_input)
except InvalidAgeError as e:
    print(f'Error: {e}')
except ValueError:
    print('Invalid input! Please enter a number')