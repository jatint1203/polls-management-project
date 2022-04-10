from tkinter import *
import time
import random  # FOr OTP generation

from PIL import Image, ImageTk
import smtplib  # This Library is for sending mail
from tkinter import messagebox
from tkinter import filedialog

from collections import Counter
import mysql.connector
import secrets
import string

'''
root.withdraw() = Hide the root window
root.deconify() = Unhide the root window
Toplevel = It will create a new window
destroy() = It will destroy window which is passed as parameters in destroy paranthesis

lambada function can be used to call multiple function by clicking a button


'''
def sql_query():
    db = mysql.connector.connect(host="localhost", user="root",port=3306,   password ="", database="test")


    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method
    cursor.execute("SELECT * FROM `admin`")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print(data)
    # disconnect from server
    db.close()



def login_page_1():
    root.state('zoomed')
    global u_id, u_number, u_pass
    u_id = StringVar()
    u_number = StringVar()
    u_pass = StringVar()

    #Loadinng the image to python
    load = Image.open(r"Img\Voting image.jpeg").resize((screen_width,screen_height))
    render = ImageTk.PhotoImage(load)


    #Placing the image to an appropriate position
    img = Label(root, image=render)
    img.image = render
    img.place(x=0, y=0)

    root.state('zoomed')


    # Creating a frame for user log in
    frame_1 = Frame(root, height=420, width=450, bg="#FB795B")
    frame_1.place(x=900, y=200)

    login_lable = Label(frame_1, text='Login Here', font='Times 32 bold', bg="#FB795B").place(x=105, y=10)

    # Aadhar card info
    login_aadhar = Label(frame_1,bg="#FB795B", text='Unique Number', font='Helvetica 15 bold').place(x=40, y=80)
    u_UID = Entry(frame_1, bg="gray", textvariable=u_id).place(x=40, y=110, width=250, height=25)

    #Mobile number info
    login_mobile = Label(frame_1,bg="#FB795B", text='Mobile Number', font='Helvetica 15 bold').place(x=40, y=150)
    login_number = Entry(frame_1, bg="gray", textvariable=u_number).place(x=40, y=180, width=250, height=25)

    login_pass = Label(frame_1,bg="#FB795B",text='Password', font='Helvetica 15 bold').place(x=40, y=220)
    login_pass = Entry(frame_1, bg="gray", textvariable=u_pass).place(x=40, y=250, width=250, height=25)
    #pass_info= Label(root,bg="#FB795B", text="Your password is SE_Roll Number. Like SE_41",font='Helvetica 10 bold').place(x=930, y=480, width=300, height=20)

    # For the captcha purpose
    #captch_entry = Entry(frame_1, bg="gray").place(x=40, y=310, width=80, height=30)
    #captch_lable = Label(frame_1, bg="black").place(x=150, y=310, width=120, height=35)



    # Login button to redirect to next page
    login = Button(root, text='Login',font='Times 20 ', bg="Orange",cursor="hand2",command= u_validate, bd=0).place(x=1050, y=490, width=115,
                                                                                     height=50)  # u_validate function will fetch the values


    # Admin Button and next page command
    admin_button = Button(root, text="Admin Login",font='Times 15 ',bg="Orange",cursor="hand2", command=admin).place(x=1100, y=70, width=130,
                                                                                height=50)  # Calling admin function
# Contact_us and next page command
    Contact_us = Button(root, text="Contact Us",font='Times 15 ',bg="Orange",cursor="hand2", command= contact).place(x=1300, y=70, width=130, height=50)  # Calling contact function

    add_user = Button(root, text="New User? SIGN UP",font='Times 12',bg="Orange",cursor="hand2", command=set_timer).place(x=1000, y=565, width=200,height=20)  # Calling admin function
def contact():
    contact_us = Toplevel()
    contact_us.title("Contact Us")
    contact_us.geometry('1000x600+200+100')
    load = Image.open(r"Img\voting image.jpeg").resize((1000, 600))
    render = ImageTk.PhotoImage(load)

    # Placing the image to an appropriate position

    img = Label(contact_us, image=render)
    img.image = render
    img.place(x=0, y=0)
    contact_us.resizable(False, False)


