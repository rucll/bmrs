from bmrs import bmrs

# TODO: remove sentence from bmrs
# TODO: fix the following example, idea- index is off?
# TODO: fix visual issue.
# TODO: remove edge check from \lambda to evl


# notes: 
# bmrs stores dic
# Expression 
if __name__ == "__main__":
    O = bmrs()
    O.add_to_dic("a_o","IF b_o(x) THEN False ELSE a(x)")
    O.add_to_dic("b_o","IF b(x) THEN True ELSE b_o(P(x))")
    
          # 012345
    word = "aabaaa" # -> aabbbb
    print(O.evl("b_o", 5, word))
    print(O.evl("a_o", 5, word))
    print(O.evl("b_o", 1, word)) # Should be false
    print(O.evl("a_o", 1, word)) # Should be true
