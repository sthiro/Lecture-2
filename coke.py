#  The user has inputted at least 50 cents, output how many cents in change the user is owed.
#  Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
#  Machine accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

ammount_due = 50

while ammount_due > 0:
    print("Amount Due:",ammount_due)
    user_input = int(input("Insert Coin: "))
    
    if user_input in [25, 10, 5]:
        ammount_due = ammount_due - user_input

print("Change Owed:",abs(ammount_due))