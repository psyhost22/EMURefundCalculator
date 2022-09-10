# Refund Cost Calculator by Jason Rousell
# 9/9/2022
# In wake of professor strike, this small tool calculates how much money
# you have wasted, or that the university has wasted, while you
# weren't able to attend class.

# This tool doesn't account for online fees, other course fees, or material costs. Add those if you want

totalCredit = int(input("Type the total amount of credit hours that you are taking.\n\n"))
classCredit = int(input("Type the amount of credit hours for this class. Most classes are worth three credit hours, "
                        "but some are worth more.\n\n"))
classDays = int(input("Type how many days a week you have this class. EX: If you have this class on Monday and "
                      "Wednesday, type 2.\n\n")) * 14

# This project assumes that total class days in a semester = 14 days for each weekday (14 Mondays, 14 Tuesdays, etc.)

daysMissed = int(input("Type how many days of this class you have missed. Do not count holidays or other similar "
                       "break days.\n\n"))
gradUndergrad = int(input("If the class is counted in UNDERGRADUATE credits (level 100-499), type 1. \nIf the class is "
                          "counted in GRADUATE credits, AND the class is course level 500-699, type 2. \nIf the class "
                          "is counted in GRADUATE credits, AND the class is course level 700+, type 3.\n\n"))
residentNon = int(input("Are you a resident of Michigan? Type 1 or 2 for \"yes\" or \"no\".\n\n"))

# Residents vs. Non-Residents have different rates at the Graduate level only

if gradUndergrad == 1:
    if totalCredit < 12:
        creditCost = (608 * classCredit)
    if 12 <= totalCredit <= 16:
        creditCost = 7250
    if totalCredit >= 17:
        creditCost = 7250 + (608 * (totalCredit - 16))

if gradUndergrad == 2:
    if residentNon == 1:
        creditCost = (938.50 * classCredit)
    if residentNon == 2:
        creditCost = (1626.50 * classCredit)

if gradUndergrad == 1:
    if residentNon == 1:
        creditCost = (1074.00 * classCredit)
    if residentNon == 2:
        creditCost = (1834.00 * classCredit)

dailyCost = creditCost / classDays

refundNeeded = round(dailyCost * daysMissed, 2)

print("Here's the math: you deserve a refund of", refundNeeded,"for the classes you've missed.")