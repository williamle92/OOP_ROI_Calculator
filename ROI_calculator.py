class ROIcalc():

    #add attribuates for the class to be zero. These are the values that we are going to be using throughout the calculator.
    def __init__(self):
        self.total_income = 0
        self.total_expenses = 0
        self.totalcf = 0
        self.returnoninvest = 0
   #First method to calculate the monthly rental income     
    def income(self):
        print("First things first, we are going to calculate your rental income. Enter 0 for the items that do not apply.")
        #convert the input into integers in order to do calculations.
        rent = int(input("Please enter your total rental income (it is usually rent x number of units): "))
        laundry_storage = int(input("Please enter the total income for laundry or storage: "))
        misc = int(input("Please enter any other miscellaneous income you receive from this property: "))
        self.total_income = rent + laundry_storage + misc
        print(f"Everything is looking good so far! Your total monthly rental income is ${self.total_income}")
        return self.total_income
    
    #Create a method to calculate that expenses of the property.
    def expenses(self):
        print("Now we are going to calculate your expenses. Enter 0 for the items that do not apply")
        expenses1 = int(input("Please enter any tax expenses: "))
        expenses2 = int(input("Please enter your insurance expenses: "))
        expenses3 = int(input("Please enter HOA expenses: "))
        expenses4 = int(input("Please enter vacancy expenses (enter as a whole number percentage ex. 5 for 5%): "))
        expenses5 = int(input("Please enter the expenses for any repairs: "))
        expenses6 = int(input("Please enter expense for capital expenditures: "))
        expenses7 = input("Does this property pay for any utilities? yes/no ")
        if expenses7.lower().strip() == "yes":
            electric = int(input("Please enter the cost of electricity: "))
            water = int(input("Please enter the cost of water per month: ")) 
            sewer = int(input("Please enter the cost of sewage: ")) 
            garbage = int(input("Please enter the cost for garage disposal: ")) 
            gas = int(input("Please enter the cost of gas: ")) 
            util = electric + water + sewer + garbage + gas
        elif expenses7.lower().strip() == "no":
            util = 0
        expenses8 = int(input("Please enter any other miscellaneous expenses not included here: "))  
    
        self.total_expenses = expenses1 + expenses2 + expenses3 + (expenses4/100 *self.total_income) + expenses5 + expenses6 + expenses8 + util
        print(f"Your total expenses is {self.total_expenses}")
        return self.total_expenses
    #Method for determining the cash flow    
    def cash_flow(self):
        print("Calculating cash flow....")
        cfask = input("...Warning! Sensitive financial information may be displayed... enter yes/no to continue. ").lower().strip()
        if cfask == "yes":
            self.totalcf = self.total_income - self.total_expenses
            print(f"Your total cash flow is {self.totalcf}$")
            return self.totalcf
        else: 
            print("Your financial information will not be shown but is still stored in our calculator.")
            self.totalcf = self.total_income - self.total_expenses
            return self.totalcf

    #method for calculating the ROI
    def return_on_investment(self):
        print("Now we are going to calculate the total invesment.")
        downpayment = int(input("Please enter the total downpayment on the property: "))
        closing_cost = int(input("Please enter the closing cost of the property: "))
        repairbudget = int(input("Enter the budget for repairs: "))
        mmisc = int(input("Enter any other miscellaneous costs: "))
        self.total_investment = downpayment + closing_cost + repairbudget + mmisc
        self.returnoninvest = self.totalcf /self.total_investment * 100
        print(f"Your cash on cash return on investment is {self.returnoninvest}%")
        return self.returnoninvest



#while loop to run the program on a loop.
calculator = ROIcalc()
while True: 
    print("Welcome to Williams Return on Investment Calculator!")
    ask = input("What would you like to do: Calculate ROI/Check ROI/Quit ").lower().strip()
    if ask == "quit":
        print("Thank you for using our program!")
        break
        
    elif ask == "check roi":
        if calculator.returnoninvest:
            print(f"Your cash on cash return on investment is {calculator.returnoninvest}%")
        else:
            print("You have not entered in any value into the ROI calculator.")
    elif ask == "calculate roi":
        #calling the methods
        print("Lets get started!")
        calculator.income()
        calculator.expenses()
        calculator.cash_flow()
        calculator.return_on_investment()
