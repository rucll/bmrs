# exp: "IF IF a(x) THEN True ELSE False THEN IF b(x) THEN c(x) ELSE d(x) ELSE c(P(x))"
# Usage:
# node.children[0~2] = condition node, then node, else node {node obj}
# node.value = string of condition                          { P(x), S(x), }
# node.name = type of node (Who Am I)                       { 'root', 'then', 'else', 'condition' }

#      01234
# s = 'xecdb'

# IF 
#   IF a(x) 
#   THEN False 
#   ELSE True 
# THEN 
#   IF b(x) 
#   THEN c(P(P(x)))
#   ELSE a(P(x))
# ELSE 
#   d(P(x))
# exp = "IF IF a(x) THEN False ELSE True THEN IF b(x) THEN c(P(P(x))) ELSE a(P(x)) ELSE d(P(x))"
# print( 'Final result is:', evl_file(exp, s, 4) )

# TODO: 
#   mod parse s.t. it uses fun for {T,F}
#   evl evls everything as a fun
#   function that updates dic(fun)

import re
from bmrs import bmrs
exp = "IF IF a(x) THEN False ELSE True THEN IF b(x) THEN b(P(P(x))) ELSE a(P(x)) ELSE a(P(x))"
sentence = "xacdb"
x = 1

O = bmrs(exp, sentence, x)
f_names = ['a',                 'b',                'c']
fs      = [lambda x : x =='a',  lambda x : x =='b', lambda x : x =='c']

O.add_to_dic(f_names, fs)
print(O.evl_exp())
