'''Solve each of the following problems using Python Scripts. Make sure you use  appropriate variable names and comments.
Where there is final answer have Python print it to be screen
       A person's body mass index(BMI) is defined as
         BMI= mass in kg/ (height in m)**2'''
mass= float(input('Enter your weight in kg'))
height= float(input(('Enter your height in metre')))
BMI= (mass/(height**2))
print(f' Your BMI is {BMI}')