from transduction import Transduction

if __name__ == "__main__":
      sigma = {"a","b","c"}
      gamma = {"a","b","c"}

      t = Transduction(sigma,gamma)

      word = "abaaacaaabaa"

      print("string "+word)

      #Truth value grid for inputs
      s = "index\t"
      for j in t.in_keys:
            s+=j+"\t"
      print(s)

      for i in range(0,len(word)):
            s = str(i)+"\t"

            for j in t.in_keys:
                  s += str(t.evl(j,i,word))+"\t"
            print(s)


      # a -> b / b __ (noniterative)
      t.new_exp("a_o","IF b_o(x) THEN False ELSE a_i(x)")
      t.new_exp("b_o","IF c_i(x) THEN FALSE ELSE IF b_i(x) THEN True ELSE b_i(P(x))")
      t.new_exp("c_o","c_i(x)")

      # a -> b / b __ (iterative)
      t.new_exp("a_o","IF b_o(x) THEN False ELSE a_i(x)")
      t.new_exp("b_o","IF c_i(x) THEN FALSE ELSE IF b_i(x) THEN True ELSE b_o(P(x))")
      t.new_exp("c_o","c_i(x)")

      # a -> b / __ b(iterative)
      t.new_exp("a_o","IF b_o(x) THEN False ELSE a_i(x)")
      t.new_exp("b_o","IF c_i(x) THEN FALSE ELSE IF b_i(x) THEN True ELSE b_o(S(x))")
      t.new_exp("c_o","c_i(x)")

      print("transducing...")

      #Truth value grid for outputs
      s = "index\t"
      for j in t.out_keys:
            s+=j+"\t"
      print(s)

      for i in range(0,len(word)):
            s = str(i)+"\t"

            for j in t.out_keys:
                  s += str(t.evl(j,i,word))+"\t"
            print(s)

      print(t.transduce(word))
