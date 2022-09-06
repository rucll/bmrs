import PySimpleGUI as sg
import sys
import copy
from src.transduction import Transducer

alphabet_setup_layout = [
    [ sg.Text('Please enter input alphabet(leave empty to read from in.txt): '),  sg.InputText()],
    [ sg.Text('Please enter output alphabet(leave empty to read from out.txt): '), sg.InputText()],
    [ sg.Submit(), sg.Cancel()]
]
menu_layout = [
    [ sg.Button('AddExpressionFromText')],
    [ sg.Button('AddExpressionsFromFile')],
    [ sg.Button('TransduceWord')],
    [ sg.Cancel()],
]

# GET ALPHABET
window = sg.Window('Alphabet Set Up', alphabet_setup_layout)
event, values = window.read()
if event == 'Cancel':
    sys.exit()
# get in alph
if( values[0] == ''):
    f = open( 'in.txt', 'r')
    sigma = f.read().split()
    f.close()
else:
    sigma = values[0].split()
# get out alph
if( values[1] == ''):
    f = open( 'out.txt', 'r')
    gamma = f.read().split()
    f.close()
else:
    gamma = values[0].split()
window.close()


# START MENU
t = Transducer(sigma,gamma)
menu_window = sg.Window('Menu', menu_layout)
while True:
    menu_event, values = menu_window.read()
    if menu_event == sg.WINDOW_CLOSED or menu_event == 'Cancel':
        menu_window.close()
        sys.exit()
    elif menu_event == 'AddExpressionFromText':
        addOneExpression_layout = [
            [ sg.Text('Name: '), sg.InputText()],
            [ sg.Text('Expression: '), sg.InputText()],
            [ sg.Submit(), sg.Cancel()]
        ]
        add_one_exp_window = sg.Window('Word', addOneExpression_layout)
        event, values = add_one_exp_window.read()
        name = values[0]
        exp = values[1]
        t.new_exp(name, exp)
        add_one_exp_window.close()
    elif menu_event == 'AddExpressionsFromFile':
        addExpressionFromFile_layout = [
            [ sg.Text('File Path(leave empty to read from exp.txt): '), sg.InputText()],
            [ sg.Submit(), sg.Cancel()]
        ]
        add_exp_file_window = sg.Window('Word', addExpressionFromFile_layout)
        event, values = add_exp_file_window.read()
        file_path = values[0]
        if file_path == '':
            file_path = 'exp.txt'
        f = open( file_path , 'r')
        lines = f.readlines()
        for line in lines:
            ne = line.split('=')
            t.new_exp(ne[0].strip(), ne[1].strip())

        add_exp_file_window.close()

    elif menu_event == 'TransduceWord':
        word_input_layout = [
            [ sg.Text('Enter the word: '), sg.InputText()],
            [ sg.Submit(), sg.Cancel()]
        ]
        transduce_window = sg.Window('Word', word_input_layout)
        event, values = transduce_window.read()
        if event == 'Cancel' or event == sg.WINDOW_CLOSED:
            transduce_window.close()

        if event == 'Submit':
            transduce_window.close()
            word = values[0]
            # in table 
            in_heading = ['Original'] + copy.deepcopy(t.in_keys)
            in_vals = []
            for i in range(0,len(word)):
                s = [str(i)]
                for j in t.in_keys:
                    s.append(str(t.evl(j,i,word)))
                in_vals.append(s)
            in_value_layout = [
                [ sg.Text( str(' Original word: ' + word ) ) ],
                [ sg.Text( ' Original word truth-table: ') ],
                [ sg.Table(headings = in_heading,values = in_vals)]
            ]
            # out table
            out_heading = ['Transduced'] + copy.deepcopy(t.out_keys)
            out_vals = []
            for i in range(0,len(word)):
                s = [str(i)]
                for j in t.out_keys:
                        s.append(str(t.evl(j,i,word)))
                out_vals.append(s)
            out_value_layout = [
                [ 
                    sg.Text( str(' Original word: ' + word ) ) , 
                    sg.Text( str(' Transduced result: ' + t.transduce(word) ) ) 
                ],
                [ 
                    sg.Table(headings = in_heading,values = in_vals),
                    sg.Table(headings = out_heading, values = out_vals)
                ]
            ]
            out_value_window = sg.Window('Outputs', out_value_layout)
            event, values = out_value_window.read()
        