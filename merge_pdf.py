from PyPDF2 import PdfFileMerger

print("started")

pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf'] ##Dateien in dieser Reihenfolge 

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()

print("done")
print("look for result.pdf")
