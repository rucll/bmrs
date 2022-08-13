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
