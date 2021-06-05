import random

print("Hii, What is your name ?")
name = input()

print('Welcome' + ' ' +  name + ' ' + 'I am thinking of a number between 1 to 10:')
num = random.randint(1,10)

for guesses in range(1,3):
    print("Take a guess:")
    guess = int(input())

    if guess < num:
        print("Your guess is a little low.")

    elif guess > num:
        print("Your guess is too high.")

if guess == num:
    print("Congratulations" + ' ' + name + ' ' + "you have guessed my number in" + str(guesses) +' ' + "guesses!!")

else:
    print("I am sorry, the number was" + ' ' +  str(num))