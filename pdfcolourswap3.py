import fitz
from PIL import Image
import io

def replace_colors(input_pdf, output_pdf, c1, c2, scale=2):
    doc = fitz.open(input_pdf)

    for page in doc:
        # Get the current page image with scaling
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale))
        image = Image.open(io.BytesIO(pix.tobytes("png")))

        # Convert colors to RGB tuples
        c1 = tuple(int(val * 255) for val in c1)
        c2 = tuple(int(val * 255) for val in c2)

        # Cycle through each pixel in the image
        for y in range(image.height):
            for x in range(image.width):
                current_color = image.getpixel((x, y))
                if current_color == c1:
                    image.putpixel((x, y), c2)
                elif current_color == c2:
                    image.putpixel((x, y), c1)

        # Save the image to a temporary file
        temp_image_path = "temp_image.png"
        image.save(temp_image_path)

        # Replace the page image with the modified one
        page.insert_image(page.rect, filename=temp_image_path)

    # Save the modified PDF
    doc.save(output_pdf)
    doc.close()

replace_colors("Career_Tree_v2.pdf", "output.pdf", (1.0, 1.0, 1.0), (0.0, 0.0, 0.0), scale=3)
