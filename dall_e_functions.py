from io import BytesIO
from PIL import Image
import openai

# Read the image file from disk and resize it


def open_image_resize(path, width, height):
    image = Image.open(path)
    image = image.resize((width, height))
    return image

# Convert the image to a BytesIO object


def byteISOconversion(image):
    byte_stream = BytesIO()
    image.save(byte_stream, format='PNG')
    byte_array = byte_stream.getvalue()
    return byte_array


# getting image using api call
def get_image(byte_array):

    try:
        response = openai.Image.create_variation(
            image=byte_array,
            n=1,
            size="1024x1024"
        )
        img_resp = response['data'][0]['url']
    except openai.error.OpenAIError as e:
        img_resp = (e.http_status, e.error)
    return img_resp
