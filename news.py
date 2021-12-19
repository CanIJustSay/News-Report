from tkinter import *
from tkinter.ttk import *
import requests
import os
from tkinter import messagebox
os.system("cls")

root = Tk()
root.title("News Report")

root.geometry("500x300")


countryLabel = Label(root, text="Enter City Name: ",
                     font=("bold", 10)).place(x=620, y=80)
countryText = StringVar()
countryInput = Entry(root, textvariable=countryText)
countryInput.place(x=725, y=79)


def GetCode():
    link = "https://api.printful.com/countries"
    country = countryText.get()
    response = requests.get(link)
    data = response.json()

    result = data["result"]
    cc = ''
    for i in result:
        if i["name"].lower() == country.lower():
            cc = i["code"].lower()
    print(cc)
    if cc == '':
        messagebox.showerror('Error', "Country Not Found: {}".format(country))
    else:
        GetNews(cc)


def GetNews(c):
    link = "https://newsapi.org/v2/top-headlines?country=" + \
        c + "&apiKey=bdc912d442614e15846f1804f1b751d8"

    response = requests.get(link)
    data = response.json()

    articles = data["articles"]
    myArt = ''
    counter = 0

    for i in articles:
        counter += 1

        myArt = myArt + str(counter)+". " + i["title"] + '\n'
    newsLabel.config(text=myArt)


goButton = Button(root, text="Go", width=12, command=GetCode)
goButton.place(x=715, y=100)

newsLabel = Label(root, text='', font=("bold", 10))
newsLabel.place(x=615, y=200)

root.mainloop()
