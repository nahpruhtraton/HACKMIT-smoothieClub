import sys
from flask import Flask, render_template, redirect, url_for, request
# from django.db import models
from tkinter import *
from webserver.login_window.login import login_api
sys.path.append('/webserver/login_window')

app = Flask(__name__)

@app.route('/')

def home():
    # main_account_screen()
    login_api()
    return 'Website content goes here. Wo'

# # Route for handling the login page logic
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)

def main_account_screen():
    
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("Account Login") # set the title of GUI window
 
    # create a Form label 
    Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
     
    # create Login Button 
    Button(text="Login", height="2", width="30").pack() 
    Label(text="").pack() 
     
    # create a register button
    Button(text="Register", height="2", width="30").pack()
     
    main_screen.mainloop() # start the GUI

if __name__ == '__main__':
    app.run(debug=True)
