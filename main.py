import os
import re
import piexif

directory = "/path/to/folder/with/photos"

jpegs = []

for root, dirs, files in os.walk(directory):
    for filename in files:
        jpegs.append(os.path.join(root, filename))

for jpg in jpegs:
    data = re.search('-(.*?)-' , jpg)
    x = data.group(1)
    year = x[0:4]
    month = x[4:6]
    day = x[6:8]
    newDate = year + ":" + month + ":" + day + " 12:00:00"

    exif_dict = piexif.load(jpg)
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = bytes(newDate, 'utf-8')
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, jpg)
