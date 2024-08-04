#pip install PyMuPDF
import fitz

fileName = input("png로 변경할 pdf 이름 : ")

doc = fitz.open(fileName+".pdf")
for i, page in enumerate(doc):
    img = page.get_pixmap()
    img.save(f"./"+fileName+".png")