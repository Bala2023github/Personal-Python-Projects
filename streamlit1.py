import streamlit as st
import glob2


def load_images():
    image_files = glob2.glob("../imgs/*.jpg")
    # st.write(len(image_files))
    manuscripts = []
    for image_file in image_files:

        image_file = image_file.replace("../imgs\IMG","\IMG")
        parts = image_file.split("\\")
        # st.write(parts[1])
        if parts[1] not in manuscripts:
            manuscripts.append(parts[1])

    manuscripts.sort()    
    # st.write(manuscripts)
        # st.write(image_file)
    return image_files, manuscripts

st.title("Demo Image Grid Display")
image_files, manuscripts = load_images()

view_manuscripts = st.multiselect("Select manuscript(s)", manuscripts)
# st.write(view_images)

width = st.number_input("Select grid width : 1 to 5",1,5,3)

view_images = []

for image_file in image_files:
    if any(manuscript in image_file for manuscript in view_manuscripts):
        view_images.append(image_file)

# st.write(view_images)


groups = []

for i in range(0,len(view_images),width):
    groups.append(view_images[i:i+width])
st.write(groups)


for group in groups:
    cols = st.columns(width)
    for i, image_file in enumerate(groups):
        cols[i].image(image_file)
        # st.write(i,image_file)



# for view_image in view_images:



