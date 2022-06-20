from bmrs import bmrs

# TODO: remove sentence from 
# TODO: fix the following example, idea- index is off?
# TODO: fix visual issue.
# TODO: remove edge check from \lambda to evl
# TODO: add to dic

sentence = "aabaaa"
O = bmrs()
O.add_to_dic("b_o","IF b(x) THEN True ELSE b_o(p(x))")
print(O.evl("b_o", 5, sentence))
