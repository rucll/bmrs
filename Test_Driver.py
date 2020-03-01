from BMRS_parser import BMRS_parser

while True:

    print("Input a BMRS expression, or type \"D\" and hit Enter to run a demo: ")
    input_expression = input()
    parser = BMRS_parser()
    
    if input_expression == 'D':
        print("===========================")
        input_expression = "b(p(x))"
        print("Input: \'" + input_expression + "\'")
        print("Output: " + str(parser.parse(input_expression)))
        print("===========================")
        input_expression = "if (b(p(x)) then T"
        print("Input: \'" + input_expression + "\'")
        print("Output: " + str(parser.parse(input_expression)))
        print("===========================")
        input_expression = "if (b(p(x)) then T else F"
        print("Input: \'" + input_expression + "\'")
        print("Output: " + str(parser.parse(input_expression)))
        print("===========================")
        input_expression = "if a(p(x)) then (b(p(x)) else c(p(x))"
        print("Input: \'" + input_expression + "\'")
        print("Output: " + str(parser.parse(input_expression)))
        print("===========================")
        input_expression = "if a(p(p(p(x)))) then a(x) else F"
        print("Input: \'" + input_expression + "\'")
        print("Output: " + str(parser.parse(input_expression)))
        print("===========================")
        input_expression = "if b(p(x)) then T else if c(x) then F else a(x)"
        print("Input: \'" + input_expression + "\'")
        print("Output: " + str(parser.parse(input_expression)))
        print("===========================")
        input_expression = "if a(p(x)) then T else if b(p(x)) then F else if c(p(x)) then T else F"
        print("Input: \'" + input_expression + "\'")
        print("Output: " + str(parser.parse(input_expression)))
        print("===========================")
        input_expression = "if if b(p(x)) then a(p(p(x))) else F then T else F"
        print("Input: \'" + input_expression + "\'")
        print("Output: " + str(parser.parse(input_expression)))
        print("===========================")
        input_expression = "if if if b(p(x)) then T else F then T else F then F else F"
        print("Input: \'" + input_expression + "\'")
        print("Output: " + str(parser.parse(input_expression)))
        print("===========================")
        input_expression = "if a(p(x)) then if (b(p(x)) then T else c(p(p(x)) else T"
        print("Input: \'" + input_expression + "\'")
        print("Output: " + str(parser.parse(input_expression)))
        print("===========================")
        input_expression = "if if a(p(x)) then if b(p(x)) then if c(p(x)) then C else F else d(p(x)) else F then T else e(p(x))"
        print("Input: \'" + input_expression + "\'")
        print("Output: " + str(parser.parse(input_expression)))
        print("===========================")
        print()

    else:
        print("===========================")
        print("Input: \'" + input_expression + "\'")
        print("Output: " + str(parser.parse(input_expression)))
        print("===========================")
        print()
