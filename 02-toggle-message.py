from tkinter import *

msg1 = 'I am learning python programming'
msg2 = 'I am learning GUI programming using tkinter'

msg_num = 1

control_msg = None
root_window = None

def toggle_button_handler():
    global msg_num
    if msg_num == 1:
        control_msg.set(msg1) #different and important
        msg_num = 2
    elif msg_num == 2:
        control_msg.set(msg2) #different and important
        msg_num = 1


def exit_button_handler():
    root_window.destroy()



root_window = Tk()
root_window.title('Toggle demo')
root_window.geometry('300x200')

control_msg = StringVar()#different and important line
msg = Label(root_window)
msg.configure(textvariable = control_msg)
control_msg.set(msg1)   #different and important line
msg.grid(row=0, column=0)

toggle_button = Button(root_window)
toggle_button.configure(text='Toggle', command=toggle_button_handler)
toggle_button.grid(row=1, column=0)

root_window.mainloop()
