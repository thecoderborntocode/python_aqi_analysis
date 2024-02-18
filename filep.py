import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
import csv
path = 'csvtest.csv'
# path1 = pd.read_csv('csvtest.csv')
root = tk.Tk()
root.title("V_J CORP")
root.geometry("700x500")
file = pd.read_csv("country3.csv")
file32 = pd.read_csv("country2.csv")
# file2 = pd.read_csv("country3.csv")
label2 = tk.Label(root)
labelrem = tk.Label(root)
def getdatafrombutton():
    entry1.destroy()
    entry2.destroy()
    entry3.destroy()
    entry4.destroy()
    labelrem.destroy()
    global label2
    label2.destroy()
    try:

        ent = entry.get()
        entdata = file32[ent]

        label2 = tk.Label(root, text=entdata,font=30)
        label2.pack()
    except Exception:
        label2 = tk.Label(root,text="DID YOU ENTER THE FIRST NAME CAPITAL? DID YOU ENTER VALID VALUE")
        label2.pack(pady=50)
entry = tk.Entry(root,width=100,bg="orange",fg="black")
label = tk.Label(root,text="ENTER THE NAME OF A COUNTRY TO FETCH AQI VALUE")
cap = tk.Label(root,text="THE FIRST LETTER SHOULD BE CAPITAL: EX:: India,Russia")

label.pack()
cap.pack()
entry.pack(padx=100)
button = tk.Button(root,text="SUBMIT",command=getdatafrombutton)
button.pack()
labelcmp = tk.Label(root,text="YOU CAN COMPARE THEE AQI OF 4 COUNTRIES ")
labelcmp.pack()
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)
button3 = tk.Button(root)
labelerror = tk.Label(root)
l1 = tk.Label(root)
l2 = tk.Label(root)
l3 = tk.Label(root)
l4 = tk.Label(root)
data = []
def compare():
    label2.destroy()
    labelerror.destroy()
    global a


    global entry1,entry2,entry3,entry4
    entry1.destroy()
    entry2.destroy()
    entry3.destroy()
    entry4.destroy()
    global l1,l2,l3,l4
    global labelrem
    labelrem.destroy()
    labelerror.destroy()
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    labelrem = tk.Label(root,text="enter the name of any 4 countries only ")
    labelrem.pack()
    entry1 = tk.Entry(root,width=50,bg="orange",fg="black")
    l1 = tk.Label(root)
    l2 = tk.Label(root)
    l3= tk.Label(root)
    l4 = tk.Label(root)
    entry2 = tk.Entry(root,width=50,bg="orange",fg="black")
    entry3 = tk.Entry(root,width=50,bg="orange",fg="black")
    entry4 = tk.Entry(root,width=50,bg="orange",fg="black")
    entry1.pack()
    l1.pack()
    entry2.pack()
    l2.pack()
    entry3.pack()
    l3.pack()
    entry4.pack()
    def displaygraph():

        try:

            get1 = entry1.get()
            get2 = entry2.get()
            get3 = entry3.get()
            get4 = entry4.get()
            data = [["country","AQI LEVEL"],
                    [get1,file[get1]],
                    [get2,file[get2]],
                    [get3,file[get3]],
                    [get4,file[get4]]
                    ]

            with open(path,mode='w',newline='') as file1:
                write = csv.writer(file1)
                write.writerows(data)
            path1 = pd.read_csv('csvtest.csv')
            plt.bar(path1['country'],path1['AQI LEVEL'],color="red")
            plt.xlabel('Country')
            plt.ylabel('AQI')
            plt.title('AQI Comparison between India and China')

            plt.show()
        except:
            global labelerror
            labelerror.destroy()
            labelerror = tk.Label(root,text="SOMETHING WENT WRONG MAY BE SOME INFO IS NOT FOUND OR DID YOU ENTER THE FIRST WORLD CAPITAL!?")
            labelerror.pack()
    global button3
    button3.destroy()
    button3 = tk.Button(root,command=displaygraph,text="COMPARE!!")
    button3.pack()

button2 = tk.Button(root,text="COMPARE",command=compare)
button2.pack()
root.mainloop()