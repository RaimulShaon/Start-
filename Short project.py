from PyPDF2 import PdfMerger
Allpdp = ["BIGD- CIPS Flyer- 21-09-16.pdf", "CV Of Raimul_Hasan.pdf"]
P1 = PdfMerger()

for Pdf in Allpdp:
    P1.append(Pdf)

P1.write("merged-pdf.NewPdf")
P1.close()