'''A school decided to replace the desks in  three classrooms. Each desk sits two students. Given the number of students
 in each class, print  the smallest possible number of desks that can be  purchased.
 The program should read three integers. the numbers of studets in each of the three classes, a,b and c respectively
 '''
a= int(input('Enter the number of students in 1st class'))
b= int(input('Enter the number of students in 2nd class '))
c= int(input('Enter  the number of  students in 3rd class'))
sum= a+b+c
desk=sum/2
print(f'The number of required desk is {desk}')