# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# Assume that any letters in the user’s input will be uppercase. 


def main():

    plate = input("Plate: ")
    if is_valid(plate): #is_valid going to return bool value
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if length_check(s) and first_2_letter_check(s) and number_middle_check(s) and no_punctuation_space_check(s): #I created function for all type of check
        return True
    else:
        return False


def length_check(plate):

    if 2 <= len(plate) <= 6: #Check length of plate
        return True
    else:
        return False

def first_2_letter_check(plate):

    first_2_letter = plate[0:2] # Slice first two value of plate string

    if not first_2_letter.isdecimal(): # Checks whether it's not numeric character 
        return True # If it's not decimal, it's Alphabet ! (Note: punctuation check is checked in other function)
    else:
        return False 
    
def no_punctuation_space_check(plate):

    check = True
    punctuation_space = ["!", "#", "$", "%", "&" , "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";" ,"<" , "=", ">", "?", "@", "[", "]", "^", "`", "{", "|" ,"}", "~",'"'," "]
    for i in plate:
        if i in punctuation_space:
            check = False
            
    if check: return True
    else: return False

def number_middle_check(plate):
    # Itereate each element in that created list and check whether it contain number or not

    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    plate_list = list(plate) # Make new  list 
    sliced_plate_list = plate_list[2:-1] # Slice it using [2:-1], it doesnt include first, second and last element

    for char in sliced_plate_list: # Iterates for each element in the sliced list

        if char in number: # Detects number
                    
            index_for_first_detected_number = plate_list.index(char) # Returns the index of the first occurrence of the detected number. 
            remaining_list = plate_list[index_for_first_detected_number:]
            remaining_string = "".join(remaining_list) # Joints the remaining list into string

            if char == "0": return False # Number starts with 0
            
            if remaining_string.isdecimal(): #Return True or False by check if number isn't in the middle,  break the loop and function
                return True # Number is not in middle
            else: 
                return False #Number is in middle

    return True # Return True if there is no number in the middle 


main()