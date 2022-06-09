work_hours = int(input('Please enter the number of working hours : '))
pay_hour = int(input('Please enter the pay amount you get per hour : '))

calculate_regular = work_hours * pay_hour

a = input('Type Yes if you work extra hours, and type No if you do not have extra working hours : ')


if a == 'yes':
    extra_hour = int(input('Enter the amount of extra hours : '))
    extra_pay = int(input('Enter the pay amount per extra hour : '))
    calculate_extra = extra_hour * extra_pay
    calculate_all = calculate_regular + calculate_extra
    print(f'Your salary with extra hours is : {calculate_all}')
elif a == 'no':
    print(f'Your salary without extra working hours is : {calculate_regular}')
else:
    print('Enter a vaild text, either Yes or No')