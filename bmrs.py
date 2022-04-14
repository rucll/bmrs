import re
from types import LambdaType
from treeplotter.plotter import create_tree_diagram
from parse import build_tree, parse_exp

class bmrs:
    # structure: "xecdb"
    structure = ""
    # dic: dictionary from name to function
    dic = {}

    def __init__(self,  structure: str):
        self.structure = structure
        self.dic = {
            'True': lambda x: True, 
            'False': lambda x: False,
            'P': lambda x: False if (x<0 or x>len(structure)) else x-1,
            'S': lambda x: x+1,
            'a': lambda x: self.structure[x] == 'a',
            'b': lambda x: self.structure[x] == 'b',
            'c': lambda x: self.structure[x] == 'c'
        }

    class Exp_fun:
        # expression: IF fun(x) THEN fun(x) ELSE fun(x)
        expression = ""
        # tree: built from expression
        tree = None

        def __init__(self, expression: str):
            self.tree = build_tree(expression)

        def rec_par_fun(self, fun, x, dic):
            # base case when there's only x left
            if len(fun) == 1: 
                if fun[0] == "x":
                    return x
                elif fun[0] in dic:
                    f = dic[fun[0]]
                    if isinstance(f, LambdaType):
                        t = f(x)
                        return t
                    else:
                        # print("_______",f(x))
                        t = f.evl_exp(x)
                        return t
                else:
                    raise "invalid expression"
            
            # apply f to right
            f_name = fun[0]
            if f_name not in dic: 
                raise "expression is not found"
            f = dic[f_name]
            if isinstance(f, LambdaType):
                return f(self.rec_par_fun(fun[1:], x, dic))
            else:
                return f.evl_exp(x, dic)

        def parse_fun(self, fun, x, dic):
            fun = re.split("\(|\)", fun)
            while "" in fun:
                fun.remove("")
            res = self.rec_par_fun(fun, x, dic)
            print("Function:",fun , " at ", x ," is evaluated to", res)
            return res
        
        def evl_exp_helper(self, root, x:int, dic):
            # Base case (leaf node)
            if len(root.children) <= 0:
                return self.parse_fun(root.value, x, dic)
            # condition can be complicated here
            if self.evl_exp_helper( root.children[0], x, dic):
                return self.evl_exp_helper( root.children[1], x, dic)
            else:
                return self.evl_exp_helper( root.children[2], x, dic)

        def evl_exp(self, x:int, dic):
            return self.evl_exp_helper( self.tree, x ,dic)

    def add_to_dic (self, f_names, fs):
        if isinstance(fs, str):
            self.dic[f_names] = self.Exp_fun(fs)
        elif isinstance(fs, LambdaType):
            self.dic[f_names] = fs
        else:
            raise("invaid function")
    
    def evl(self, f_name, x, structure):
        if f_name not in self.dic:
            raise "cannot find function to evaluate"
        self.structure = structure
        return self.dic[f_name].evl_exp(x, self.dic)
    