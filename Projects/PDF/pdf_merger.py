from PyPDF2 import PdfWriter

# simplest form

pdfWriterObj = PdfWriter()
pdfWriterObj.append("pdf1.pdf")
pdfWriterObj.append("pdf2.pdf")

pdfWriterObj.write("merged1and2.pdf")
pdfWriterObj.close()


# pdfs = ["pdf1.pdf", "pdf2.pdf", "pdf3.pdf"]
#
# # n = int(input("How many pdfs do you want to merge?\n"))
# #
# # for i in range(0, n):
# #     name = input(f"Enter the name of pdf {i+1}: ")
# #     pdfs.append(name)
#
# merger = PdfWriter()
# for pdf in pdfs:
#     merger.append(pdf)
#
# merger.write("merged-pdf.pdf")
# merger.close()