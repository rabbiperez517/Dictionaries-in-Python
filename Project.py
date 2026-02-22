available_numbers = {
    1: 'one',
    2: 'two',      
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: 'zero'
}

phone_number = input("Enter your phone number: ")
for number in phone_number:
    print(available_numbers[int(number)])
