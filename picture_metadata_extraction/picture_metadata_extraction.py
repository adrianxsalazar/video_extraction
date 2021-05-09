import numpy as np
from PIL import Image
from PIL.ExifTags import TAGS
import argparse

#Arg to indicate the path
parser = argparse.ArgumentParser()
parser.add_argument('--image', type=str, default='image', help='initial image')
opt = parser.parse_args()

#path to the image or video
imagename = opt.image

#read the image data using PIL
image = Image.open(imagename)

#Get metadata of the video
exifdata = image.getexif()


for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)

    #print the metadata of the image
    print(f"{tag:25}: {data}")
