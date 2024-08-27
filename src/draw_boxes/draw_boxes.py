from PIL import Image, ImageDraw
import io


def draw_bounding_boxes(image, boxes):
    imageStream = io.BytesIO(image)
    image = Image.open(imageStream)
    image = ImageDraw.Draw(image)
    for elt in boxes:
        box = elt['position']
        x, y, w, h = box['left'], box['top'], box['width'], box['height']
        shape = [x, y, x + w, y + h]
        image.rectangle(shape, fill=None, outline="red")
    return image._image