def vote():
    # Intializing the user inter phase

    global user_vote
    user_vote = Toplevel()
    user_vote.state('zoomed')
    global render
    root.withdraw()  # Hiding the root window
    #user_vote.geometry('1000x700+100+50')
    user_vote.title("Choose Candidate")

    user_vote.state('zoomed')
    user_vote.resizable(False, False)
    load = Image.open(r"Img\voting image.jpeg").resize((screen_width,screen_height))
    render = ImageTk.PhotoImage(load)

    # Placing the image to an appropriate position

    img = Label(user_vote, image=render)
    img.image = render
    img.place(x=0, y=0)

    #Creating a Lable for user_name Delete them later
    u_name_welcome = Label(user_vote, text="Welcome,", font='Helvetica 25 bold').place(x=400, y=45)
    u_name_show =Label(user_vote, text=u_info[1], font='Helvetica 25 bold').place(x=559,y=45)
    try:
        db = mysql.connector.connect(host="localhost", user="root", port=3306, password="", database="polls")
        cursor = db.cursor()
        '''
        Here I feched all data from my created dataabse and started to fetching them if 
        al data is correct it will give me a tuple of data if it found something incorrect then
        it will show as none

        '''
        cursor.execute("SELECT  `a_name` FROM `voters_details`")
        candidate_names = cursor.fetchall()
        print(candidate_names)
        print(candidate_names[0])
        print(candidate_names[1])
        print(candidate_names[2])
        print(candidate_names[3])
    except Exception as e:
        pass

    names=[]
    for i in range(0,6):
        name_lbl = Label(user_vote, text = candidate_names[i],height=1,width=10,font='Helvetica 15 bold')
        names.append(name_lbl)
    names[0].place(x=300, y=355)
    names[1].place(x=705, y=355)
    names[2].place(x=1095, y=355)
    names[3].place(x=303, y=670)
    names[4].place(x=705, y=670)
    names[5].place(x=1095, y=670)


    # Creating radion button

    var = StringVar()
    R1 = Radiobutton(user_vote, text="SELECT",cursor="hand2", variable=var, height=1, width=10, value=candidate_names[0],indicatoron=0,font='Helvetica 15 bold',bg=	'#FF8C00').place(x=310, y=390,height=35,width=110)

    R2 = Radiobutton(user_vote, text="SELECT",cursor="hand2", variable=var, height=1, width=10, value=candidate_names[1],indicatoron=0,font='Helvetica 15 bold',bg=	'#FF8C00'
                     ).place(x=715, y=390,height=35,width=110)

    R3 = Radiobutton(user_vote, text="SELECT",cursor="hand2", variable=var, height=1, width=10, value=candidate_names[2],indicatoron=0,font='Helvetica 15 bold',bg=	'#FF8C00'
                     ).place(x=1105, y=390,height=35,width=110)

    R4 = Radiobutton(user_vote, text="SELECT",cursor="hand2", variable=var, height=1, width=10,value=candidate_names[3], indicatoron=0,font='Helvetica 15 bold',bg=	'#FF8C00').place(x=310, y=705,height=35,width=110)

    R5 = Radiobutton(user_vote, text="SELECT",cursor="hand2", variable=var, height=1, width=10, value=candidate_names[4],indicatoron=0,font='Helvetica 15 bold',bg=	'#FF8C00'
                     ).place(x=715, y=705,height=35,width=110)

    R6 = Radiobutton(user_vote, text="SELECT",cursor="hand2", variable=var, height=1, width=10, value=candidate_names[5],indicatoron=0,font='Helvetica 15 bold',bg=	'#FF8C00').place(x=1105, y=705,height=35,width=110)

    submit_button = Button(user_vote, text="Choose Candidate",cursor="hand2", bg="Orange",font='Times 15', command=lambda :[ errorthrow(var.get())]).place(x=690, y=775, width=170,
                                                                                                 height=50)  # Calling thank function
    home_btn = Button(user_vote, text="Logout",cursor="hand2", bg="Orange",font='Times 15',
                      command=lambda: (login_page_1(), user_vote.destroy())).place(x=1325, y=87, width=130, height=50)

