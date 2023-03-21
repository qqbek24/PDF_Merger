from tkinter import filedialog
from tkinter import *
from tkinterdnd2 import *
import tkinter.font as font
import pdf_Merge_def

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
    pdf_Merge_def.GoAndMerge(ListOfFiles, v_Destination, v_ResultFileName)

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

window.mainloop()
