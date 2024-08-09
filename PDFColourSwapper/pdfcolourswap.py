import fitz
from PIL import Image
import io

def hex_to_rgb(hex_colour):
    hex_colour = hex_colour.lstrip('#')
    return tuple(int(hex_colour[i:i+2], 16) for i in (0, 2, 4))

def swap_pdf_colours(input_pdf, output_pdf, c1, c2):
    #c1 = hex_to_rgb(c1)
    #c2 = hex_to_rgb(c2)

    # Open the PDF
    doc = fitz.open(input_pdf)

    for page in doc:
        for obj in page.get_drawings():
            if obj['fill'] is not None:
                obj['fill'] = (1, 1, 1)
        page.refresh
        '''if 'fill' in obj and obj['fill'] == (1.0, 1.0, 1.0):
            obj['fill'] = c2  # Set to new color
        elif 'fill' in obj and obj['fill'] == c2:
            obj['fill'] = c1  # Swap back to original color'''

    doc.save(output_pdf)
    doc.close()



#inputpdf = input('Type the name of your pdf: ')
#col1 = input('Input the first colour in hex starting with #: ')
#col2 = input('Input the second colour in hex starting with #: ')
inputpdf = 'Career_Tree_v2.pdf'
col1 = (0.0, 0.0, 0.0)
col2 = (1.0, 1.0, 1.0)
swap_pdf_colours(inputpdf, 'output.pdf', col1, col2)

'''

# Cycle through each page
    for i in range(doc.page_count):
        # Load the page
        page = doc.load_page(i)

        # Get the page dimensions
        page_width = int(page.rect.width)
        page_height = int(page.rect.height)

        # Get the current page image
        pix = page.get_pixmap()
        image = Image.open(io.BytesIO(pix.tobytes("png")))

        # Cycle through each pixel in the page
        for y in range(page_height):
            for x in range(page_width):
                # Get the current pixels colour
                current_colour = image.getpixel((x, y))
                # Check if the current pixels colour is either colour 1 or colour 2
                if (current_colour[0] == c1[0] and current_colour[2] == c1[2] and current_colour[2] == c1[2]):
                    image.putpixel((x, y), c2)  # If the pixels colour is colour 1 then set it to colour 2
                elif (current_colour[0] == c2[0] and current_colour[2] == c2[2] and current_colour[2] == c2[2]):
                    image.putpixel((x, y), c1)  # If the pixels colour is colour 2 then set it to colour 1

        # Save the image to a temporary file
        temp_image_path = "temp_image.png"
        image.save(temp_image_path)

        # Insert the image into the PDF page
        img_rect = fitz.Rect(0, 0, page_width, page_height)
        page.insert_image(img_rect, filename=temp_image_path)'''

    # Save the modified PDF
    #doc.save(output_pdf)
    #doc.close()


'''import fitz  # PyMuPDF

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

old_color = hex_to_rgb('#ff0000')
new_color = hex_to_rgb('#00ff00')

def replace_colors(input_pdf, output_pdf, old_color, new_color):
    doc = fitz.open(input_pdf)
    page = doc.load_page(0)
    doc = fitz.open(input_pdf)



    for page in doc:
        for obj in page.get_drawings():
            for item in obj["items"]:
                if isinstance(item, list):
                    for i, color in enumerate(item):
                        if isinstance(color, tuple) and len(color) == 3:
                            if color == old_color:
                                item[i] = new_color
    doc.save(output_pdf)

replace_colors("test.pdf", "output.pdf", old_color, new_color)
'''
