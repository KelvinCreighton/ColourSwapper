import fitz


def replace_colors(input_pdf, output_pdf, c1, c2, resolution=1, width=1):
    drawtotal = 500
    doc = fitz.open(input_pdf)
    for page in doc:
        for obj in page.get_drawings():
            i = 0
            start_point = None
            for item in obj['items']:
                if drawtotal == 1:
                    print(obj)
                if item[0] == 'l':  # Line object type
                    if start_point == None:
                        start_point = fitz.Point(item[1].x, item[1].y)
                    i += 1
                    if i > resolution:
                        end_point = fitz.Point(item[2].x, item[2].y)
                        line_cap = obj.get('linecap', 0)
                        line_join = obj.get('lineJoin', 0)
                        dash_pattern = obj.get('dashes', None)
                        stroke_opacity = obj.get('stroke_opacity', 1.0)

                        page.draw_line(start_point, end_point, c2)
                        '''width=width or obj.get('width', 1),
                        lineCap=line_cap,
                        lineJoin=line_join,
                        dashes=dash_pattern,
                        stroke_opacity=stroke_opacity'''
                        #page.draw_line(start_point, end_point, c2, width=width)
                        start_point = end_point
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

#inputpdf = 'WindTunnel.pdf'
inputpdf = 'Career_Tree_v3.pdf'
outputpdf = 'output.pdf'
color1 = (1.0, 1.0, 1.0)
color2 = (1.0, 0.0, 1.0)

replace_colors(inputpdf, outputpdf, color1, color2, 0, 2)
