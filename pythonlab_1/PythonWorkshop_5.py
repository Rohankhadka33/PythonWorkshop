# N students take K apples and distribute them among eachothers evenly. The remaining(the undivisible) part remains in the basket? The program reads the number N and K. It should prnt the two answers for the questions above.
N= int(input('Enter the numbers  of students'))
K= int(input('Enter the numbers of apples'))
A= N//K
B= N%K
print(f'Each student will get',A, 'apple')
print(f'The remaining number of apple in the basket is',B)