#defining input_number function
def input_number():
    num1 = int(input("please input value for num1: "))
    num2 = int(input("please input value for num2: "))
    num3 = int(input("please input value for num3: "))
    return num1, num2, num3

#defining max_num function
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

#defining close function
def close():
    print("\nThe following will ask you to input 3 text and it will return the longest text from the 3 input")


while True:
    num1, num2, num3 = input_number()
    print("\nThe maximum number is: ", max_num(num1, num2, num3))

    again = input("\nWould you like to do it again? (y/n): ")
    if again.lower() != 'y':
        close()
        break

def input_phrase():
    ph1 = input("\nplease enter a text/phrase1: ")
    ph2 = input("please enter a text/phrase2: ")
    ph3 = input("please enter a text/phrase3: ")
    return ph1, ph2, ph3

def max_len(ph1, ph2, ph3):
    if len(ph1) > len(ph2) and len(ph1) > len(ph3):
        return ph1
    elif len(ph2) > len(ph1) and len(ph2) > len(ph3):
        return ph2
    else:
        return ph3

def close():
    print("\nThanks for using my program")

while True:
    ph1, ph2, ph3 = input_phrase()
    print("\nThe longest text is:", max_len(ph1, ph2, ph3))

    again = input("\nWould you like to do it again? (y/n): ")
    if again.lower() != 'y':
        close()
        break

