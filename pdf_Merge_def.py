import PyPDF2 

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



# FileList = [r'C:\Users\PL106539\OneDrive - Solar A S\Desktop\PDF_Merger_Files\1. a.pdf', r'C:\Users\PL106539\OneDrive - Solar A S\Desktop\PDF_Merger_Files\2. b.pdf']
# Start_Merging (FileList)
