# from PIL import Image 

# image_path = "Fried noodle with chicken2.jpg"
# image_file =  Image.open(image_path)

# image_file.save ("Fried noodle with chicken.jpg", quailty=25)
import PIL 
import os
from PIL import Image

input_folder = "JPG"
output_folder = "JPG1"

def change_resolution():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            input_path = os.path.join(input_folder, filename)
            img = Image.open(input_path)
            resize_img = img.resize((1000,1000))
            output_path = os.path.join(output_folder,filename)
            resize_img.save(output_path,dpi=(100,100))

change_resolution()
