from tkinter import *
import pandas as pd

root = Tk()
root.title("Application Name")
root.geometry("640x320")

data = pd.read_csv('./resources/file.csv')

print(list(data.columns.values))
print(data['Unnamed: 0'])
entered = StringVar()
entry = Entry(root,textvariable=entered).place(x=200,y=50)

text = Text(root)


def display():
    print('Hello '+str(entered.get()))

    text.insert(INSERT, str(entered.get()))




botton1 = Button(text='Click me',fg ='red',command=display)

label1 = Label(root,text='One',bg='green',fg='white')




botton1.grid()


root.mainloop()


