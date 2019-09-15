#import modules
 
from tkinter import *
import os
from PIL import ImageTk, Image
from CoordRead import CoordRead
import random
 
# Designing window for registration

INT_TO_COLOR = {0: 'green', 1: 'yellow', 2: 'orange', 3: 'red', 4: 'purple', 5: 'purple'}
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg=None).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()
    Button(register_screen, text="Back", width=5, height=1, command=delete_reg_screen).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    Button(login_screen, text="Back", width=5, height=1, command=delete_login_screen).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open('users/' + username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir('users')
    if username1 in list_of_files:
        file1 = open('users/' + username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success_usernames.append(username1)
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success


 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="Proceed to Map", command=load_map).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Load map

def load_map():
    global map_screen
    map_screen = Toplevel(login_screen)
    map_screen.title("parkMIT")
    map_screen.geometry("3000x2500")
    map_screen.configure(background='white')
    path = "MIT_map.png"

    Button(map_screen, text="Find nearby parking.", command=None).pack()
    Button(map_screen, text="Logout", command=delete_gui).pack()
    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open(path))
    canvas = Canvas(map_screen, width=3000, height=2500)
    canvas.create_image(-100, -110, anchor=NW, image=img)
    canvas.pack(expand=YES, fill=BOTH)

    for elt in parking_instances:
        y = elt[0] # lat
        x = elt[1] # lon
        print(tuple([y]+[x]))

        x_pixel = (57873.25138) * (x + 71.1058) + 130
        y_pixel = 770-(80769.40552 * (y - 42.3534))
        print(x_pixel)
        print(y_pixel)
        color = round(random.random() * 5)

        canvas.create_oval(x_pixel, y_pixel, x_pixel+10, y_pixel+10, fill=INT_TO_COLOR[color])

    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = Label(map_screen, image=img)

    #The Pack geometry manager packs widgets in rows or columns.
    panel.pack()
    
    # canvas = Canvas(map_screen, width=3000, height=2500)
    # canvas.pack()
    # img = PhotoImage(file='MIT_map.png')
    # canvas.create_image(300, 300, anchor=NW, image=img)
    mainloop()

    # global map_screen
    # map_screen = Toplevel(login_screen)
    # canvas = Canvas(map_screen, width=3000, height=2500)
    # background_image=PhotoImage(file='MIT_map.png')
    # canvas.pack()
    # image = canvas.create_image(3000, 2500, image=background_image)
    # line = canvas.create_line(10, 10, 100, 35, fill="red")
    # # map_screen.wm_geometry("794x370")
    # map_screen.title('Map')
    # map_screen.mainloop()

# root = Tk.Tk()
# canvas = Tk.Canvas(root)
# background_image=Tk.PhotoImage(file="map.png")
# canvas.pack(fill=Tk.BOTH, expand=1) # Stretch canvas to root window size.
# image = canvas.create_image(0, 0, anchor=Tk.NW, image=background_image)
# line = canvas.create_line(10, 10, 100, 35, fill="red")
# root.wm_geometry("794x370")
# root.title('Map')
# root.mainloop()
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()


def delete_login_screen():
    login_screen.destroy()

def delete_reg_screen():
    register_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
def delete_gui():
    main_screen.destroy()

# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("3000x2500")
    main_screen.title("Account Login")


    Label(text="Please Login or Register:", bg=None, width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    Label(text="").pack()
    Button(text="Exit", height = "1", width="15", command=delete_gui).pack()
    
    main_screen.mainloop()

def login_api():
    main_account_screen()
    try:
        print('User logged in:', login_success_usernames[-1])
    except:
        print('No user logged in.')
    if len(login_success_usernames) == 0:
        return None
    else:
        return login_success_usernames[-1]
    print(result)
    return result

parking_instances = CoordRead('coordinates.txt')
login_success_usernames = []
login_api()
