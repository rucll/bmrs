from transduction import Transduction

if __name__ == "__main__":
      sigma = {"a","b","c"}
      gamma = {"a","b","c"}

      t = Transduction(sigma,gamma)

      word = "acba"

      print(t.evl("a_i",0,word))
      print(t.evl("a_i",1,word))
      print(t.evl("a_i",2,word))
      print(t.evl("a_i",3,word))
      print(t.evl("b_i",0,word))
      print(t.evl("b_i",1,word))
      print(t.evl("b_i",2,word))
      print(t.evl("b_i",3,word))

      print(t.evl("b_o",0,word))
      print(t.evl("b_o",1,word))
      print(t.evl("b_o",2,word))
      print(t.evl("b_o",3,word))


      t.new_exp("a_o","IF b_o(x) THEN False ELSE a_i(x)")
      t.new_exp("b_o","IF c_i(x) THEN FALSE ELSE IF b_i(x) THEN True ELSE b_i(P(x))")
      t.new_exp("c_o","c_i(x)")
      t.new_exp("a_i","c_i(x)")
