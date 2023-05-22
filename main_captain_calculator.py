
# Loot = Investment
# Bounty = Profit

# Client = Client
# Client Company = Client company

# Four Square Method 

# Incomes:  - Rental_Ship_Income(200,000 shillings and a pack of smokes) - Each part of the ship rents for 2.5 shillings
#           - Ship_Docking_Income --- (0 shilling per month)
#           - Misc_Income --- (0 shilling per month)

# TOTAL INCOME: --- (2,000 shillings per month)

# Expenses: - Ship_Tax --- (150 shillings per month)
#           - Ship_Insurance --- (100 shillings per month)
#           - Ship_Utilies (Sub catagories - well_water, sewage) --- (0 shillings per month)
#           - SOA(Ship_Owners_Association) --- (0 shillings per month)
#           - Vacency_Abandoned_Ship --- (100 shillings per month)
#           - Ship_Repairs(For Damage by Renter) --- (100 shillings per month)
#           - CopEx(For Big Ship Repairs Fixing big things) --- (100 shillings per month)
#           - Ship_Property_Management --- (200 shillings per month)
#           - Ship_Mortage --- (860 shillings per month)

# TOTAL MONTHLY EXPENSES: --- (1,610 shillings per month)

# Cashflow: (Income-Expenses) (2000 shillings -1610 shillings = 390 shillings per month)

# TOTAL MONTHLY CASH FLOW: --- (390 Shillings per month)

# Cash on Cash ROI (Return on Investment):
#           - Downpayment (40,000 shillings)
#           - Closing Costs (3,000 shillings)
#           - Rehab Budget (7,000 shillings)
#           - Misc Other (0 shillings)

# TOTAL INVESTMENT : --- (50,000 shillings)

# 390 X 12 = 4,680 shillings

# def the cashflow to investment for percentage
# Annual_Cashflow / Total_Investment
# 4680 / 50,000 = 9.36%

# Cash on cash ROI  9.36%

import client

class main_captain_calculator: # Seadog Brandon ROI Calculator
    def main_captain_calculator(self, income, expense, total_investment):
        self.income = income  # Variables or Attributes
        self.expense = expense  # Variables or Attributes
        self.total_investment = total_investment # Variables or Attributes

    def income(self, rental_ship_income, ship_docking_income, misc_income): # Definition of Income
        self.rental_ship_income = rental_ship_income (input("200,000 Shillings & Pack of Smokes"))
        self.ship_docking_income = ship_docking_income (input("0 Shillings per month"))
        self.misc_income = misc_income (input("0 Shillings per month"))

    def expenses(self, ship_tax, ship_insurance, ship_utilies, SOA, vacency_abandoned_ship, ship_repairs, copex, ship_property_management, ship_mortgage): # Definition of Expenses
        self.ship_tax = ship_tax (input("150 Shillings per month"))
        self.ship_insurance = ship_insurance(input("100 Shillings per month"))
        self.ship_utilies = ship_utilies(input("0 Shillings per month"))
        self.SOA = SOA(input("0 Shillings per month"))
        self.vacency_abandoned_ship = vacency_abandoned_ship(input("100 Shillings per month"))
        self.ship_repairs = ship_repairs(input("100 Shillings per month"))
        self.copex = copex(input("100 Shillings per month"))
        self.ship_property_management = ship_property_management(input("200 Shillings per month"))
        self.ship_mortgage = ship_mortgage(input("860 Shillings per month"))

    def cash_flow(self, income, expenses, cash_flow): # Definition of Cashflow
        income - expenses
        return cash_flow 

    def cash_on_cash_ROI(self, downpayment, closing_costs, rehab_budget, misc_other): # Definition of Cash on Cash
        self.downpayment = downpayment(input("40,000 shillings"))
        self.closing_costs = closing_costs(input("3,000 Shillings"))
        self.rehab_budget = rehab_budget(input("7,000 Shillings"))
        self.misc_other = misc_other(input("0 Shillings"))


#     def ROI_calculator(self):
#         print("Arrr Ye Wishin To Calculate ? Ye Haut Come To Thee Right Place, Welcome To Me Captain's ROI Calculator.") # Game started
#         self.calculator_started = True
#         self.make_the_client_calculator()
#         self.client_show_total(True)

#         self.income.show_total(True) # Income shows total
#         self.expense.show_total(True) # Expense shows total

#         income_calculation_value = self.income.get_calculation_value() # Income total of incomes
#         expense_calculation_value = self.expense.get_calculation_value() # Expense total of expenses


# def income_input(captain_calculator):
    
#     if captain_calculator.calculation_started is not True:
#        income_choice = input("Me Hearties. Shall We Gather Some Loot What Say Ye? (Enter: (y/n) )") # Yay or Nay
#     if income_choice == "n":
#             print("Blimey, Ye Scurvy Dog, Ye Abandoned Ship.") # Income inputs stop
#             captain_calculator.captain_calculator_started = False
#             quit()

#     income_choice = input("Ye Wish To Add Loot or Stop, Thee Choice Be Yer's, What Say Ye? Enter: (y/n): ") # Yay or Nay
#     choice = income_choice.lower()
#     if choice == "y" or choice == "n" or choice == "yay" or choice == "nay": # Yay or Nay
#         return income_choice
#     else: 
#         income_choise = input(f"Avast...Read Me Regulations Again Matey: [{income_choice}]. Shall Ye Try Again? ... Enter y/n or yay/nay or quit: ") # If invalid selection
#         if (income_choise.lower == "quit"):
#             print("Shiver Me Timbers... Ye Abandoned Ship, Guess Ye Doesn't Like Loot.") # Income quit
#             quit()
#     return income_choise
    


# # calculator = calculator()
# # income_input(addition)
# # expenses_input(subtraction)
# # calculation_started.() # start ROI calculator
