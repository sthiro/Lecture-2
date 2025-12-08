# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# Assume that any letters in the user’s input will be uppercase. 

# #initial plan
# 2 <= len(string) <= 6
# slice the list [0:2] and check whether they are letters or not
# use in statement to check whether there are punctuation and spaces
# check endwith method to check whether number is in end 

def main():
    plate = input("Plate: ")
    if is_valid(plate): #is_valid going to return bool value
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length_check(s) and  first_2_letter_check() and end_is_number_check() and only_letter_number_check():
        return True
    else:
        return False


main()