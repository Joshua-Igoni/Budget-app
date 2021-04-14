import random

Food_budget = globals()
Entertainment_budget = globals()
Clothing_budget = globals()
Business_budget = globals()
Food_budget = 1000000
Entertainment_budget = 1000000
Clothing_budget = 1000000
Business_budget = 1000000

SelectionOptions = ["1. Food budget",
                    "2. Entertainment budget",
                    "3. Clothing budget",
                    "4. Business budget",
                    "5. Exit application"
                    ]
budgetOperations = ["1. withdraw",
                    "2. deposit",
                    "3. check balance",
                    "4. transfer"
                    ]


class Budget:

    def __init__(self, name):
        self.name = name

    def withdraw(self):
        global Food_budget, Entertainment_budget, Clothing_budget, Business_budget
        loading = random.randrange(11, 99)
        if self is Foodcategory:
            withdrawal_amount = int(input('amount to withdraw?\n'))
            Food_budget -= withdrawal_amount
            print("*********************PROCESSING", loading, "%**********************")
            print('You have successfully withdrawn ', withdrawal_amount, "from Food budget")
        elif self is Entertainmentcategory:
            withdrawal_amount = int(input('amount to withdraw?\n'))
            Entertainment_budget -= withdrawal_amount
            print("*********************PROCESSING", loading, "%**********************")
            print('You have successfully withdrawn ', withdrawal_amount, "from Entertainment budget")
        elif self is Clothingcategory:
            withdrawal_amount = int(input('amount to withdraw?\n'))
            Clothing_budget -= withdrawal_amount
            print("*********************PROCESSING", loading, "%**********************")
            print('You have successfully withdrawn ', withdrawal_amount, "from Clothing budget")
        elif self is Businesscategory:
            withdrawal_amount = int(input('amount to withdraw?\n'))
            Business_budget -= withdrawal_amount
            print("*********************PROCESSING", loading, "%**********************")
            print('You have successfully withdrawn ', withdrawal_amount, "from Business budget")

    def deposit(self):
        global Food_budget, Entertainment_budget, Clothing_budget, Business_budget
        loading = random.randrange(11, 99)
        if self is Foodcategory:
            deposit_amount = int(input('amount to deposit?\n'))
            Food_budget += deposit_amount
            print("*************************PROCESSING", loading, "%************************")
            print("you have succesfully deposited ", deposit_amount, " into Food budget")
        elif self is Entertainmentcategory:
            deposit_amount = int(input('amount to deposit?\n'))
            Entertainment_budget += deposit_amount
            print("*************************PROCESSING", loading, "%************************")
            print("you have succesfully deposited ", deposit_amount, " into Entertainment budget")
        elif self is Clothingcategory:
            deposit_amount = int(input('amount to deposit?\n'))
            Clothing_budget += deposit_amount
            print("*************************PROCESSING", loading, "%************************")
            print("you have succesfully deposited ", deposit_amount, " into Clothing budget")
        elif self is Businesscategory:
            deposit_amount = int(input('amount to deposit?\n'))
            Business_budget += deposit_amount
            print("*************************PROCESSING", loading, "%************************")
            print("you have succesfully deposited ", deposit_amount, " into Business budget")

    def checkbalance(self):
        global Food_budget, Entertainment_budget, Clothing_budget, Business_budget
        loading = random.randrange(11, 99)
        if self is Foodcategory:
            print("*****************CALCULATING_BALANCE", loading, "******************")
            print("the current balance for this budget is ", Food_budget)
        elif self is Entertainmentcategory:
            print("*****************CALCULATING_BALANCE", loading, "******************")
            print("the current balance for this budget is ", Entertainment_budget)
        elif self is Clothingcategory:
            print("*****************CALCULATING_BALANCE", loading, "******************")
            print("the current balance for this budget is ", Clothing_budget)
        elif self is Businesscategory:
            print("*****************CALCULATING_BALANCE", loading, "******************")
            print("the current balance for this budget is ", Business_budget)

    def transfer(self):
        global Food_budget, Entertainment_budget, Clothing_budget, Business_budget
        loading = random.randrange(11, 99)
        if self is Foodcategory:
            for items in SelectionOptions:
                if items == "1. Food budget":
                    continue
                print(items)
            selection = int(input('which budget do you want to transfer to?\n'))
            if selection == 2:
                transfer_amount = int(input('pleas state amount: \n'))
                Food_budget -= transfer_amount
                Entertainment_budget += transfer_amount
                print('*****transaction_processing', loading, '******')
                print("you have successfully transfered ", transfer_amount,
                      "to Entertainment budget,\n please check your balance")
            elif selection == 3:
                transfer_amount = int(input('pleas state amount: \n'))
                Food_budget -= transfer_amount
                Clothing_budget += transfer_amount
                print('*****transaction_processing', loading, '******')
                print("you have successfully transfered ", transfer_amount,
                      "to Clothing budget,\n please check your balance")
            elif selection == 4:
                transfer_amount = int(input('pleas state amount: \n'))
                Food_budget -= transfer_amount
                Business_budget += transfer_amount
                print('*****transaction_processing', loading, '******')
                print("you have successfully transfered ", transfer_amount,
                      "to Business budget,\n please check your balance")
        elif self is Entertainmentcategory:
            for items in SelectionOptions:
                if items == "2. Entertainment budget":
                    continue
                print(items)
            selection = int(input('which budget do you want to transfer to?\n'))
            if selection == 1:
                transfer_amount = int(input('pleas state amount: \n'))
                Entertainment_budget -= transfer_amount
                Food_budget += transfer_amount
                print('*****transaction_processing', loading, '******')
                print("you have successfully transfered ", transfer_amount,
                      "to Food budget,\n please check your balance")
            elif selection == 3:
                transfer_amount = int(input('pleas state amount: \n'))
                Entertainment_budget -= transfer_amount
                Clothing_budget += transfer_amount
                print('*****transaction_processing', loading, '******')
                print("you have successfully transfered ", transfer_amount,
                      "to Clothing budget,\n please check your balance")
            elif selection == 4:
                transfer_amount = int(input('pleas state amount: \n'))
                Entertainment_budget -= transfer_amount
                Business_budget += transfer_amount
                print('*****transaction_processing', loading, '******')
                print("you have successfully transfered ", transfer_amount,
                      "to Business budget,\n please check your balance")
        elif self is Clothingcategory:
            for items in SelectionOptions:
                if items == "3. Clothing budget":
                    continue
                print(items)
            selection = int(input('which budget do you want to transfer to?\n'))
            if selection == 1:
                transfer_amount = int(input('pleas state amount: \n'))
                Clothing_budget-= transfer_amount
                Food_budget += transfer_amount
                print('*****transaction_processing', loading, '******')
                print("you have successfully transfered ", transfer_amount,
                      "to Food budget,\n please check your balance")
            elif selection == 2:
                transfer_amount = int(input('pleas state amount: \n'))
                Clothing_budget -= transfer_amount
                Entertainment_budget += transfer_amount
                print('*****transaction_processing', loading, '******')
                print("you have successfully transfered ", transfer_amount,
                      "to Entertainment budget,\n please check your balance")
            elif selection == 4:
                transfer_amount = int(input('pleas state amount: \n'))
                Clothing_budget -= transfer_amount
                Business_budget += transfer_amount
                print('*****transaction_processing', loading, '******')
                print("you have successfully transfered ", transfer_amount,
                      "to Business budget,\n please check your balance")
        elif self is Businesscategory:
            for items in SelectionOptions:
                if items == "4. Business budget":
                    continue
                print(items)
            selection = int(input('which budget do you want to transfer to?\n'))
            if selection == 1:
                transfer_amount = int(input('pleas state amount: \n'))
                Business_budget -= transfer_amount
                Food_budget += transfer_amount
                print('*****transaction_processing', loading, '******')
                print("you have successfully transfered ", transfer_amount,
                      "to Food budget,\n please check your balance")
            elif selection == 3:
                transfer_amount = int(input('pleas state amount: \n'))
                Business_budget -= transfer_amount
                Clothing_budget += transfer_amount
                print('*****transaction_processing', loading, '******')
                print("you have successfully transfered ", transfer_amount,
                      "to Clothing budget,\n please check your balance")
            elif selection == 2:
                transfer_amount = int(input('pleas state amount: \n'))
                Business_budget -= transfer_amount
                Entertainment_budget += transfer_amount
                print('*****transaction_processing', loading, '******')
                print("you have successfully transfered ", transfer_amount,
                      "to Entertainment budget,\n please check your balance")


