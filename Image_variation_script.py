
from io import BytesIO
from PIL import Image
import openai
import os

# Add your Api keys here
# get them from https://beta.openai.com/docs/api-reference/authentication
openai.organization = organisation_id
openai.api_key = apikey
openai.Model.list()


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
    response = openai.Image.create_variation(
        image=byte_array,
        n=10,
        size="256x256"
    )
    img_resp = response['data'][0]['url']
    # try:
    #     response = openai.Image.create_variation(
    #         image=byte_array,
    #         n=1,
    #         size="1024x1024"
    #     )
    #     img_resp = response['data'][0]['url']
    # except openai.error.OpenAIError as e:
    #     img_resp = (e.http_status, e.error)
    return img_resp


def create_image(text):
    response = openai.Image.create(
        prompt=text,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']


# image = open_image_resize(
#     "Image_dataset/download.png", 256, 256)
# converted_image = byteISOconversion(image)
# image.show()

api_response = create_image("Turkish guy eating pork")

print(api_response)