def errorthrow(var):
    if var=='':
        messagebox.showerror("Error", "Choose Candidate First")
    else:
        count(var)
        thank()





votes = [] #Intializing  a list global
vote_done=[] # This list will store data of all candidates who voted already


def count( varii):
    global max_votes, winner_is1,winner_is2,winner_is3

    print("done")
    votes.append(varii)
    print(votes)


        # Count the votes for persons and stores in the dictionary
    vote_count = Counter(votes)


        # Find the maximum number of votes
    max_votes = max(vote_count.values())
    print(max_votes)


        # Search for people having maximum votes and store in a list
    lst = [i for i in vote_count.keys() if vote_count[i] == max_votes]
     #Cabdidate  Got max vote

        # Sort the list and print lexicographical smallest name
    print(sorted(lst)[0]) #Candidate name who got max vote
    winner_is1=sorted(lst)[0]




def u_validate():

    #Delelte 109 Line comment also
    #Direct calling it then I will delete it
    global u_info
    print(u_id.get())
    print(u_number.get())
    if u_id.get() == "" or u_number.get() == "" or u_pass.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        try:
            '''
            Create databse coloum name as provided below other wise it will throw an error
            '''
            db = mysql.connector.connect(host="localhost", user="root", port=3306, password="", database="polls")
            cursor = db.cursor()
            '''
            Here I feched all data from my created dataabse and started to fetching them if 
            al data is correct it will give me a tuple of data if it found something incorrect then
            it will show as none

            '''
            cursor.execute("SELECT * FROM `user_login` WHERE id=%s AND phone_number=%s AND password=%s",
                        (u_id.get(), u_number.get(),u_pass.get()))
            u_info = cursor.fetchone()

            print(u_info)

            if u_info == None:
                messagebox.showerror("Error", "Invalid Credintials")

            else:
                messagebox.showinfo("Welcome", "You're welcome")
                if u_info[0] in vote_done:     #If roll number is present in vote_done then it will throw an error
                    messagebox.showerror("Error", "You have already voted.")
                else:
                    messagebox.showinfo("Welcome", "You're welcome")
                    vote_done.append(u_info[0])
                    vote()  # Calling vote function


        except Exception as e:
            print(e)



def thank():
    # Intializing the user inter phase
    thank_page = Toplevel()
    thank_page.state('zoomed')
    user_vote.destroy()  # Destroying previous page i.e. vote function page
    #thank_page.geometry('970x600+100+50')
    # Loadinng the image to pythonpng
    load = Image.open(r"Img\finish.jpeg").resize((screen_width,screen_height))
    render = ImageTk.PhotoImage(load)

    # Placing the image to an appropriate position
    img = Label(thank_page, image=render)
    img.image = render
    img.place(x=0, y=0)
    thank_page.title("Thank You and then first page")

    thank_page.state('zoomed')
    thank_page.resizable(False, False)



    # Lambda function is used because it is one liner function
    # root.deconify() is used to unhide the hided window
    # lambda is used here to call two function
    #thank_btn = Button(thank_page, text="Finish",font='Times 25', bg="#E19696",command=lambda: (login_page_1, thank_page.destroy())).place(x=710, y=560, width=120,height=55)
    thank_btn = Button(thank_page, text="Finish",cursor="hand2",font='Times 25', bg="#E19696", command = lambda: (login_page_1(), thank_page.destroy())).place(x=710, y=560, width=120, height=55)


