# import pyfiglet module
import pyfiglet

# change font color
class ANSI():
    def color_text(code):
        return "\33[{code}m".format(code=code)

# ask user for input then save it
input_str = input("What is your input string? ")
output_str = ""

# check every character
for i in range(len(input_str)):
# if *, change to a
    if input_str[i] == "*":
        output_str += "a"
# if &, change to e
    elif input_str[i] == "&":
        output_str += "e"
# if #, change to i
    elif input_str[i] == "#":
        output_str += "i"
# if +, change to o
    elif input_str[i] == "+":
        output_str += "o"
# if !, change to u
    elif input_str[i] == "!":
        output_str += "u"
    else:
        output_str += input_str[i]









