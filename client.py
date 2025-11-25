import tkinter as tk
import getpass
import requests

ip = ""

app = tk.Tk()
app.title("pycapi - connect")
t = tk.Entry(app)
t.pack(padx=20,pady=10)
def connect():
    global ip
    ip = t.get()
    app.destroy()
b1 = tk.Button(app,text="Connect",command=connect)
b1.pack(padx=20,pady=5)
app.mainloop()

root = tk.Tk()
root.title("pycapi - "+ip)
chat = tk.Text(root,height=10,width=50)
chat.pack()
input_frame = tk.Frame(root)
input_frame.pack()

entry_frame = tk.Frame(input_frame)
entry_frame.pack(side="left")

nick = tk.Entry(entry_frame)
nick.insert(0, getpass.getuser())
nick.pack()
msg = tk.Entry(entry_frame)
msg.pack()

def refresh():
    msgs_raw = requests.get("http://"+ip+":7007/msg")
    msgs = msgs_raw.json()
    chat.config(state="normal")
    chat.delete(1.0,tk.END)
    for key, value in msgs.items():
        chat.insert("end", f"{key} - {value}\n")
    chat.config(state="disabled")
    chat.see("end")

def send():
    requests.post("http://"+ip+":7007/send",json = {"name": nick.get(),"msg": msg.get()})
    msg.delete(0,tk.END)
    if nick.get() == "setmotd":
        nick.delete(0,tk.END)
        nick.insert(0,getpass.getuser())
    refresh()
    
b2 = tk.Button(input_frame, text="Send", command=send)
b2.pack(side="left", padx=5)
b3 = tk.Button(input_frame, text="Refresh", command=refresh)
b3.pack(side="left", padx=5)

def refloop():
    refresh()
    root.after(5000, refloop)
refloop()

root.mainloop()
