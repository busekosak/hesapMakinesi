import tkinter as tk
import tkinter.font as tkFont

class CalculatorApp:
    def __init__(self, root):
        # Setting window title
        root.title("Hesap Makinesi - Buse")
        # Setting window size
        width = 400
        height = 350
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Entry fields for user input
        self.entry1 = tk.Entry(root, font=("Times", 14), justify="center")
        self.entry1.place(x=130, y=50, width=150, height=30)

        self.entry2 = tk.Entry(root, font=("Times", 14), justify="center")
        self.entry2.place(x=130, y=100, width=150, height=30)

        # Output display for result
        self.result_label = tk.Label(root, text="Sonuç: ", font=("Times", 14), justify="center")
        self.result_label.place(x=130, y=230, width=150, height=30)

        # Buttons for operations
        self.create_button(root, "+", 50, 150, self.add)
        self.create_button(root, "-", 120, 150, self.subtract)
        self.create_button(root, "*", 190, 150, self.multiply)
        self.create_button(root, "/", 260, 150, self.divide)

    def create_button(self, root, text, x, y, command):
        button = tk.Button(root, text=text, bg="#f0f0f0", font=("Times", 14), fg="#000000", justify="center", command=command)
        button.place(x=x, y=y, width=50, height=50)

    def add(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = num1 + num2
            self.result_label.config(text=f"Sonuç: {result}")
        except ValueError:
            self.result_label.config(text="Geçersiz giriş")

    def subtract(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = num1 - num2
            self.result_label.config(text=f"Sonuç: {result}")
        except ValueError:
            self.result_label.config(text="Geçersiz giriş")

    def multiply(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = num1 * num2
            self.result_label.config(text=f"Sonuç: {result}")
        except ValueError:
            self.result_label.config(text="Geçersiz giriş")

    def divide(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            if num2 == 0:
                self.result_label.config(text="Sıfıra bölme hatası")
            else:
                result = num1 / num2
                self.result_label.config(text=f"Sonuç: {result}")
        except ValueError:
            self.result_label.config(text="Geçersiz giriş")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
