# Importing the modules needed for the program
import tkinter.filedialog
import tkinter as tk # for creating a graphical user interface
import PIL # for working with images
from PIL import ImageTk # for displaying images in tkinter
from PIL import Image, ImageFilter
from fastai.vision.all import * # for loading and using the classifier model
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Defining a function to load and preprocess an image from a file path
def load_image(file_path):
# Loading the image using PIL
    image = PIL.Image.open(file_path)
# Resizing the image to match the input shape of the classifier model (128 x 128 pixels)
# Converting the image to a fastai tensor image
    image = tensor(image)
# Normalizing the pixel values to be between -1 and 1
    
# Returning the preprocessed image
    return image

# Defining a function to predict if an image is yes or no using the classifier model
def predict_image(image):
# Loading the classifier model from a file using fastai load_learner method
    model = load_learner("export.pkl")
# Making a prediction using the model and the image
    prediction = model.predict(image)
# Getting the label of the prediction (yes or no)
# Returning the label
    return prediction

# Defining a function to upload an image from the user's computer and display it on the GUI
def upload_image():
# Asking the user to select an image file using tkinter file dialog
    file_path = tk.filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg *.png")])
# Checking if the user has selected a file or not
    if file_path:
# Loading and preprocessing the image using load_image function
        image = load_image(file_path)
# Predicting if the image is yes or no using predict_image function
        
        label,i,reliability = predict_image(image)
# Displaying the prediction on the GUI using tkinter label widget
        prediction_label.config(text=f"Prediction: {label}")
        reliability_label.config(text=f"reliability: {reliability[i]:.04f}%")
# Loading the original image using PIL
        original_image = PIL.Image.open(file_path)
# Resizing the original image to fit in the GUI (128 x 128 pixels)
        original_image = original_image.resize((264, 264))
# Converting the original image to tkinter compatible format using ImageTk
        tk_image = ImageTk.PhotoImage(original_image)
# Displaying the original image on the GUI using tkinter label widget
        image_label.config(image=tk_image)
        image_label.image = tk_image


# Creating a tkinter window for the GUI
window = tk.Tk()
window.title("Image Classifier")
window.geometry("400x400")

# Creating a tkinter button widget to upload an image
upload_button = tk.Button(window, text="Upload an image", command=upload_image)
upload_button.pack()

# Creating a tkinter label widget to display the prediction
prediction_label = tk.Label(window, text="Prediction: None")
prediction_label.pack()

# Creating a tkinter label widget to display the prediction
reliability_label = tk.Label(window, text="Reliability: None")
reliability_label.pack()

# Creating a tkinter label widget to display the original image
image_label = tk.Label(window, text="No image selected")
image_label.pack()

# Starting the main loop of the GUI
window.mainloop()

# End of program
