import fitz


def replace_colors(input_pdf, output_pdf, c1, c2, resolution=100):
    drawtotal = 100
    doc = fitz.open(input_pdf)
    for page in doc:
        for obj in page.get_drawings():
            i = 0
            start_point = None
            for item in obj['items']:
                if item[0] == 'l':  # Line object type
                    if i == 0:
                        start_point = fitz.Point(item[1].x, item[1].y)
                    i += 1
                    if i > resolution:
                        end_point = fitz.Point(item[2].x, item[2].y)
                        page.draw_line(start_point, end_point, c2)
                        i = 0
                        drawtotal -= 1
                if drawtotal == 0:
                    break
            if drawtotal == 0:
                break
        if drawtotal == 0:
            break



    doc.save("output.pdf")
    doc.close()

inputpdf = 'Career_Tree_v3.pdf'
outputpdf = 'output.pdf'
color1 = (1.0, 1.0, 1.0)
color2 = (0.0, 0.0, 0.0)

replace_colors(inputpdf, outputpdf, color1, color2)
