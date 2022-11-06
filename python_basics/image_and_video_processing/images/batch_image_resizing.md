# **Solution: Batch Image Resizing**
```py
import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
```
I first created a list containing the image file paths and then iterated through the aforementioned list.

The loop: reads each image, resizes, displays the image, waits for the user input key, closes the window once the key is pressed, and writes the resized image. The name of the resized image will be "resized" plus the existing file name of the original image.
<br>
<br>
### **Cv2 Documentation**<br>
Link [here](https://opencv.org/)

### **Glob Documentation**<br>
Link [here](https://docs.python.org/3/library/glob.html)