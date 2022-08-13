from bmrs import *

class Transduction(bmrs):
   """A class for defining the semantics of BMRS systems of equations as string to string transductions"""

   def __init__(self,sigma,gamma) -> True:
       """Initialize an empty (describing the empty function) BMRS transduction.
          sigma is input alphabet, gamma is output alphabet
          s in sigma will be assigned symbol s_i
          g in gamma will be assigned symbol g_o
       """
       bmrs.__init__(self)


       for s in sigma:
           self.add_pair(s+"_i",s)

       for g in gamma:
           self.add_to_dic(g+"_o", 'False')


    def transduce():
        pass

    def new_exp():
        # Note: this is just going to be add_to_dic() with a failsafe so you don't overwrite the input functions
        pass
