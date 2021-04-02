###################################################

# 1 
# Write a function to print "hello_USERNAME!" USERNAME 
# is the input of the function. 
# The first line of the code has been defined as below.

# def hello_name(user_name):

def hello_name(user_name):
    """Display a greeting to the user."""
    print("hello_" + user_name.title() + "!")

hello_name("kevin")

###################################################

 #2

odd_numbers=list(range(1,101,2))
print(odd_numbers)

###################################################

# 3 

def max_num_in_list(a_list):
    """Returns the Max number in a list"""
    print("\nThe highest number in this list is " + str(max(a_list)) + "!")

max_num_in_list(list(range(1,101)))

###################################################

# 4

# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

#    def is_leap_year(a_year):

def is_leap_year(a_year):
    """Tells whether or not a year falls in a leap year"""
    if a_year % 4 == 0 and a_year % 100 != 0:
        print("True") 
    elif a_year % 4 == 0 and a_year % 100 == 0 and a_year % 400 == 0:
        print("True")
    else:
        print("False")

is_leap_year(2021)

###################################################

# 5

def is_consecutive(a_list):
    """Lets user know if list has all consecutive numbers or not"""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

list_b=[3,4,5,6,7,8,9,]
list_c=[3,4,6,7,8,8,9,10]
print(is_consecutive(list_b))
print(is_consecutive(list_c))

###################################################