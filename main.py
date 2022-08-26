# Main script for running UI

from bmrs import *
from transduction import *
from constants import *
import re

# Variables for keeping track of named objects created by user
systems: Dict[str,Transduction] = {} # BMRS transductions
alphas:  Dict[str,set] = {}          # alphabets
current = None                       # Name (string) of current transducer

# Helper functions
def parse_alpha(s):
    """Parse alphabet in form of string '{a, b, ..., x}'"""
    r = set(s)
    r.remove('}')
    r.remove('{')
    r.remove(',')
    r.remove(' ')
    return r


# UI functions
# Each of these is going to take a list "keywords" of strings as an argument
# Remember that the first keyword will always be the name of the function!

def new_trans(keywords):
    """Create a new transducer"""
    try:
        name  = keywords[1]
        sigma = parse_alpha(keywords[2])
        gamma = parse_alpha(keywords[3])
        systems["name"] = Transduction(sigma,gamma)
        return "Added new transduction '"+name+"', input alphabet "+str(sigma)+"; output alphabet "+str(gamma)

    except:
        return "Something went wrong!\nSyntax for newt is 'newt [name] [in alpha] [out alpha]', where each alphabet is of the form '{a, b, c, ..., z}'."

# To do
# trans(keywords) #transduce a string with current transducer
# listt(keywords) #list all transducers
# alpha           #create an alphabet


# Dictionary for keywords and functions here

func_map = {
    "newt" : new_trans,
    #"t"   : trans,
}


def parse_input(s):
    """Parse input string s"""
    # keywords = s.split(" ")
    keywords = re.findall(r"\{.+?\}|\w+",s)
    try:
        head = keywords[0]
        return func_map[head](keywords)
    except:
        return "Sorry, could not parse."



# Main

if __name__ == "__main__":
    print(opening)
    print(prompt+" ",end="")
    in_string = input()

    while in_string != quitstring:
        print(parse_input(in_string))

        print(prompt+" ",end="")
        in_string = input()
