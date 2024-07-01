year = int(input("Which year you want to check? "))

if (year%4 == 0):
    if(year%100 == 0):
        if(year%400 ==0):
            print(f'So the yaer {year} is a leap year')
        else:
           print(f'So the yaer {year} is not a leap year') 
        
    else:
        print(f'So the yaer {year} is a leap year')
    
else:
    print(f'So the yaer {year} is not a leap year')