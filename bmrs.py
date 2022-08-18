from ast import Expression
import re
import csv
import copy
from types import LambdaType
from numpy import isin
from treeplotter.tree import Node
from treeplotter.plotter import create_tree_diagram
from parse import build_tree, parse_exp
from typing import Dict, List


class Expression: 
    def __init__(self) -> None:
        self.is_lambda = True
        self.expression = None
    def __init__(self, exp) -> None:
        if isinstance(exp, LambdaType) :
            self.is_lambda = True
            self.expression = exp
        elif isinstance(exp, str):
            self.is_lambda = False
            self.expression = build_tree(exp)
    def add(self, exp) -> None:
        if isinstance(exp, LambdaType) :
            self.is_lambda = True
            self.expression = exp
        elif isinstance(exp, str):
            self.is_lambda = False
            self.expression = build_tree(exp)

    # solves f1(f2(x))
    # in helper, fun = [f1, f2, x]
    def evl_fun_helper(self, dic, fun, x:int):
        if x<0:
            raise "Index out of bound"
        # base case when there's only x left
        if len(fun) == 1: 
            if fun[0] == "x":
                return x
            elif fun[0] in dic:
                f = dic[fun[0]]
                return f.evl_exp(dic, x)
            else: 
                raise LookupError("invalid expression")
        
        # apply f to right
        f_name = fun[0]
        if f_name not in dic: 
            raise LookupError("expression "+ f_name +" is not found" )
        f = dic[f_name]
        
        if f.is_lambda :
            return f.expression( self.evl_fun_helper(dic, fun[1:], x) )
        else:
            # when funciton is a tree
            return f.evl_exp(dic, self.evl_fun_helper(dic, fun[1:], x))
    def evl_fun(self, dic, fun,  x:int):
        fun = re.split("\(|\)", fun)
        while "" in fun:
            fun.remove("")
        res = self.evl_fun_helper(dic, fun, x)
        return res

    # evl if f1(x) then True else f2(f3(x))
    def evl_exp_helper(self, dic, root: Node, x:int):
        if x<0:
            raise "Index out of bound"
        # Base case (leaf node), the expression will be the condition needs to be evled
        if len(root.children) <= 0:
            return self.evl_fun(dic, root.value, x)
        
        # condition can be complicated here
        # it could be an expresssion that returns a bool.
        if self.evl_exp_helper(dic, root.children[0], x):
            return self.evl_exp_helper(dic, root.children[1], x)
        else:
            return self.evl_exp_helper(dic, root.children[2], x)
    def evl_exp(self, dic, x:int):
        if self.is_lambda:
            try:
                r = self.expression(x)
                # print( "please", x, r)
                return r
            except:
                return False
        else:
            try:
                return self.evl_exp_helper(dic, self.expression, x)
            except:
                return False

class bmrs:
    def __init__(self) -> None:
        # dic: dictionary from name to function
        self.word = ""
        # TODO: self.alphabet = alpha
        dic: Dict[str,  Expression] = {
            'True':     Expression( lambda x: True ),
            'False':    Expression( lambda x: False ),
            'P':        Expression( lambda x: x-1 ),
            'S':        Expression( lambda x: x+1 )
        }
        self.dic = dic

    def add_pair(self, name, fun):
        self.dic[copy.deepcopy(name)] = Expression( lambda x, y=fun: y ==  self.word[x] )


    def readCSV(self, path):
        with open(path, encoding='utf-8') as f:
            pairs = csv.reader( f )
            for pair in pairs:
                self.dic[copy.deepcopy(str(pair[0]))] = Expression( lambda x, y=pair[1]: y ==  self.word[x] )


    def add_to_dic (self, f_names, fs):
        self.dic[f_names] = Expression(fs)
        
    def evl(self, exp, x, word):
        if exp not in self.dic:
            raise LookupError("Expression '"+str(exp)+"' not found")
        self.word = word
        if x<0 or x>=len(word):
            raise IndexError("Index out of bound")
        try:
            return self.dic[exp].evl_exp(self.dic, x)
        except:
            return False
