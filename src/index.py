from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title('Yahtzee')
    window.geometry('450x450')
    window.resizable(0, 0)
    ui = UI(window)
    ui.start()

    window.mainloop()

if __name__ == '__main__':
    main()
