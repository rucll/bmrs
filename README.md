# bmrs.py

An implementation of BMRS written in Python with a simple graphical interface.

## Running

Requires Python 3.x and [PySimpleGUI](https://www.pysimplegui.org/en/latest/).

To install PySimpleGUI, simply run
```
pip install pysimplegui
```
(or `pip3 install pysimplegui`).

With PySimpleGUI installed, simply clone this repository and in the main folder run
```
python3 main.py
```

## UI

### Syntax

`bmrs.py` runs a BMRS transducer a la [Bhaskar et al. 2020](http://adamjardine.net/files/bhaskaretalBMRSms.pdf) and [Chandlee and Jardine 2021](http://adamjardine.net/files/chandleejardineBMRSms.pdf).
For full description of the BMRS syntax, see those papers. 

The syntax here uses the basic BMRS syntax, as in the following example.
```
a_o = IF b_o(x) THEN False ELSE a_i(x)
b_o = IF b_i(x) THEN True ELSE if a_i(x) THEN b_o(P(x)) ELSE False
c_o = c_o(x)
```
Note that `a_i(x)` indicates an *input* `a`, whereas `a_o(x)` indicates an *output* `a`.

### Alphabet Set Up

Optionally specify the input and output alphabet from text files. 
Examples are given in `in.txt` and `out.txt`. 
Leave blank and click `Submit` to proceed with the default alphabets (currently both `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, `i`, `j`, `k`, `l`, `m`). 

### Menu

After the alphabets have been set up, `bmrs.py` loads an empty BMRS transducer. From this menu, you can:

* `AddExpressionFromText` -
Add a new definition directly from the UI.
* `AddExpressionFromFile` - 
Add a series of definisions from a text file. For formatting, see the example in `exp.txt`.
* `Transduce` - 
Transduce a string with the currently loaded set of definitions.
* `Cancel` - 
Quit.


## To be added

* Features
* Copy set (for epenthesis)
* Saving, loading, and viewing of transducers
* Other UI sugar
* ... (suggestions welcome!)

# Contributors

* [Adam Jardine](https://www.adamjardine.net) (Faculty advisor)
* [Daniel Jin](https://github.com/v0lv0) (main programmer)
