my_date=18
your_date=int(input('Type date, honey: '))
if my_date==your_date:
    print('Nya, you did it')
else:
    if my_date<your_date:
        print('It\'s too much')
    elif my_date>your_date:
        print('It\'s too low')
    your_date=int(input('Type date, honey: '))
    if my_date==your_date:
        print('Nya, you did it')
    else:
        print('Sorry, honey. Try again later')