def admin():
    global admin_details, login_email_id_parameter, frame_2, a_username, a_password, a_email, a_email_otp

    a_username = StringVar()
    a_password = StringVar()
    a_email = StringVar()
    a_email_otp = StringVar()




    admin_details = Toplevel()
    admin_details.state('zoomed')
    root.withdraw()  # It will hide the root window or main window
    # Only trying that this couldd be possible way or not
    # root.geometry('0x0')

    # Intializing the user inter phase
    #admin_details.geometry('970x600+100+50')
    admin_details.title("Admin Login")
    admin_details.resizable(False, False)
    load = Image.open(r"Img\admin.png").resize((screen_width,screen_height))
    render = ImageTk.PhotoImage(load)


    #Placing the image to an appropriate position
    img = Label(admin_details, image=render)
    img.image = render
    img.place(x=0, y=0)
    # Creating a frame for user log in
    frame_2 = Frame(admin_details, height=500, width=400, bg="#455361")
    frame_2.place(x=560, y=170)

    login_lable = Label(frame_2, text='Login Here', font='Times 32 bold',bg="#455361").place(x=90, y=10)

    # User name info
    login_username = Label(frame_2, text='User Name', font='Helvetica 15',bg="#455361").place(x=40, y=80)
    login_uname = Entry(frame_2, bg="gray", textvariable=a_username).place(x=40, y=115, width=250, height=25)

    # Password info
    login_pass = Label(frame_2, text='Password', font='Helvetica 15',bg="#455361").place(x=40, y=155)
    login_password = Entry(frame_2, bg="gray", textvariable=a_password).place(x=40, y=190, width=250, height=25)

    login_email = Label(frame_2, text='Email', font='Helvetica 15',bg="#455361").place(x=40, y=235)
    login_email_id = Entry(frame_2, bg="gray", textvariable=a_email).place(x=40, y=270, width=250, height=25)

    email_otp = Label(frame_2, text='Enter OTP', font='Helvetica 15',bg="#455361").place(x=40, y=315)
    email_otp_enter = Entry(frame_2, bg="gray", textvariable=a_email_otp).place(x=40, y=350, width=250, height=25)

    # login_password.show("*")
    login_send_otp = Button(frame_2, text="Send OTP",cursor="hand2", font='Times 15',
                            command=lambda: (send_otp_mail(a_email.get())))
    login_send_otp.place(x=40, y=385, width=95, height=30)

    # widget = Entry(parent, show="*", width=15)
    # login_email_id.config(state='disabled')
    # For the captcha purpose
    # captch_entry = Entry(frame_2, bg="gray").place(x=40, y=230, width=80, height=30)
    # captch_lable = Label(frame_2, bg="black").place(x=140, y=240, width=120, height=35)
    # Login button to redirect to next page

    login_send_otp = Button(frame_2, text="Login",cursor="hand2", font='Times 20 bold', bg="Orange",
                            command=admin_details_validate)
    login_send_otp.place(x=120, y=440, width=140, height=50)

    Back_btn = Button(admin_details, text="Back",cursor="hand2", font='Times 25', bg="Orange",
                      command=lambda: (login_page_1(),admin_details.destroy())).place(x=70, y=70,
                                                                                                       width=115,
                                                                                                       height=50)


def admin_details_validate():
    #admin_basic_work()
    #admin_basic_work()  # Calling here only for testing as databas I haven't created yet
    if a_username.get() == "" or a_password.get() == "" or a_email.get() == "" or a_email_otp.get() == "" or a_password=="":
        messagebox.showerror("Error", "All fields are required")
    else:
        try:
            '''
            Create databse coloum name as provided below other wise it will throw an error
            '''
            db = mysql.connector.connect(host="localhost", user="root", port=3306, password="", database="polls")
            cursor = db.cursor()
            '''
            Here I feched all data from my created dataabse and started to fetching them if 
            al data is correct it will give me a tuple of data if it found something incorrect then
            it will show as none

            '''
            cursor.execute("select * from admin_details where a_name=%s and a_pass=%s and a_email=%s",
                        (a_username.get(), a_password.get(), a_email.get()))
            u_info = cursor.fetchone()

            print(u_info)

            if u_info == None:
                messagebox.showerror("Error", "Invalid Credintials")

            else:
                if (a_email_otp.get() == OTP_numbers):  # I created OTP Number as a global variable
                    messagebox.showinfo("Welcome", "You're welcome")
                    admin_basic_work()  # Calling vote function

                else:
                    messagebox.showerror("Error", "Invalid OTP")

        except Exception as e:
            print(e)


