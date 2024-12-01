from television_gui import *

def main():
    window = Tk()
    window.title('Remote')
    window.geometry('240x240')
    window.resizable(True, True)
    Gui(window)
    window.mainloop()
if __name__ == '__main__':
    main()
