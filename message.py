from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

root.geometry("733x570")
root.title("pycharm")

def myfunc():
    print("haha")
    
    
def help():
    print("say ur problem")
    a = tmsg.showinfo("help","fbi is on the way")
    # print(a)
    

def rate():
    print("rate us")
    value = tmsg.askquestion("was ur exp gud?","you used our gui!!!")
    print(value)
    if value == "yes":
        msg = "great .Rate us on store"
    else:
        msg = "give us recommendations?"
    tmsg.showinfo("experience",msg)
    
    
    
def ask():
    ans = tmsg.askretrycancel("will u be our partner", " no thanks")
    if ans:
        print("check again")
    else:
        print("thanks for not joining us")

# dropdown menu
mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="new project", command=myfunc)
m1.add_command(label="save", command=myfunc)
m1.add_separator()
m1.add_command(label="edit", command=myfunc)
m1.add_command(label="scale", command=myfunc)
m1.add_separator()
m1.add_command(label="exit", command=exit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="file",menu=m1)


m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="drag", command=myfunc)
m2.add_command(label="cut", command=myfunc)
m2.add_separator()
m2.add_command(label="copy", command=myfunc)
m2.add_command(label="paste", command=myfunc)
m2.add_separator()
m2.add_command(label="exit", command=exit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="edit",menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="help", command=help)
m3.add_command(label="rate us", command=rate)
m3.add_command(label="friends", command=ask)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="help",menu=m3)

root.mainloop()