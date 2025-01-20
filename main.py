from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
def create(file_name,date,ref,content,image_path,width,height,p_sign):
    pdf = canvas.Canvas(file_name, pagesize=letter)
    ratio = width / height
    pdf.drawInlineImage(image_path, 65, 650, width=width, height=height, preserveAspectRatio=ratio)
    pdf.drawString(75,670, "Dr. A. R. Ravikumar")
    pdf.drawString(75,655, "Principal")
    pdf.drawString(400,655, "Date:"+date)
    pdf.drawString(400,670, "Ref:"+ref)
    pdf.setFont("Helvetica-Bold",12)
    pdf.drawString(265,625,"CIRCULAR")
    pdf.setFont("Helvetica",12)
    text ="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+content
    styles = getSampleStyleSheet()
    text_object = Paragraph(text, styles["BodyText"])
    text_object.wrapOn(pdf,425,300)
    text_object.drawOn(pdf,85,575)
    pdf.drawString(75,500,"Copy to:")
    pdf.drawString(75,485,"All Dept. HODs,")
    pdf.drawString(75,470,"All faculties,")
    pdf.drawString(75,455,"All students of SIET")
    pdf.drawInlineImage(p_sign, 400, 480, width=70, height=25)
    pdf.drawString(410,465,"Principal")
    pdf.save()
if __name__ == "__main__":
    file_name=input("File name:")
    date=input("Date:")
    ref=input("Reference:")
    content=input("Content:")
    image_path = "D:\\Prithiv\\CircularBuilder\\srishakthi.png"
    principal_sign = "D:\\Prithiv\\CircularBuilder\\principalsign.png"
    width=500
    height=200
    create(file_name,date,ref,content,image_path,width,height,principal_sign)
    print(f"PDF '{file_name}' created successfully.")
