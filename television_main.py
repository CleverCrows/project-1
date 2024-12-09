from television_gui import *

def main() -> None:
    """
    Tkinter GUI creation.
    """
    window = Tk()
    window.title('Remote')
    window.geometry('300x350')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()
if __name__ == '__main__':
    main()
