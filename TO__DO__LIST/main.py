import tkinter
from tkinter import*

root = Tk()
root.title("TO-DO-LIST")
root.geometry('400x650+400+100')
root.resizable(False,False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)

def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
             tasks= taskfile.readline()

        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END ,task)
    except:
        file=open("tasklist.txt","w")
        file.close()



Label(root,bg="#32405b",width=400,height=4).place(x=0,y=0)
# root.configure(bg="#32405b")
heading = Label(root,text="All TASKS",font="arial 20 bold", fg="white",bg="#32405b")
heading.place(x=130,y=20)

frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button = Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

frame1 = Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(250,0))

listbox = Listbox(frame1, font=("arial",12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


openTaskFile()
# delete_icon=PhotoImage(file="Image/3687412.png")
# Button(root,image=delete_icon,bd=0).pack(side=BOTTOM,pady=13)

button = Button(root,text="DELETE",font="arial 20 bold",width=6,bg="red",fg="white",bd=0,command=deleteTask)
button.place(x=150,y=575)

# class todo:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("To-Do-List")
#         self.root.geometry('650x410+300+150')
#
#         self.label1 = Label(self.root, text="To-Do-List-App",font= "arial, 25 bold", width=10, bd=5, bg="orange", fg="black")
#         self.label1.pack(side="top", fill=BOTH)
#
#         self.label2 = Label(self.root, text="Add Task", font="arial, 18 bold", width=10, bd=5, bg="orange", fg="black")
#         self.label2.pack(x=40, y=54)
#
#         self.label3 = Label(self.root, text="Tasks", font="arial, 25 bold", width=10, bd=5, bg="orange", fg="black")
#         self.label3.pack(x=320, y=54)
#
#
# def main():
#     root = Tk()
#     ui = todo (root)

root.mainloop()
#
#
# if __name__ == "__main--":
#     main()
