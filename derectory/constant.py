import derectory.input_handle as income

add = income.Deposite('Kaveesha Dias')

ask_list ="""[1] Add Income
[2] Add Expences
[3] Check Balance
[4] Current Status
"""


methods_link = {
    '1' : add.deposit,
    '2' : add.expense,
    '3' : add.balance
}