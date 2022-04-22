
import os
from PyPDF2 import PdfFileMerger
input("Welcome to the PDF merger! \nTo merge pdf-s put them in the same folder as pdfMerger.py and press ENTER!")
#pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']
x = [a for a in os.listdir() if a.endswith(".pdf")]
merger = PdfFileMerger()
print("Merging files...")
if (len(x) < 2): 
    input("Nothing to merge!Press Enter to finish!")
else:
    for pdf in x:
        merger.append(open(pdf,'rb'))

    with open("Merged.pdf","wb") as fout:
        merger.write(fout)
        input("Merging complete! Press Enter to finish!")
    merger.close()