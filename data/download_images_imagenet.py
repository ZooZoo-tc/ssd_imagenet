import urllib.request
import os
from urllib.parse import urlparse
import string
import cv2

def store_raw_images():
    neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02773838'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 953
          
    for i in neg_image_urls.split('\n'):
        a = urlparse(i)
        filename = os.path.basename(a.path)
        filename = filename.replace('\r', '')
        filename = "n02773838/"+filename
        print(filename)
        try:
            # print(filename)
            urllib.request.urlretrieve(i, filename)
            img = cv2.imread(filename)
            # # should be larger than samples / pos pic (so we can place our image on it)
            # # resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite(filename,img)
            # pic_num += 1
            
        except Exception as e:
            print(str(e)) 

store_raw_images()            