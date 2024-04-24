first_number = float(input('enter a number : '))
second_number = float(input('enter a number : '))
third_number = float(input('enter a number : '))

sum = first_number + second_number + third_number

if first_number != second_number != third_number:
    print(f'The sum of these numbers is {sum}')


if first_number == second_number == third_number:
     sum1 = sum * 4
     print(f'These numbers are the same! \nThe sum of these numbers is {sum} \nMultiplied by 4 this becomes {sum1}')