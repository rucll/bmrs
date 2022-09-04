import PySimpleGUI as sg
import sys
from src.transduction import Transducer

layout = [
    [ sg.Text("Please enter file name for input alphabet: "),  sg.InputText()],
    [ sg.Text("Please enter file name for output alphabet: "), sg.InputText()],
    [ sg.Submit(), sg.Cancel()]
]

window = sg.Window("Alphabet Set Up", layout)
event, values = window.read()
if event == 'Cancel':
    sys.exit()
try:
    f = open( values[0], "r")
    sigma = f.read().split()
    f.close()
except:
    sys.exit('Input alphabet not found')

try:
    f = open( values[1], "r")
    gamma = f.read().split()
    f.close()
except:
    sys.exit('Output alphabet not found')

layout = [
    [ sg.Text("Enter the word: "), sg.InputText()],
    [ sg.Submit(), sg.Cancel()]
]
window = sg.Window("Set Up", layout)
event, values = window.read()

if event == 'Cancel':
    sys.exit()
word = values[0]


t = Transducer(sigma,gamma)

s = "index\t"
for j in t.in_keys:
    s+=j+"\t"
# print(s)

for i in range(0,len(word)):
    s = str(i)+"\t"

    for j in t.in_keys:
            s += str(t.evl(j,i,word))+"\t"
    # print(s)



