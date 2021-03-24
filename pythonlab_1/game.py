''' game finding a secret number within 3 attemps using while loop'''
a= 10
i= 0
while(i<3):
    match=int(input("Guess the word"))
    if(match==a):
        print("you entered correct number")
        break
    else:
        print("you have guessed incorrect number")
        if(i==2):
            print("Game over")
    i=i+1
    