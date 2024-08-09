import fitz  # PyMuPDF

def change_pdf_color(input_pdf, output_pdf, old_color, new_color):
    doc = fitz.open(input_pdf)
    for page in doc:
        for annot in page.annots():
            print(annot)
            '''
            if annot.type[0] == 8:  # Check if it's a highlight annotation
                # Replace color
                color = annot.info['color']
                #if color == old_color:
                annot.set_colors(stroke=new_color, fill=new_color)
                annot.update()'''
    #doc.save(output_pdf)

# Example usage
input_pdf = 'Career_Tree_v2.pdf'
output_pdf = 'output.pdf'
old_color = (1, 0, 0)  # RGB Red
new_color = (0, 1, 0)  # RGB Green
change_pdf_color(input_pdf, output_pdf, old_color, new_color)
