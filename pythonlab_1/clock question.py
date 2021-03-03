'''Given the integer N- the number of minutes that is passed since midnight - how many hours and minutes are displayed
on the 24h digital clock? The program should print two numbers; the numbers of hours(between 0 and 59)'''
N= int(input('Enter the number'))
hours=(N//60)
minutes=(N%60)
print(f'the hours is {hours}')
print(f'The minutes is {minutes}')
print(f'Its {hours}:{minutes} now')