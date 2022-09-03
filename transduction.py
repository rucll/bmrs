from bmrs import *

class Transducer(bmrs):
   """A class for defining the semantics of BMRS systems of equations as string to string transductions"""

   def __init__(self,sigma,gamma) -> True:
      """Initialize an empty (describing the empty function) BMRS transduction.
         sigma is input alphabet, gamma is output alphabet
         s in sigma will be assigned symbol s_i
         g in gamma will be assigned symbol g_o
      """

      bmrs.__init__(self)
      self.in_alph = sigma
      self.out_alph = gamma

      # Lists that keep track of which function names in dictionary correspond
      # to input functions and which go to output functions
      self.in_keys = []
      self.out_keys = []

      for s in sigma:
         self.in_keys.append(s+"_i")
         self.add_pair(s+"_i",s)

      for g in gamma:
         self.out_keys.append(g+"_o")
         self.add_to_dic(g+"_o", 'False')


   def transduce(self,s):
      """
      Transduce string s interpreting bmrs as an order-preserving transduction.
      Essentially follows the rules in Bhaskar et al., 2021, which ultimately is derived
      from those in Engelfriet and Hoogeboom 2001
      """
      indices = range(0,len(s))

      output = ""

      for i in indices:

         trues = []

         for k in self.out_keys:
            if self.evl(k,i,s):
               trues.append(k.strip("_o"))

         # Only output if there *is exactly one* output function which i satisfies
         if len(trues) == 1:
            output += trues[0]
         # ...otherwise output empty string
         else:
            output += ""

      return output


   def new_exp(self,f_name,f):
      """
      Add a new expression to the BMRS dictionary.
      Note: This is just add_to_dic() with a failsafe so user doesn't overwrite the input functions
      """

      if f_name not in self.in_keys:
         self.add_to_dic(f_name,f)
      else:
         raise LookupError("Cannot rewrite input alphabet functions")


   # def __str__(self)
