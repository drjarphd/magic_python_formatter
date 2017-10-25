import re

def format_text(n):
    # DEFINITION: Takes a string as input and splits the
    # string into a list. The list items are then sent to
    # capital_case where they are capitalized individually
    new_string = re.split('; |, ',n)
    for x in new_string:
        capital_case(x)
        print(capital_case(x))
    
def capital_case(n):
    # DEFINITION: Returns a new string in capital case
    index_length = len(n)
    new_string = n[0].upper() + n[1:index_length].lower()
    return (new_string)

def upper_case(n):
    # DEFINITION: Returns a new string in upper case
    new_string = n.upper()
    return (new_string)

def number_processing(n):
    # DEFINITION: Helper function for format_number
    num = str(n)
    if len(num) == 10 :
        return format_number(num,3)
    if len(num) % 3 == 0 :
        return format_number(num,3)
    if len(num) % 4 == 0:
        return format_number(num,4)        
    else:
        return format_number(num,2)

def format_number(n,number_length):
    # DEFINITION: Returns a formatted string of numbers   
    new_string = '-'.join(n[i:i+number_length] for i in range(0, len(n), number_length))
    return (new_string)


sample_string = "this is a SAMPLE string to test the pRoGrAm"
second_sample_string = "The quick brown fox jumps over the lazy dog"
sample_number = 1815276125

format_text(sample_string)
print(capital_case("hello"))
print(upper_case("hello"))
print(number_processing(sample_number))
