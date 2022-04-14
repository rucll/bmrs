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
#   Fix add_to_dic

from bmrs import bmrs

x = 1
sentence = "baaaa"
O = bmrs(sentence)

exp = "IF IF e2(x) THEN False ELSE True THEN IF b(x) THEN b(P(P(x))) ELSE a(P(x)) ELSE b(P(x))"
O.add_to_dic("e1", exp )

exp = "IF a(x) THEN False ELSE True"
O.add_to_dic("e2", exp )

print(O.evl("e1", x, sentence))