def send_otp_mail(receiver_email):
    global OTP_numbers
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    MAX_OTP = 6

    OTP_numbers = []
    for i in range(MAX_OTP):
        c = random.choice(number)
        OTP_numbers.append(c)

    OTP_numbers = ''.join(OTP_numbers)  # This function will joint all number so it can be look like a otp
    print(OTP_numbers)

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "ganup345@gmail.com"
    password = "Radha2009"
    message = (f"This is your OTP for the registration {OTP_numbers}")

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls()  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)

        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
        print("Send")
        time.sleep(3)


def admin_basic_work():
    global admin_work
    admin_work = Toplevel()
    admin_work.state('zoomed')
    admin_details.destroy()
    # Intializing the user inter phase
    #admin_work.geometry('970x600+100+50')
    load = Image.open(r"Img\candiate.png").resize((screen_width,screen_height))
    render = ImageTk.PhotoImage(load)

    # Placing the image to an appropriate position
    img = Label(admin_work, image=render)
    img.image = render
    img.place(x=0, y=0)
    admin_work.title("Admin Work")
    admin_work.resizable(False, False)

    aware_button = Button(admin_work,font='Times 15', text="Notify",cursor="hand2", command=aware_user).place(x=270, y=480, width=115, height=45)
    #timer_button = Button(admin_work,font='Times 15', text="Add User",cursor="hand2", command=set_timer).place(x=935, y=350, width=115, height=45)
    winner_button = Button(admin_work,font='Times 15', text="Winner",cursor="hand2", command=Winner_Candidate).place(x=715, y=480, width=115,
                                                                                      height=45)
    add_candidate_button = Button(admin_work,font='Times 15', text="Add Candidate",cursor="hand2", command=Add_Candidate).place(x=1165, y=480,
                                                                                                 width=135, height=45)
    # send_user_mail = Button(admin_work, text= "Send Mail",bg="Gray", command = send_mail).place(x=200, y=35, width=115, height=35) # Sending mail to user for awareness

    home_btn = Button(admin_work, text="Home",font='Times 25', bg="Orange",cursor="hand2",
                      command=lambda: (admin_work.destroy(), login_page_1())).place(x=1320, y=66,
                                                                                                       width=115,
                                                                                                       height=50)


def aware_user():
    global aware_user
    # Intializing the user inter phase
    aware_user = Toplevel()
    aware_user.geometry('1000x600+200+100')
    load = Image.open(r"Img\voting image.jpeg").resize((1000,600))
    render = ImageTk.PhotoImage(load)

    # Placing the image to an appropriate position
    img = Label(aware_user, image=render)
    img.image = render
    img.place(x=0, y=0)
    aware_user.title("Aware User")
    aware_user.resizable(False, False)
    description_email = Label(aware_user, text="This will send an E-mail to all voters",
                              font='Times 20 bold').place(x=280,y=350)
    send_mail_to_all = Button(aware_user, text="Send E-mail",cursor="hand2",font='Times 15', bg="Orange", command=send_mail).place(x=450,y=400)

    description_sms = Label(aware_user, text="This will send an SMS to all voters", font='Times 20 bold').place(x=300,y=170)
    send_mail_to_all = Button(aware_user, text="Send SMS",cursor="hand2",font='Times 15', bg="Orange", command=send_mail).place(x=460,y=220)


