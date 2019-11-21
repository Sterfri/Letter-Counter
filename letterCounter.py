from tkinter import *


def letterCount():
    #gets user input
    name = e1.get()

    #makes everything lowercase
    name = name.lower()

    #populating the dic
    dic = {}
    for i in range(0, len(name)):

        if name[i] != ' ':
            if name[i] in dic:
                dic[name[i]] = dic[name[i]] + 1
            else :
                dic[name[i]] = 1


    #outputting the dic
    for x in dic:
        box.insert(INSERT, str(x) + " = " + str(dic[x]) + "\n")
        print(x, " = ", dic[x])


root = Tk()

header = Label(root, text="Letter counter", bg="orange")
header.pack(side=TOP, fill=X)

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

lab = Label(topFrame, text="Enter Sentence: ")
lab.pack()
e1 = Entry(topFrame)
e1.pack()

box = Text(topFrame, height=10, width=20)
box.pack()


button1 = Button(bottomFrame, text="Click Me", bg="grey", command=letterCount)
button1.pack()

root.mainloop()
