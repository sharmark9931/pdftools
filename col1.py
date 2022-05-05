from tkinter import *
from tkinter import filedialog
# import main

# all methods for col1
btnClicked = False

# methodCol1 = list(map(string, [compressPdf, pdfConverter, pdfScanner]))
# methodCol1 = ['compressPdf', 'pdfConverter', 'pdfScanner']

# print(type(methodCol1))
# print(methodCol1)

def compressPdf():
    print("compress pdf")
    btnClicked = True

    if btnClicked :
        btnClicked = False
        root = Tk()

        root.title('compress pdf')
        root.geometry('500x500')

        # all widgets goes below
        
        # Function for opening the
        # file explorer window
        def browseFiles():
            filename = filedialog.askopenfilename(initialdir = "/home/ravi", title = "Select a File", filetypes = (("all files", "*.*"), ("Text files", "*.txt*")))
            
            # Change label contents
            label_file_explorer.configure(text="File Opened: "+filename)
            

        #Set window background color
        root.config(background = "white")

        # Create a File Explorer label
        label_file_explorer = Label(root, text = "File Explorer using Tkinter", width = 100, height = 4, fg = "blue")

            
        button_explore = Button(root, text = "Browse Files", command = browseFiles)
        button_compressPdf = Button(root, text="Compress Pdf", command = implementCompressPdf)
        button_exit = Button(root, text = "Exit", command = exit)

        # Grid method is chosen for placing
        # the widgets at respective positions
        # in a table like structure by
        # specifying rows and columns
        label_file_explorer.grid(column = 1, row = 1)

        button_explore.grid(column = 1, row = 2)
        button_compressPdf.grid(column = 1, row = 3)
        button_exit.grid(column = 1,row = 4)

        root.mainloop()

    # btnClicked = False

def pdfConverter():
    print('pdf converter')

def pdfScanner():
    print('pdf scanner')


def implementCompressPdf():
    pass