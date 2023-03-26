# import base64

# your_code = base64.b64encode(b""")

import PyPDF2 
from tkinter import filedialog
from tkinter import *
from tkinterdnd2 import *
import tkinter.font as font

def GoAndMerge(ListToCheck, v_DestinationPath, v_ResultFileName):
    readylist = [r'%s' % fname for fname in ListToCheck]
    if len(readylist) >0: 
        Start_Merging(readylist, v_DestinationPath, v_ResultFileName)
        return True
    else: return False


def Start_Merging(File_Path_List, v_DestinationPath, v_ResultFileName):

    # Function - open file and loops through pages in that file
    def Loop_Pages_in_file (pdf_File_path, pdfWriter):

        # Open the file
        pdf2File = open(pdf_File_path, 'rb')
        # Read the file that you have opened
        pdf2Reader = PyPDF2.PdfReader(pdf2File)

        # Loop through all the pagenumbers for the document
        for pageNum in range(0,len(pdf2Reader.pages)):
            pageObj = pdf2Reader.pages[pageNum]
            pdfWriter.add_page(pageObj)

        pdf2File.close()
        
        return pdfWriter
    
    
    # Create a new PdfWriter object which represents a blank PDF document
    pdfWriter = PyPDF2.PdfWriter()

    for fname in File_Path_List:
        pdfWriter = Loop_Pages_in_file(fname, pdfWriter)

    # Now that you have copied all the pages from documents, write them into the new document
    # pdfOutputFile = open(r'C:\Users\PL106539\OneDrive - Solar A S\Desktop\PDF_Merger_Files\Merged_file\Merged_files.pdf', 'wb')
    v_DestPath = v_DestinationPath + '/' + v_ResultFileName + '.pdf'
    pdfOutputFile = open(r'%s' % v_DestPath, 'wb')

    pdfWriter.write(pdfOutputFile)
    
    # Close all the files - Created as well as opened
    pdfOutputFile.close()
   

# Function - splits string to file path list and insert to listbox
def path_listbox(event):
    strFiles = event.data
    #FinalList = strFiles.translate({ord(i): None for i in '{} '})
    strFiles = strFiles.replace('{','')
    filelist = strFiles.split('} ')

    for fname in filelist:
        fname = fname.replace('}','')
        if fname.endswith('.pdf'): 
            listbox.insert("end", fname)

# Button Merge function call
def Btn_Merge_Function():
    ListOfFiles = listbox.get(0,END)
    v_Destination = filedialog.askdirectory()
    v_ResultFileName = 'Merged_File'
    GoAndMerge(ListOfFiles, v_Destination, v_ResultFileName)

# Button Listbox Clear function call
def Btn_Clear_Function():
    listbox.delete(0,END)


# Setting the app window param
window = TkinterDnD.Tk()
window.title('simple PDF Merge tool')
window.geometry('760x360')
window.config(bg='white') # for blue use: '#145cb3'
frame = Frame(window)
frame.pack()

# Setting the ListBox
listbox = Listbox(
    frame,
    width=110,
    height=10,
    selectmode=SINGLE,
    )
listbox.pack(fill=X, side=LEFT, padx=5, pady=5)
listbox.drop_target_register(DND_FILES)
listbox.dnd_bind('<<Drop>>', path_listbox)

scrolbar= Scrollbar(
    frame,
    orient=VERTICAL
    )
scrolbar.pack(side=RIGHT, fill=Y)
# displays the content in listbox
listbox.configure(yscrollcommand=scrolbar.set)
# view the content vertically using scrollbar
scrolbar.config(command=listbox.yview)

# Setting Entry textbox
# EntryDestination = Entry(window, width=100)
# EntryDestination.pack(padx=5, pady=5)

# Setting the Buttons
buttonFont = font.Font(size=10, weight='bold')
buttonStart = Button(window, text='Merge PDF', width=40, height=3, bg='#1F618D', fg="white", font=buttonFont, command=Btn_Merge_Function)
buttonClear = Button(window, text='Clear file list', width=40, height=3, bg='#F7DC6F', font=buttonFont, command=Btn_Clear_Function)

buttonStart.pack(padx=5, pady=5)
buttonClear.pack(padx=5, pady=5)

# window.iconbitmap("icon.ico")
window.mainloop()

#""")

#exec(base64.b64decode(your_code))