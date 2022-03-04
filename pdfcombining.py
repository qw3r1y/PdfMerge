from PyPDF2 import PdfFileMerger 

merge = PdfFileMerger()

fawn = open("Fawn.pdf", "rb")
meow = open("Meow.pdf", "rb")

merge.append(meow)
merge.append(fawn)
merge.write("Merge.pdf")