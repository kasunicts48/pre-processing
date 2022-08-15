import cv2
import glob
from skimage.filters import gaussian
from skimage import img_as_ubyte

path = "Dataset/*.*"
img_number = 1  


for file in glob.glob(path):
    print(file)    
    img= cv2.imread(file, 0)  
    
    smoothed_image = img_as_ubyte(gaussian(img, sigma=5, mode='constant', cval=0.0))
    
    cv2.imwrite("processedimg/smoothed_image"+str(img_number)+".jpg", smoothed_image)
    img_number +=1   