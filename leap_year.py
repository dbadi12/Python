import math 
def leap_year_calc():
    year = int(input('Enter year: '))
    if year % 400 == 0:
        print('Leap year')
    elif year % 100 == 0:
        print('No leap year')    
    elif year % 4 == 0:
        print('Leap year')   
    else:
        print('No leap year')


def main():
    leap_year_calc()

main()