def set_timer():
    global set_timer, user_fname2,user_dob,user_email2,user_pass,user_contat2,user_confirm_pass,user_city2,user_pincode2, user_add2
    # Intializing the user inter phase
    set_timer = Toplevel()
    set_timer.geometry('1000x600+200+100')
    load = Image.open(r"Img\voting image.jpeg").resize((1000, 600))
    render = ImageTk.PhotoImage(load)

    # Placing the image to an appropriate position
    img = Label(set_timer, image=render)
    img.image = render
    img.place(x=0, y=0)
    set_timer.title("Add User")
    set_timer.resizable(False, False)
    user_fname2 = StringVar()
    user_dob = StringVar()
    user_email2 = StringVar()
    user_pass = StringVar()
    user_contat2 = StringVar()
    user_confirm_pass = StringVar()
    user_city2 = StringVar()
    user_pincode2 = StringVar()
    user_add2 = StringVar()
    login_lable = Label(set_timer, text='Register Here', font='Heletica 32 bold').place(x=80, y=10)

    # User name info
    Cand_fname = Label(set_timer, text='Full Name', font='Helvetica 15 bold').place(x=40, y=80)
    Cand_fname1 = Entry(set_timer, bg="gray", textvariable=user_fname2).place(x=40, y=120, width=250, height=25)

    # Password info
    Cand_mname = Label(set_timer, text='DOB', font='Helvetica 15 bold').place(x=40, y=160)
    Cand_mname1 = Entry(set_timer, bg="gray", textvariable=user_dob).place(x=40, y=200, width=250, height=25)

    Cand_lname = Label(set_timer, text='Contact Number', font='Helvetica 15 bold').place(x=40, y=240)
    Cand_lname1 = Entry(set_timer, bg="gray", textvariable=user_contat2).place(x=40, y=280, width=250, height=25)

    Cand_contact = Label(set_timer, text='Email', font='Helvetica 15 bold').place(x=40, y=320)
    Cand_contat1 = Entry(set_timer, bg="gray", textvariable=user_email2).place(x=40, y=360, width=250, height=25)

    # User name info
    Cand_email = Label(set_timer, text='Create Password', font='Helvetica 15 bold').place(x=40, y=400)
    Cand_email1 = Entry(set_timer, bg="gray", textvariable=user_pass).place(x=40, y=440, width=250, height=25)

    # Password info
    Cand_state = Label(set_timer, text='Confirm Password', font='Helvetica 15 bold').place(x=500, y=80)
    Cand_state1 = Entry(set_timer, bg="gray", textvariable=user_confirm_pass).place(x=500, y=120, width=250, height=25)

    Cand_city = Label(set_timer, text='City', font='Helvetica 15 bold').place(x=500, y=160)
    Cand_city1 = Entry(set_timer, bg="gray", textvariable=user_city2).place(x=500, y=200, width=250, height=25)

    Cand_pincode = Label(set_timer, text='Pincode', font='Helvetica 15 bold').place(x=500, y=240)
    Cand_pincode1 = Entry(set_timer, bg="gray", textvariable=user_pincode2).place(x=500, y=280, width=250,
                                                                                      height=25)

    Cand_add = Label(set_timer, text='Address', font='Helvetica 15 bold').place(x=500, y=320)
    Cand_add1 = Text(set_timer, bg="gray", width=30, height=4).place(x=500, y=360, width=250, height=100)


    # Creating a frame for user log in
    # cand_frame = Frame(Add_Candidate, height=450, width=600).place(x=40,y=80)
    #query = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)"
   #"VALUES (%s, %s, %s, %s, %s)"
    save_info_cand = Button(set_timer, text="Save",cursor="hand2",bg="Orange", font='Times 24 bold',
                            command=lambda :[root.withdraw(),add_user_place_vacant_checking()])
    save_info_cand.place(x=390, y=540, height=50, width=150)
    global Upload_aadhar
    text="Upload Aadhar Card"
    global Upload_aadhar
    Upload_aadhar= Button(set_timer, text=text,cursor="hand2",bg="Orange", font='Times 20 bold',
                            command=browseFiles).place(x=320, y=480, height=40, width=300)
    #Upload_aadhar.configure(text="gfst")

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("Text files",".png"),("all files",".")))





def add_user_place_vacant_checking():
    if user_fname2.get()=="" or user_contat2.get()==""or user_email2.get()==""or user_pincode2.get()=="" or user_confirm_pass.get()=="":
        messagebox.showerror("Error", "All fields are required", )
    else:
        root.deiconify()
        root.state('zoomed')
        set_timer.destroy()
       # print(user_fname2.get(),user_contat2.get(),user_email2.get(),user_confirm_pass.get())
        j=1
        insert_into_database(user_fname2.get(),user_email2.get(),j,user_contat2.get(),user_confirm_pass.get())




