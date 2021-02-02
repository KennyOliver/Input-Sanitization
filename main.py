def test_number():
  """ program to display whether a number is less than 50 or greater than or equal to 50 """
  
  answer = "Y"
  
  while answer == "Y":
    number = int(get_number())
    if number < 50:
      print("number is less than 50")
    else:
      print("number is greater than or equal to 50")
    answer = get_answer()
#------------------------------------------
def get_number():
  """ function that keeps asking the user for input until they have entered a value (presence check) and it is a digit (integer)"""
  number = input("Enter a whole number\n--> ")
  while number == "" or not number.isdigit():
    number = input("Must enter a number\n--> ")
  return number
#------------------------------------------
def get_answer():
  """ function to sanitise the input so only 'Y' or 'N' is returned """
  answer = input("Enter Y or N\n--> ")
  
  while answer not in ["Yes","yes","Y","y","No","no","N","n"]:
    answer = input("Enter Y or N\n--> ")

  if answer in ["Yes","yes","Y","y"]:
    return "Y"
  else:
    return "N"
# main program
test_number()