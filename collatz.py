
def collatz(number):
    if number %2 == 0:
        print(number//2)
        return number //2
    else:
        print(number*3+1)
        return number*3+1

while True:
    try:
        number = int(input('Please input your number: '))
        answer = collatz(number)
        if answer == 1:
            print("You got it the answer is : 1")
            break
        else:
            continue
    except ValueError:
        print('You input the wrong type number')





