#youssef ehab mohamed
#ID:20210466
sum = 0
def game():
    global sum
    while sum < 100:
        num1 = int(input("player1,enter a number from 1 to 10: "))
        while num1 > 10 or num1 < 1:
            print("wrong number")
            num1 = int(input("enter another number from 1 to 10: "))
        while sum + num1 > 100:
            print("wrong number")
            num1 = int(input("enter smaller number: "))
        sum = sum + num1
        print("Sum of numbers = " + str(sum))
        if sum == 100:
            print("player 1 win")
        else:
            play()

def play():
    global sum
    num2 = int(input("player2,enter a number from 1 to 10: "))
    while num2 > 10 or num2 < 1:
        print("wrong number")
        num2 = int(input("enter another number from 1 to 10: "))
    while sum + num2 > 100:
        print("wrong number")
        num2 = int(input("enter smaller number: "))
    sum = sum + num2
    print("Sum of numbers = " + str(sum))
    if sum == 100:
        print("player 2 win")

game()
