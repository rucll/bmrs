from ast import Expression
import copy
import re
from treeplotter.tree import Node, Tree
from treeplotter.plotter import create_tree_diagram
from parse import build_tree, parse_exp

class bmrs:
    # expression: IF fun(x) THEN fun(x) ELSE fun(x)
    expression = ""
    # sentence: "xecdb"
    sentence = ""
    # x: starting pos 
    x = 0
    # dic: dictionary from name to function
    dic = {}
    # tree: built from expression
    tree = None

    def __init__(self, expression: str, sentence: str, x: int):
        self.expression = expression
        self.sentence = sentence
        self.x = x
        self.dic = {
            'True': lambda x: True, 
            'False': lambda x: False,
            'P': lambda x: x-1,
            'S': lambda x: x+1
        }
        self.tree = build_tree(expression)

    
    def add_to_dic (self, f_names, fs):
        for name,f in zip(f_names, fs):
            if name == "x" or name == "S" or name == "P" or name == "True" or name == "False":
                raise "x, P, S, True and False are reserved"
            self.dic[name] = f
    

    def rec_par_fun(self, fun):
        # base case when there's only x left
        print(fun[0])
        if len(fun) == 1: 
            if fun[0] == "x":
                return self.x
            elif fun[0] in self.dic:
                return self.dic[fun[0]](self.x)
            else:
                raise "expression should end with variable x"
        
        # apply f to right
        f_name = fun[0]
        if f_name not in self.dic: 
            raise "expression is not found"
        return self.dic[f_name]( self.rec_par_fun(fun[1:]) )


    def parse_fun(self, fun):
        fun = re.split("\(|\)", fun)
        while "" in fun:
            fun.remove("")
        return self.rec_par_fun(fun)


    def evl_exp_helper(self, root):
        # Base case (leaf node)
        if len(root.children) <= 0:
            return self.parse_fun(root.value)
        
        # condition can be complicated here
        if self.evl_exp_helper( root.children[0]):
            return self.evl_exp_helper( root.children[1])
        else:
            return self.evl_exp_helper( root.children[2])

    def evl_exp(self):
        return self.evl_exp_helper( self.tree )


