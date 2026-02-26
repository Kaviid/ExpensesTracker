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

expense_categories = {
    "1": "Rent",
    "2": "Utilities",
    "3": "Groceries",
    "4": "Transportation",
    "6": "Phone & Internet",
    "7": "Dining Out",
    "8": "Entertainment",
    "9": "Shopping",
    "10": "Gym / Fitness",
    "11": "Salon / Personal Care",
    "12": "Health & Medical",
    "13": "Gifts",
    "14": "Subscription",
    "15": "Miscellaneous",
    "16": "Router",
    "17": "Phone Call",
    "18": "Hutch Data",
    "19": "Fire Extinguisher",
    "20": "Smile / Saving",
    "21": "Other"
}

