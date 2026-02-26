import derectory.input_handle as income
from derectory import constant

add = income.Deposite("Kaveesha Dias")

methods_link = {
    '1' : add.deposit,
    '2' : add.expense,
    '3' : add.balance
}

print(constant.ask_list)
user_want = input("What do you need to do : ")

try :
    #user_want is used to get callable method from constant.methods_link dict
    methods_link[user_want]() #We have an error in here (amount) when call another method like balance....
except Exception as KeyError:
    #When user enter a number which isn't valid
    print("\nUSAGE : Only add given methods number <1>")
    print("Exiting...\n")