def Winner_Candidate():
    global Winner_Candidate
    # Intializing the user inter phase
    Winner_Candidate = Toplevel()
    Winner_Candidate.geometry('1000x600+200+100')
    load = Image.open(r"Img\voting image.jpeg").resize((1000, 600))
    render = ImageTk.PhotoImage(load)

    # Placing the image to an appropriate position
    img = Label(Winner_Candidate, image=render)
    img.image = render
    img.place(x=0, y=0)
    Winner_Candidate.title("Winner Candidate")
    Winner_Candidate.resizable(False, False)
    #print f("{lst[0]} and got {max_votes}")
    text=winner_is1
    #text1=winner_is2
    #@text2=winner_is3
    winner = Label(Winner_Candidate,text=text,bg="Orange", font='Times 53 bold',).place(x=450,y=300)
   # winner = Label(Winner_Candidate,text=text,bg="Orange", font='Times 30 bold',).place(x=150,y=400)
    #winner = Label(Winner_Candidate,text=text,bg="Orange", font='Times 30 bold',).place(x=150,y=450)
    #winner.config(text= winner_is, height=5, width=50)
    #Winner_Candidate.wm_attributes("-transparentcolor", 'grey')


def insert_into_database(name,email,k,contact,password):
    global strong_username
    try:
        db = mysql.connector.connect(host="localhost", user="root", port=3306, password="", database="polls")
        cursor = db.cursor()

    except Exception as e:
        print(e)


    # using random.choices()
    # generating random strings
    gen_pass = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                  for i in range(7))

    # print result
    print("The generated random password : " + str(gen_pass))
    strong_username=str(gen_pass)
    if(k==1):

        query="INSERT INTO `user_login`(`id`, `name`, `phone_number`, `password`, `email`) VALUES (%s,%s,%s,%s,%s)"
        val=(strong_username,name,contact,password,email)
        cursor.execute(query,val)
        db.commit()
        j = 2
        send_mail(email,j)
        print('done')
    elif(k==2):
        query="INSERT INTO `voters_details`(`a_name`, `a_pass`, `a_email`) VALUES (%s,%s,%s)"

        val=(name,strong_username,email)
        cursor.execute(query,val)
        db.commit()
        j = 3
        send_mail(email,j)
        print('done')




