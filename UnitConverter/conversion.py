"""I will be making a program that will convert the units in a recipe for you"""

print("""HELLO! WELCOME TO JALYN'S UNIT CONVERTER FOR YOUR COOKING NEEDS!""")

#ASK THE USER WHAT THEY ARE MAKING
recipe = input("What are you making? ")

#print that what they are making is a good choice
print(f"{recipe} is a wonderful choice. now lets help you make {recipe}!")
#where the function restarts from
def start():
    #available conversions tuple
    available_coversions = [ 
       (1,'tbsp','tsp'),
        (2,'tsp','tbsp'),
        (3,'c'  , 'oz'),
        (4,'oz' ,'c'),
        (5,'pt' ,'c'),
        (6,'qt' ,'c'),
        (7,'c'  , 'qt'),
        (8,'qt' , 'pt'),
        (9,'pt' , 'qt'),
       (10,'gal','qt'),
        (11,'qt', 'gal'),]

    print(f"Here is a list of the conversions we offer!:") 

    #printing the tuple and adding an arrow pointing to the conversions
    for conversion_number, from_unit, to_unit in available_coversions:
        print(f"{conversion_number}) {from_unit} -> {to_unit}")
    #subtracting 1 to get correct conversion input
    conversion = input("Enter the number of the conversion you want to use: ")
    conversion_index = int(conversion) -1
    #calculation
    conversion_number, from_unit, to_unit = available_coversions[conversion_index]

    from_value = float(input(f"Enter how many {from_unit}: "))

    if conversion_number == 1:
        to_value = from_value * 3
        print(f"Your conversion is: {from_value} {from_unit} = {to_value} {to_unit}")

    elif conversion_number == 2:
        to_value = from_value /3
        print(f"Your conversion is: {from_value} {from_unit} = {to_value} {to_unit}")

    elif conversion_number == 3:
        to_value = from_value *8
        print(f"Your conversion is: {from_value} {from_unit} = {to_value} {to_unit}")

    elif conversion_number == 4:
        to_value = from_value /8
        print(f"Your conversion is: {from_value} {from_unit} = {to_value} {to_unit}")

    elif conversion_number == 5:
        to_value = from_value *2.4
        print(f"Your conversion is: {from_value} {from_unit} = {to_value} {to_unit}")

    elif conversion_number == 6:
        to_value = from_value *4
        print(f"Your conversion is: {from_value} {from_unit} = {to_value} {to_unit}")  

    elif conversion_number == 7:
        to_value = from_value /4
        print(f"Your conversion is: {from_value} {from_unit} = {to_value} {to_unit}")
        
    elif conversion_number == 8:
        to_value = from_value *1.665
        print(f"Your conversion is: {from_value} {from_unit} = {to_value} {to_unit}")

    elif conversion_number == 9:
        to_value = from_value /1.665
        print(f"Your conversion is: {from_value} {from_unit} = {to_value} {to_unit}")

    elif conversion_number == 10:
        to_value = from_value *4
        print(f"Your conversion is: {from_value} {from_unit} = {to_value} {to_unit}")

    elif conversion_number == 11:
        to_value = from_value /4
        print(f"Your conversion is: {from_value} {from_unit} = {to_value} {to_unit}")

    more_conversions = input("Would you like to choose another conversion?(y/n):").lower()

    if more_conversions == "y":
        start()
    else:    
        print(f"Thank You for using Jalyn's conversions Enjoy your {recipe}!")
        exit()
start()

