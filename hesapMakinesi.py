import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Hesap makinesi - Buse")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_16=tk.Button(root)
        GButton_16["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_16["font"] = ft
        GButton_16["fg"] = "#000000"
        GButton_16["justify"] = "center"
        GButton_16["text"] = "+"
        GButton_16.place(x=70,y=360,width=30,height=25)
        GButton_16["command"] = self.GButton_16_command

        GButton_919=tk.Button(root)
        GButton_919["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_919["font"] = ft
        GButton_919["fg"] = "#000000"
        GButton_919["justify"] = "center"
        GButton_919["text"] = "-"
        GButton_919.place(x=150,y=360,width=30,height=25)
        GButton_919["command"] = self.GButton_919_command

        GButton_848=tk.Button(root)
        GButton_848["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_848["font"] = ft
        GButton_848["fg"] = "#000000"
        GButton_848["justify"] = "center"
        GButton_848["text"] = "*"
        GButton_848.place(x=230,y=360,width=30,height=25)
        GButton_848["command"] = self.GButton_848_command

        GButton_569=tk.Button(root)
        GButton_569["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_569["font"] = ft
        GButton_569["fg"] = "#000000"
        GButton_569["justify"] = "center"
        GButton_569["text"] = "/"
        GButton_569.place(x=310,y=360,width=30,height=25)
        GButton_569["command"] = self.GButton_569_command

        GLineEdit_11=tk.Entry(root)
        GLineEdit_11["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_11["font"] = ft
        GLineEdit_11["fg"] = "#333333"
        GLineEdit_11["justify"] = "center"
        GLineEdit_11["text"] = "Entry1"
        GLineEdit_11.place(x=130,y=200,width=70,height=25)

        GLineEdit_785=tk.Entry(root)
        GLineEdit_785["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_785["font"] = ft
        GLineEdit_785["fg"] = "#333333"
        GLineEdit_785["justify"] = "center"
        GLineEdit_785["text"] = "Entry2"
        GLineEdit_785.place(x=240,y=200,width=70,height=25)

        GLabel_991=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_991["font"] = ft
        GLabel_991["fg"] = "#333333"
        GLabel_991["justify"] = "center"
        GLabel_991["text"] = "rakam2"
        GLabel_991.place(x=240,y=170,width=70,height=25)

        GLineEdit_953=tk.Entry(root)
        GLineEdit_953["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_953["font"] = ft
        GLineEdit_953["fg"] = "#333333"
        GLineEdit_953["justify"] = "center"
        GLineEdit_953["text"] = "Entry3"
        GLineEdit_953.place(x=350,y=200,width=70,height=25)

        GLabel_634=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_634["font"] = ft
        GLabel_634["fg"] = "#333333"
        GLabel_634["justify"] = "center"
        GLabel_634["text"] = "rakam1"
        GLabel_634.place(x=120,y=170,width=70,height=25)

        GLabel_609=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_609["font"] = ft
        GLabel_609["fg"] = "#333333"
        GLabel_609["justify"] = "center"
        GLabel_609["text"] = "rakam3"
        GLabel_609.place(x=350,y=170,width=70,height=25)

    def GButton_16_command(self):
        print("Buton 1'e basildi")


    def GButton_919_command(self):
        print("Buton 2'ye basildi")


    def GButton_848_command(self):
        print("Buton 3' basildi")


    def GButton_569_command(self):
        print("Buton 4'e basildi")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    textBoxYazilanlar1 = tk.StringVar()
    textBoxYazilanlar2 = tk.StringVar()
    textBoxYazilanlar3 = tk.StringVar()

    root.mainloop()
