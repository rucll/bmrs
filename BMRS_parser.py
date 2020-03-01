"""
This separates input expressions into a list of lists.
It does this by copying the input expression as a list, then replacing subexpressions with sublists while removing all the "if/then/else"s.

It uses the following algorithm:
    1. Find index i of the rightmost "if" in the list
    2. Make a sublist of the elements following "if", "then", and "else" (positions i+1, i+3, and i+5)
    3. Replace i through i+5 with just this list of elements
    4. Repeat until there are no more "if"s
    
By finding the rightmost "if" in the expression, the algorithm ensures that it finds the corresponding "then" and "else" for the next innermost sublist.
"""
class BMRS_parser:

    # The main "parse" method: takes a string and returns a list
    def parse (self, inputExpression : str) -> list:
        
        # The list to be returned starts off as a copy of the input string
        resultList = inputExpression.split()

        # Start by finding the index of the rightmost "if" -> i
        # While you can find an "if", run the algorithm
        ## [Replace while condition with next two lines for v. < 3.8]
        # i = self.findLastIf(resultList)
        # while i != -1:
        while i := self.findLastIf(resultList)) != -1:
            
            # The following 2 if statements attempts to catch missing "then/else" clauses
            if len(resultList) < 3 or resultList[i+2] != "then":
                return "Parse error at index " + str(i) + ": The \"if\" statement missing a \"then\" clause."
            if len(resultList) < 5 or resultList[i+4] != "else":
                return "Parse error at index " + str(i) + ": \"if\" statement missing an \"else\" clause."
            
            innerList = [0]*3 # Initialize a sublist. Now we want to add the relevant bits:
            innerList[0] = resultList[i+1] # Add the T|F|_(p(x)) after "if"
            innerList[1] = resultList[i+3] # Add the T|F|_(p(x)) after "then"
            innerList[2] = resultList[i+5] # Add the T|F|_(p(x)) after "else"
            # The sublist will not contain "if" because we are already working with the rightmost "if"
            
            del resultList[i+1:i+6] # Remove this expression from the list

            if i == 0: # If this was the last "if", then the sublist is the final list
                return innerList
            else: # Replace the expression with the sublist
                resultList[i] = innerList 

            # { Uncomment below for v. < 3.8 }
            # i = self.findLastIf(resultList) 

        return resultList # In case the input expression has no "if" to begin with (i.e. is just T|F|_(p(x)))

    # Support method: takes a list and returns the position of the rightmost "if"
    def findLastIf (self, inputList : list) -> int:
        index = 0
        posLastIf = -1
        for element in inputList:
            if element == "if":
                posLastIf = index
            index+=1
        return posLastIf
