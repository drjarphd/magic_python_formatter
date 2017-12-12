import re

def index(text):
    '''
    Gets the index of a string after a colon
    This is important because most fields contain information
    delimited by a colon    
    '''
    for dex in range(0,len(text)):
        count = text[dex]        
        if (count == ":"):
            return (dex+2)

def format_text(n):
    '''
    Takes a string as input and splits the
    string into a list. The list items are then sent to
    capital_case where they are capitalized individually
    '''
    new_string = re.split(' ',n)
    for x in new_string:
        capital_case(x)
        print(capital_case(x))
    
def capital_case(input_string):
    '''
    @return: Returns a new string in capital case
    '''
    index_length = len(input_string)
    new_string = input_string[0].upper() + input_string[1:index_length].lower()
    return (new_string)

def upper_case(input_string):
    '''
    @return: Returns a new string in upper case
    '''
    new_string = input_string.upper()
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

        
## Open files for reading and file for writing
file_open = open("input1.txt","r")
##file_write = open("newfile.txt","w")

## Read lines of file
entered_list = file_open.readlines()


access_code = entered_list[1]
first_name = entered_list[2]
middle_name = entered_list[3]
last_name = entered_list[4]
other_name = entered_list[5]
ssn_dob = entered_list[6]
gender = entered_list[7]
prev_eval = entered_list[8]
prev_ref = entered_list[9]
being_sent = entered_list[10]
address = entered_list[13]
apt = entered_list[14]
city = entered_list[15]
state = entered_list[16]
zip_code = entered_list[17]
country_primary_email = entered_list[18]
secondary_email = entered_list[19]
phone = entered_list[20]
phone2 = entered_list[21]

sample_string = "this is a SAMPLE string to test the pRoGrAm"
second_sample_string = "The quick brown fox jumps over the lazy dog"
sample_number = 1815276125


print(access_code[index(access_code):])
print(capital_case(first_name[index(first_name):]) + capital_case(middle_name[index(middle_name):]) + upper_case(last_name[index(last_name):]) )
print(other_name[index(other_name):])
print(gender[index(gender):] + "\n")
print(prev_eval[index(prev_eval):])
print(being_sent[index(being_sent):] + "\n")
print(address[index(address):] + apt[index(apt):] + city[index(city):] + state[index(state):]+ zip_code[index(zip_code):])

##file_write.writelines(access_code[index(access_code):])
##file_write.writelines(capital_case(first_name[index(first_name):]) + capital_case(middle_name[index(middle_name):]) + upper_case(last_name[index(last_name):]) )
##file_write.writelines(other_name[index(other_name):])
##file_write.writelines(gender[index(gender):] + "\n")
##file_write.writelines(prev_eval[index(prev_eval):])
##file_write.writelines(being_sent[index(being_sent):] + "\n")
##file_write.write(address[index(address):] + apt[index(apt):] + city[index(city):] + state[index(state):] + zip_code[index(zip_code):])


## Close both opened files
file_open.close()
##file_write.close()
