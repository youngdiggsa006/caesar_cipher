# Amaris Young-Diggs
# Vigenere Cipher: Decoding and Encoding Project


# tkinter is the standard GUI library in python. Provides a set of tools and functions
# to create windows, dialogs, buttons, labels, etc. base64 is a module in Python's standard
# library that provides functions for encoding and decoding binary data using base64 encoding
from tkinter import *
import base64

root = Tk()  # creates a window for the program
root.geometry('500x300')  # sets the width & height to a set amt of pixels (wxh)
root.resizable(0, 0)  # height and width not resizable
root.title("Message Encoder and Decoder")  # set title of window

# Label() widget use to display one or more than one line of text that users aren't able to modify
Label(root, text='ENCODE | DECODE', font='tahoma 20 bold').pack() # this line creates a label that displays "ENCODE DECODE"
Label(root, text='Caesar Cipher', font='tahoma 20 bold').pack(side=BOTTOM) # this line creates a label that displays "Ceaser Cipher"

# Define vars
Text = StringVar()  # stores the message to encode and decode
private_key = StringVar()  # stores the private key used to encode and decode
mode = StringVar()  # used to select whether it's for decoding or encoding
Result = StringVar()  # stores the results of the decode/encode operation


# Function to encode
# this function takes a key and a message, and it encodes the message by adding
# characters from the key cyclically and then performing Base64 encoding on the result.
# takes the numeric representation of the message character and the corresponding key
# character, adds them together, and takes the result modulo 256 (keeps the result within
# the range of valid characters)
def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 52 + 65))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Function to decode
# function's purpose to reverse the encoding process and recover the original message
# takes an encoded message and a decryption key, then reverses the encoding process to
# recover the original message
def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c) + 52) % 52 + 65))
    return "".join(dec)


# Function to set mode
# this function is responsible for setting the mode of operation, which can be either
# encoding or decoding
def Mode():
    if mode.get() == 'e' or 'E':
        Result.set(Encode(private_key.get(), Text.get()))
    elif mode.get() == 'd' or 'D':
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')


# Function to exit window
def Exit():
    root.destroy()


# Function to reset window
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


# Labels and Buttons
Label(root, font='tahoma 12 bold', text='MESSAGE').place(x=60, y=60)
Entry(root, font='arial 10', textvariable=Text, bg='ghost white').place(x=290, y=60)

Label(root, font='tahoma 12 bold', text='KEY').place(x=60, y=90)
Entry(root, font='arial 10 bold', textvariable=private_key, bg='ghost white').place(x=290, y=90)

Label(root, font='tahoma 12 bold', text='MODE (e (enc), d (dec))').place(x=60, y=120)
Entry(root, font='arial 10', textvariable=mode, bg='ghost white').place(x=290, y=120)
Entry(root, font='arial 10 bold', textvariable=Result, bg='ghost white').place(x=290, y=150)

Button(root, font='tahoma 10 bold', text = 'RESULT', padx = 2, bg = 'LimeGreen', command = Mode).place(x=60, y=150)

Button(root, font='tahoma 10 bold', text = 'RESET', width = 6, command = Reset, bg = 'Yellow', padx = 2).place(x=185, y=200)

Button(root, font = 'tahoma 10 bold', text = 'EXIT', width = 6, command = Exit, bg = 'OrangeRed', padx = 2, pady=2).place(x=260, y=200)

root.mainloop()