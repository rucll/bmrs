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
sentence = "aabaaa"
O = bmrs(sentence)

exp = "IF IF e2(x) THEN False ELSE True THEN IF b(x) THEN b(P(P(x))) ELSE a(P(x)) ELSE b(P(x))"
O.add_to_dic("e1", exp )

exp = "IF a(x) THEN False ELSE True"
O.add_to_dic("e2", exp )


# Testing from Adam

# There are very often rules of the form a -> b / b _ (iterative), meaning that baaaa would be mapped to bbbbb
# In such a case, we would want to define an output b using the following expression

O.add_to_dic("b_o","IF b(x) THEN True ELSE b_o(p(x))")

print(O.evl("b_o", 0, sentence))

# Rule: b -> c / c X _ (X can be any string of segments)

# follows_c = "IF c(p(x)) THEN True ELSE follows_c(p(x))"
# a_o = "a(x)"
# b_o = "if follows_c(x) THEN False ELSE b(x)"
# c_o = "if c(x) THEN True ELSE IF b(x) THEN follows_c(x) ELSE False"

# ldrule = bmrs("acaaba")
# ldrule.add_to_dic("follows_c",follows_c)
# ldrule.add_to_dic("a_o",a_o)
# ldrule.add_to_dic("b_o",b_o)
# ldrule.add_to_dic("c_o",c_o)

# print(ldrule.evl("follows_c",0,"acaaba")) # < - This throws an "expression is not found" error
