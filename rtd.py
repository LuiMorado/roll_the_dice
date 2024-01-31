# rtd.py 
import random

# Dice
dice_art = {
  1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
die_height = len(dice_art[1])
die_width = len(dice_art[1] [0])
die_face_separator = " "    

def generate_dice_faces_diagram(dice_values):
  """Return a diagram of dice faces from 'dice_values'.

  The string returned contains a representation of each die.
  For example, if 'dice_values = [4 , 1 , 3 , 2]' then the string should look likes this:
  ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
  

# . . .
def parse_input(input_string):
  """Return 'input_string as an integer between 1 and 6.

  check if 'input_string is an integer number between 1 and 6.
  If so, return an integer with the same value. otherwise, tell the user to enter a valid number and quit the program. """"

  if input_string.strip() in {"1" , "2" , "3" , "4" , "5" , "6"}:
    return init(input_string)
  else:
    print("Pleaseenter a number from 1 to 6.")
    raise SystemExit(1)
    
# Main Code
# Task 1: Get user's Input, validate it.
num_dice_input = input("How many die? [1-6]")
num_dice = parse_input(num-dice_input)

#2 Task 2: Roll the dice
roll_results = roll_dice(num_dice)
print(roll_results) #REMOVE THIS LINE AFTER APP TEST

# Dice Code
# Task 1: import die.
import random
min_value = 1
max_value = 6
roll_again = "yes"
While roll_again == "yes" or roll_again == "y":
  print("Rolling the dices...") 
  break
  print("The values are....")
  break
  value1 = random.randint (min_value , max_value)
  value2 = random.randint (min_value , max_value)
  value3 = random.randint (min_value , max_value)
  value4 = random.randint (min_value , max_value)
  value5 = random.randint (min_value , max_value)
  value6 = random.randint (min_value , max_value)
  roll_again = input("Type 'Y' or 'Yes' to roll the dices again.")
  roll_end = input("Type 'N' or 'No' to stop.")
  break
print("Yeaaaa boiiii")
