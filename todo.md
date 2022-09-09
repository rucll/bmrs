# To do list:

* Fix S(x) wrapping around problem
* Make whitespace insensitive. For example, inputting the following text will return an error:
```
a_o = if b_o(x) then False else a_i(x)
b_o = if b_i(x) then True else
      if a_i(x) then b_o(P(x)) else
      False
```
* Do a syntax check so it doesn't hang on ill-formed expressions


# Done

* IF/THEN parsing needs to be case insensitive
...
