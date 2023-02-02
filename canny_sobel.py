import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from matplotlib import pyplot as plt

def CannyEdgeDetection(image):
    global gray_image,blurred_image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    canny = cv2.Canny(blurred_image, 50, 200)
    return canny

def select_image():
    global image
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        image= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        messagebox.showinfo("Image selected", "Image has been successfully selected")

def SobelEdgeDetection(image):
    global sobel_x,sobel_y,gradient_magnitude
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(gray_image, (5,5), 0) 
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    sobel = cv2.Sobel(img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
    gradient_magnitude = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
    gradient_magnitude *= 255.0 / gradient_magnitude.max()
    #sobel = np.sqrt(np.power(sobel_x, 2) + np.power(sobel_y, 2))
    return sobel

def apply_canny():
    global image
    if image is None:
        messagebox.showerror("No Image", "Please select an image first")
        return
    canny_image = CannyEdgeDetection(image)
    #cv2.imshow('Canny Edge Detection', canny_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    plt.subplot(2,2,1),plt.imshow(image,cmap="Greys")
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(gray_image,cmap = 'gray')
    plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(blurred_image,cmap = 'gray')
    plt.title('Blurred Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(canny_image,cmap = 'gray')
    plt.title('Canny Edge Detection'), plt.xticks([]), plt.yticks([])
    
    plt.show()
    plt.suptitle("Canny Edge",fontsize=14)


def apply_sobel():
    global image
    if image is None:
        messagebox.showerror("No Image", "Please select an image first")
        return
    sobel_image = SobelEdgeDetection(image)
    #cv2.imshow('sobel Edge Detection', sobel_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    plt.subplot(2,3,1),plt.imshow(image,cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,2),plt.imshow(sobel_x,cmap = 'gray')
    plt.title('Sobel Edge Detection on the X axis'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,3),plt.imshow(sobel_y,cmap = 'gray')
    plt.title('Sobel Edge Detection on the Y axis'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,4),plt.imshow(gradient_magnitude,cmap = 'gray')
    plt.title('Gradient Magnitude'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,5),plt.imshow(sobel_image,cmap = 'gray')
    plt.title('Sobel Edge Detection on XY axis'), plt.xticks([]), plt.yticks([]) 
    plt.show()

def apply_canny_sobel():
    global image
    if image is None:
        messagebox.showerror("No Image", "Please select an image first")
        return
    canny_image = CannyEdgeDetection(image)
    sobel_image = SobelEdgeDetection(image)

    plt.subplot(1,3,1),plt.imshow(image,cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,3,2),plt.imshow(canny_image,cmap = 'gray')
    plt.title('Canny Edge Detection'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,3,3),plt.imshow(sobel_image,cmap = 'gray')
    plt.title('Sobel Edge Detection'), plt.xticks([]), plt.yticks([])

    plt.show()

root = tk.Tk()
root.title(" Edge Detection")
root.geometry("200x200")
root.maxsize(300, 300)
root.config(bg="skyblue")

image = None

select_image_button = tk.Button(root, text="Select Image", command=select_image)
apply_canny_button = tk.Button(root, text="Apply Canny", command=apply_canny)
apply_sobel_button = tk.Button(root, text="Apply Sobel", command=apply_sobel)
apply_canny_sobel_button = tk.Button(root, text="Apply Canny and Sobel", command=apply_canny_sobel)

action = tk.Button(root,text= " Quit ",command=root.quit)

select_image_button.place(x=60,y=10)
apply_canny_button.place(x=58,y=40)
apply_sobel_button.place(x=61,y=70)
apply_canny_sobel_button.place(x=35,y=100)
action.place(x=80,y=130)

root.mainloop()
