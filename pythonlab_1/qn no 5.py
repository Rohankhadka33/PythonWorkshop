second = int(input("Enter the value for seconds"))
day = (((second//60)//60)//24)
print(f"Total day for the given second is {day}")
hour = ((second//60)//60)
print(f"the hour for the given second  is {hour}")
minutes = second//60
print(f"total minutes  for  given seconds: {minutes}")