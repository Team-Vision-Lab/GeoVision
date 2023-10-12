import streamlit as st
from streamlit_image_comparison import image_comparison
import rasterio
import os
from glob import glob
import pandas as pd
from streamlit_image_annotation import detection
import json
import cv2

# def geotiff_to_jpg(tif_filename):
#     with rasterio.open(tif_filename) as infile:
#         profile=infile.profile
        # change the driver name from GTiff to PNG
        # profile['driver']='PNG'
        # # pathlib makes it easy to add a new suffix to a
        # # filename
        # #    
        # png_filename=tif_filename.with_suffix('.png')
        # raster=infile.read()
        # with rasterio.open(png_filename, 'w', **profile) as dst:
        #     dst.write(raster)
        #
        # now do jpeg
        # profile['driver']='JPEG'
        # jpeg_filename=tif_filename.with_suffix('.jpeg')
        # with rasterio.open(jpeg_filename, 'w', **profile) as dst:
        #     dst.write(raster)

# set page config
st.set_page_config(page_title="GeoVision", layout="centered")

# Title
st.title("Geovision Showcase")

# Subtitle
st.subheader("Welcome to our Hackathon Solution Showcase for the NASA SpaceApps Hackathon")

st.subheader("Team: to the moon")

# Description
st.write("We developed a novel downstream task for land cover classification, utilizing HLS data from NASA Earthdata for various locations such as New York (USA), California (USA), Mumbai (India), Delhi (India), and Sundarbans (India). We manually annotated this geospatial data and used it to fine-tune a pre-trained model, Prithvi-100m, which served as our backbone. Our model achieved accurate land cover segmentation with minimal labeled data. Additionally, we applied our solution to assess landscape change detection in cities like New York and Mumbai, highlighting the rapid urban expansion. This platform showcases our results, provides intuitive before-and-after images of landscape changes over time, and allows researchers to upload their datasets for easy fine-tuning on Prithvi-100m. Our solution not only advances geospatial AI models but also empowers researchers to efficiently contribute to this field, making it an essential contribution to disaster response planning, environmental monitoring, and geospatial analytics.")

col1, col2 = st.columns(2)
# Original Image
with col1:
        st.image("original_image.jpg", caption="Original Image", use_column_width=True)
# Manually Annotated Segmented Mask
with col2:
        st.image("segmented_mask.jpg", caption="Manually Annotated Segmentation Mask", use_column_width=True)

# Description of the solution
#st.write("Our solution solves the following problems:")

# List of problems solved
#st.write("1. Problem 1 description here.")
#st.write("2. Problem 2 description here.")
#st.write("3. Problem 3 description here.")



# Features or key points
st.subheader("Key Features")
st.write("Our solution comes with the following key features:")

# List of key features
st.write("- Prithvi-100m foundational model fine-tuned for land cover classification")
st.write("- The platform allows users to observe before-and-after changes")
st.write("- The platform allows researchers to upload their annotated dataset and fine-tune the model achieving high accuracy with less data and time")

# convert a geotiff to jpg
dataset = rasterio.open('HLS.S30.T43QBB.2021352T054241.v2.0.B02.tif')



image_comparison(
    img1="2017.jpg",
    img2="2023.jpg",
    label1="2017 Mumbai",
    label2="2023 Mumbai",
    width=700,
    starting_position=50,
    show_labels=True,
    make_responsive=True,
    in_memory=True,
)
# Add a custom html footer
st.markdown(
    """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
    ,
    unsafe_allow_html=True,
)
def extract_zip(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall("uploaded_data")


# Allow users to upload a zip file
uploaded_zip = st.file_uploader("Upload a ZIP file containing dataset:", type=["zip"])

if uploaded_zip:
    # Check if a file is uploaded
    if st.button("Extract and Process"):
        st.write("Extracting the uploaded ZIP file...")
        extract_zip(uploaded_zip)
        st.write("ZIP file extracted successfully!")

        # Now you can access the extracted data and process it further as needed
        # For example, list the extracted files
        extracted_files = os.listdir("uploaded_data")
        st.write("Extracted files:", extracted_files)


label_list = ['black patch']
image_path_list = glob('images/*.jpg')
if 'result_dict' not in st.session_state:
    result_dict = {}
    for img in image_path_list:
        result_dict[img] = {'bboxes': [], 'labels': []}
    st.session_state['result_dict'] = result_dict.copy()

# with next and prev button to cycle through the images two columns
col1,_, col2 = st.columns(3)
with col1:
    prev_button = st.button('Previous')
with col2:
    next_button = st.button('Next')

if prev_button:
    if st.session_state['num_page'] > 0:
        st.session_state['num_page'] -= 1
elif next_button:
    if st.session_state['num_page'] < len(image_path_list) - 1:
        st.session_state['num_page'] += 1
else:
    if 'num_page' not in st.session_state:
        st.session_state['num_page'] = 0
    else:
        st.session_state['num_page'] = st.session_state['num_page']


num_page = st.session_state['num_page']

target_image_path = image_path_list[num_page]

new_labels = detection(image_path=target_image_path,
                    bboxes=st.session_state['result_dict'][target_image_path]['bboxes'], 
                    labels=st.session_state['result_dict'][target_image_path]['labels'], 
                    label_list=label_list, key=target_image_path)

if new_labels is not None:
    st.session_state['result_dict'][target_image_path]['bboxes'] = [v['bbox'] for v in new_labels]
    st.session_state['result_dict'][target_image_path]['labels'] = [v['label_id'] for v in new_labels]

# add a text box saying 'annotation completed for 1/2 images'
if st.session_state['num_page'] is not None:
    # blue color for the text box
    # Set the background color of the box to blue
    st.markdown(
    """
    <style>
    .blue-box {
        background-color: rgba(52, 152, 219, 0.3); /* Blue with 60% opacity */
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #6A87B3; /* Dark blue border */
        width: 60%; /* Set the width to 30% of the container */
    }
    </style>
    """,
    unsafe_allow_html=True
)

    # Create the blue-colored box with the text inside
    st.markdown('<div class="blue-box">❕Annotation completed for {}/{} images</div>'.format(num_page+1  , len(image_path_list)), unsafe_allow_html=True)

# space
st.write('')
annotation_json = st.session_state['result_dict']
# length of non-empty bboxes and labels in the annotation json 
count_file = 0
count_label = 0
for img in annotation_json:
    if len(annotation_json[img]['bboxes']) > 0 and len(annotation_json[img]['labels']) > 0:
        count_file += 1
        count_label += 1
    else:
        count_file += 1


# download button to the json file
if count_file == count_label:
    st.download_button(label='Download Annotation JSON', data=json.dumps(annotation_json), file_name='annotation.json', mime='application/json')
    # space
    st.write('')
    st.write('Output images generated ')




hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
