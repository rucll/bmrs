from bmrs import bmrs

# TODO: remove sentence from bmrs
# TODO: fix the following example, idea- index is off?
# TODO: fix visual issue.
# TODO: remove edge check from \lambda to evl


# notes: 
# bmrs stores dic
# Expression 
O = bmrs()
# O.add_to_dic("d", lambda x: O.word[x]=='d')
# print(O.dic['d'].expression('d') )
O.add_to_dic("b_o","IF b(x) THEN True ELSE b_o(P(x))")

      # 012345
word = "aabaaa"
print(O.evl("b_o", 1, word))
