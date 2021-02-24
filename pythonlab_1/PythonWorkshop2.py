#Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a seperate line.
length= int(input('Enter the value of length of the triangle'))
height= int(input('Enter the value of height of the triangle'))
a= 0.5
area= a*length*height
print(f'The area of the triangle is',area)