# loading, displaying, resizing and creating images
import cv2

# loading an image
img=cv2.imread("python_course/python_basics/image_and_video_processing/images/galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

# resizing an image
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

# displaying an image
cv2.imshow("Galaxy",resized_image)

# creating an image
cv2.imwrite("python_course/python_basics/image_and_video_processing/images/galaxy_resized.jpg",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()