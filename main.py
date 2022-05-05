# importing tkinter
from tkinter import *

import col1 as c1
import col2 as c2
import col3 as c3
import col4 as c4
import col5 as c5
import col6 as c6

# btnClicked = False

#creating root element
root = Tk()

# set title of window
root.title("PDFtools")

#setting windows size
root.geometry('1200x600')

# adding buttons
# ===================================================
col1 = ["Compress PDF", "PDF Converter", "PDF Scanner"]
i = 0
# methodCol1 = ["compressPdf", "pdfConverter", "pdfScanner"]
# btn1 = []
# for i in range(len(col1)):
#     btn1[i] = Button(root, text = col1[i], fg="blue", command = c1.methodCol1[i])
#     btn1[i].grid(column = 1, row = i*10)

btn11 = Button(root, text=col1[i], fg='blue', command=c1.compressPdf)
btn11.grid(column=1, row=i*10)
i += 1
btn12 = Button(root, text=col1[i], fg='blue', command=c1.pdfConverter)
btn12.grid(column=1, row=i*10)
i += 1
btn13 = Button(root, text=col1[i], fg='blue', command=c1.pdfScanner)
btn13.grid(column=1, row=i*10)
# =====================================================
col2 = ["Splite PDF", "Merge PDF"]
# for i in range(len(col2)):
#     btn2 = Button(root, text = col2[i], fg="blue")
#     btn2.grid(column = 10, row = i*10)
i = 0
btn21 = Button(root, text=col2[i], fg='blue', command=c2.splitePdf)
btn21.grid(column=10, row=i*10)
i += 1
btn22 = Button(root, text=col2[i], fg='blue', command=c2.mergePdf)
btn22.grid(column=10, row=i*10)
# ==========================================
col3 = ["Edit PDF", "PDF Reader", "Number Pages", "Delete PDF Pages", "Rotate PDF"]

# for i in range(len(col3)):
#     btn3 = Button(root, text = col3[i], fg="blue")
#     btn3.grid(column = 20, row = i*10)
i = 0
btn31 = Button(root, text=col3[i], fg='blue', command=c3.editPdf)
btn31.grid(column=20, row=i*10)
i += 1
btn32 = Button(root, text=col3[i], fg='blue', command=c3.pdfReader)
btn32.grid(column=20, row=i*10)
i += 1
btn32 = Button(root, text=col3[i], fg='blue', command=c3.numberPages)
btn32.grid(column=20, row=i*10)
i += 1
btn34 = Button(root, text=col3[i], fg='blue', command=c3.deletePdfPages)
btn34.grid(column=20, row=i*10)
i += 1
btn35 = Button(root, text=col3[i], fg='blue', command=c3.rotatePdf)
btn35.grid(column=20, row=i*10)
# =============================================
col4 = ["PDF to word", "PDF to excel", "PDF to PPT", "PDF to JPG"]
# for i in range(len(col4)):
#     btn4 = Button(root, text = col4[i], fg="blue")
#     btn4.grid(column = 30, row = i*10)
i=0
btn41 = Button(root, text=col4[i], fg='blue', command=c4.pdfToWord)
btn41.grid(column=30, row=i*10)
i += 1
btn42 = Button(root, text=col4[i], fg='blue', command=c4.pdfToExcel)
btn42.grid(column=30, row=i*10)
i += 1
btn43 = Button(root, text=col4[i], fg='blue', command=c4.pdfToPpt)
btn43.grid(column=30, row=i*10)
i += 1
btn44 = Button(root, text=col4[i], fg='blue', command=c4.pdfToJpg)
btn44.grid(column=30, row=i*10)
# =============================================
col5 = ["Word to PDF", "Excel to PDF", "PPT to PDF", "JPG to PDF"]
# for i in range(len(col5)):
#     btn4 = Button(root, text = col5[i], fg="blue")
#     btn4.grid(column = 40, row = i*10)
i=0
btn51 = Button(root, text=col5[i], fg='blue', command=c5.wordToPdf)
btn51.grid(column=40, row=i*10)
i += 1
btn52 = Button(root, text=col5[i], fg='blue', command=c5.excelToPdf)
btn52.grid(column=40, row=i*10)
i += 1
btn53 = Button(root, text=col5[i], fg='blue', command=c5.pptToPdf)
btn53.grid(column=40, row=i*10)
i += 1
btn54 = Button(root, text=col5[i], fg='blue', command=c5.jpgToPdf)
btn54.grid(column=40, row=i*10)
# =============================================
col6 = ["eSign PDF", "Unlock PDF", "Protect PDF"]
# for i in range(len(col6)):
#     btn4 = Button(root, text = col6[i], fg="blue")
#     btn4.grid(column = 50, row = i*10)

i=0
btn61 = Button(root, text=col6[i], fg='blue', command=c6.eSignPdf)
btn61.grid(column=50, row=i*10)
i += 1
btn62 = Button(root, text=col6[i], fg='blue', command=c6.unlockPdf)
btn62.grid(column=50, row=i*10)
i += 1
btn63 = Button(root, text=col6[i], fg='blue', command=c6.protectPdf)
btn63.grid(column=50, row=i*10)
i += 1













root.mainloop()