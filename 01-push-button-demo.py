from tkinter import *


def ok_button_handler():
    print('OK BUTTON IS CLICKED')


root_window  = Tk()
root_window.title('Push button demo')
root_window.geometry('300x200')


ok_button = Button(root_window)
ok_button.configure(text='ok', command=ok_button_handler)
ok_button.grid(row=0, column=0)


print('ATA CONTROL FLOW root_window.mainloop() MADHE JAT AHE')
root_window.mainloop()

print('MALA TERMINAL HO - ASHI ADNYA ALI')
