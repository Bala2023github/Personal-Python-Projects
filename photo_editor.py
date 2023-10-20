from PIL import Image, ImageEnhance, ImageFilter
import os

img_path='./imgs'
edited_path = '/edited_imgs'

for image_file in os.listdir(img_path):

    image = Image.open(f"{img_path}/{image_file}")

    edit_1 = image.filter(ImageFilter.SHARPEN).convert('L')

    edit_2 = ImageEnhance.Contrast(edit_1)

    print(edit_2)

    edit_3 = edit_2.enhance(2)

    print(edit_3)
    
    edited_image = os.path.splitext(image_file)[0]

    edit_3.save(f'.{edited_path}/{edited_image}_edited.jpg')