Foodcategory = Budget("Food")
Entertainmentcategory = Budget("entertainment")
Clothingcategory = Budget("clothing")
Businesscategory = Budget("business")


def init():
    print("Budget App ZURI")
    print("what Budget would you like to work with?\n")
    for items in SelectionOptions:
        print(items)
    Budgetselection = int(input("select an option above\n"))
    if Budgetselection == 1:
        for items in budgetOperations:
            print(items)

        OperationSelection = int(input("what would you like to do?\n"))
        if OperationSelection == 1:
            Foodcategory.withdraw()
            init()
        elif OperationSelection == 2:
            Foodcategory.deposit()
            init()
        elif OperationSelection == 3:
            Foodcategory.checkbalance()
            init()
        elif OperationSelection == 4:
            Foodcategory.transfer()
            init()
        else:
            print("you have entered a wrong input.\n please try again")
            init()
    elif Budgetselection == 2:
        for items in budgetOperations:
            print(items)

        OperationSelection = int(input("what would you like to do?\n"))
        if OperationSelection == 1:
            Entertainmentcategory.withdraw()
            init()
        elif OperationSelection == 2:
            Entertainmentcategory.deposit()
            init()
        elif OperationSelection == 3:
            Entertainmentcategory.checkbalance()
            init()
        elif OperationSelection == 4:
            Entertainmentcategory.transfer()
            init()
        else:
            print("you have entered a wrong input.\n please try again")
            init()
    elif Budgetselection == 3:
        for items in budgetOperations:
            print(items)

        OperationSelection = int(input("what would you like to do?\n"))
        if OperationSelection == 1:
            Clothingcategory.withdraw()
            init()
        elif OperationSelection == 2:
            Clothingcategory.deposit()
            init()
        elif OperationSelection == 3:
            Clothingcategory.checkbalance()
            init()
        elif OperationSelection == 4:
            Clothingcategory.transfer()
            init()
        else:
            print("you have entered a wrong input.\n please try again")
            init()
    elif Budgetselection == 4:
        for items in budgetOperations:
            print(items)

        OperationSelection = int(input("what would you like to do?\n"))
        if OperationSelection == 1:
            Businesscategory.withdraw()
            init()
        elif OperationSelection == 2:
            Businesscategory.deposit()
            init()
        elif OperationSelection == 3:
            Businesscategory.checkbalance()
            init()
        elif OperationSelection == 4:
            Businesscategory.transfer()
            init()
        else:
            print("you have entered a wrong input.\n please try again")
            init()
    else:
        print("its a good habit to keep track of your budget activities")
        print("Zuri budget app is always here to facilitate the process")
        print("come back again sometime")
        exit()


init()