def Add_Candidate():
    print("REached")
    global Add_Candidate, Cand_fname2 ,Cand_mname2  ,Cand_lname2 ,Cand_contat2 ,Cand_email2 ,Cand_state2 ,Cand_city2, Cand_pincode2, Cand_add2
    # Intializing the user inter phase
    Add_Candidate = Toplevel()
    Add_Candidate.geometry('1000x600+200+100')
    load = Image.open(r"Img\voting image.png").resize((1000, 600))
    render = ImageTk.PhotoImage(load)

    # Placing the image to an appropriate position
    img = Label(Add_Candidate, image=render)
    img.image = render
    img.place(x=0, y=0)
    Add_Candidate.title("Add Candidate")
    Add_Candidate.resizable(False, False)

    # Hiding previous page
    #admin_work.withdraw()

    Cand_fname2 = StringVar()
    Cand_mname2 = StringVar()
    Cand_lname2 = StringVar()
    Cand_contat2 = StringVar()
    Cand_email2 = StringVar()
    Cand_state2 = StringVar()
    Cand_city2 = StringVar()
    Cand_pincode2 = StringVar()
    Cand_add2 = StringVar()
    login_lable = Label(Add_Candidate, text='Enter Candidates Details', font='Heletica 32 bold').place(x=80, y=10)

    # User name info
    Cand_fname = Label(Add_Candidate, text='Full Name*', font='Helvetica 15 bold').place(x=40, y=80)
    Cand_fname1 = Entry(Add_Candidate, bg="gray", textvariable=Cand_fname2).place(x=40, y=120, width=250, height=25)

    # Password info
    Cand_mname = Label(Add_Candidate, text='Area', font='Helvetica 15 bold').place(x=40, y=160)
    Cand_mname1 = Entry(Add_Candidate, bg="gray", textvariable=Cand_mname2).place(x=40, y=200, width=250, height=25)

    Cand_lname = Label(Add_Candidate, text='Post', font='Helvetica 15 bold').place(x=40, y=240)
    Cand_lname1 = Entry(Add_Candidate, bg="gray", textvariable=Cand_lname2).place(x=40, y=280, width=250, height=25)

    Cand_contact = Label(Add_Candidate, text='Contact Number*', font='Helvetica 15 bold').place(x=40, y=320)
    Cand_contat1 = Entry(Add_Candidate, bg="gray", textvariable=Cand_contat2).place(x=40, y=360, width=250, height=25)

    # User name info
    Cand_email = Label(Add_Candidate, text='Email*', font='Helvetica 15 bold').place(x=40, y=400)
    Cand_email1 = Entry(Add_Candidate, bg="gray", textvariable=Cand_email2).place(x=40, y=440, width=250, height=25)

    # Password info
    Cand_state = Label(Add_Candidate, text='State', font='Helvetica 15 bold').place(x=500, y=80)
    Cand_state1 = Entry(Add_Candidate, bg="gray", textvariable=Cand_state2).place(x=500, y=120, width=250, height=25)

    Cand_city = Label(Add_Candidate, text='City', font='Helvetica 15 bold').place(x=500, y=160)
    Cand_city1 = Entry(Add_Candidate, bg="gray", textvariable=Cand_city2).place(x=500, y=200, width=250, height=25)

    Cand_pincode = Label(Add_Candidate, text='Pincode', font='Helvetica 15 bold').place(x=500, y=240)
    Cand_pincode1 = Entry(Add_Candidate, bg="gray", textvariable=Cand_pincode2).place(x=500, y=280, width=250,
                                                                                      height=25)

    Cand_add = Label(Add_Candidate, text='Address', font='Helvetica 15 bold').place(x=500, y=320)
    Cand_add1 = Text(Add_Candidate, bg="gray", width=40, height=5).place(x=500, y=360, width=250, height=100)

    print(Cand_fname2.get())

    # Creating a frame for user log in
    # cand_frame = Frame(Add_Candidate, height=450, width=600).place(x=40,y=80)

    save_info_cand = Button(Add_Candidate, text="Save",cursor="hand2", bg="Orange", font='Helvetica 20 bold',
                            command=add_candidate_place_vacant_checking)
    save_info_cand.place(x=390, y=550, height=40, width=150)



def add_candidate_place_vacant_checking():
    if Cand_fname2.get()=="" or Cand_email2.get()=="":
        messagebox.showerror("Error", "All fields are required", )
    else:
        print(Cand_fname2.get())
        admin_work.deiconify()
        admin_work.state('zoomed')
        Add_Candidate.destroy()
        j = 2
        insert_into_database(Cand_fname2.get(),Cand_email2.get(),j,'None','None')


def admin_go_home_page():
    admin_work.destroy()
    login_page_1()


def send_sms():
    '''
    Here only copy the code from Fast2Sms website and send it so no need to worry.
    '''
    pass


def send_mail(email,j=1):#iamusingjvariablebecausetouseifelseo]condition
    print(j)
    print(email)

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "be.a.programmer9312@gmail.com"
    password = "Programmer7512"
    message = "Bunty Bhai"

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls()  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        if(j==1):
            f = open("emails.txt", "r+")

            receiver_email = []  # Intializing a list for sendnig mail
            for mails in f:
                receiver_email.append(mails)
            f.close()
        elif(j==2):
            receiver_email=email
            message="Your uername is " +strong_username
        elif(j==3):
            receiver_email=email
            message = "Your password is " +strong_username
        server.sendmail(sender_email, receiver_email, message)


    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


# Intializing the user inter phase

root = Tk()
#root.geometry('970x600+100+50')
root.title("Login Page")

#root.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())  # This will disable the cancel button
root.state('zoomed')  # This will  open page as maximize window
root.resizable(False, False)# It will disable the maximize or minimize button option GUI

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width,screen_height)
login_page_1()  # Calling the function


root.mainloop()