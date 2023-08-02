

# number formatting
long_number = 0.22734823648726348724
print(f"Number is {long_number:%}") # prints 22.73482364%
print(f"Number is {long_number:.2%}") # prints 0.23

# alignment formatting for numbers
for number in range(5, 15):
    print(f"The number is {number:4}") # right align the output values (int) for clearer formatting 
    print(f"The number is {number:_4}") # right align with _ rather than ' ' space 
# alignment formatting for strings
greet = "hello"
print(f"{greet:>4}") # right align the output values (str) for clearer formatting
print(f"{greet:_>4}") # right align with _ rather than ' ' space 


# datetime
today = datetime.datetime.now()
print(f"Todays date is: {today:%D}")
print(f"Todays is a: {today:%A}")
print(f"The time is: {today:%T}")
print(f"The month is: {today:%B}")
print(f"The year is: {today:%Y}")


