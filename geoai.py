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
st.title("GeoVision")

# Subtitle center aligned
st.subheader("Welcome to our Solution Showcase for the NASA Space Apps Challenge 2023")

# add a link to the team page Team: to the moon 🚀 with 15 font size
st.markdown('<p style="font-size:20px;"><b>Team: to the moon 🚀</b></p>', unsafe_allow_html=True)

st.markdown('<p style="font-size:25px;"><b>Solution Overview</b></p>', unsafe_allow_html=True)
# three list items
st.markdown('> - <u>**Innovative Land Cover Classification:**</u> Our solution is built on an inventive approach in order to use :orange[minimal training data]. We introduced a novel downstream task for :orange[land cover segmentation], using NASA Earthdata\'s HLS data for various locations such as New York (USA), California (USA), Mumbai (India), Delhi (India), and Sundarbans (India). We manually annotated this geospatial data and used it to fine-tune a pre-trained model, :orange[Prithvi-100m], which served as our backbone. Our model achieved accurate land cover segmentation with minimal labeled data.', unsafe_allow_html=True)

st.markdown('> - <u>**Landscape Change Detection for Environmental Awareness:**</u> Our solution is more than just classifying stuff. It\'s like :orange[eco-goggles for cities] like New York and Mumbai. We\'ve seen how they\'re growing fast, with skyscrapers everywhere. It\'s a reminder that we need to :orange[create and protect green spaces] while curbing city sprawl. Our platform shows you before-and-after pics to highlight how green areas are shrinking due to human actions, urging climate-conscious choices.', unsafe_allow_html=True)

st.markdown('> - <u>**Empowering Open Science and Collaborative Research:**</u> We didn\'t stop at creating a powerful AI tool; we aimed to make it accessible to all. Our platform lets researchers upload their geospatial datasets and annotate black patch areas, just like in the original [Prithvi-100M Model](https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M). This allows them to :orange[fine-tune their data] with the Prithvi-100m model, creating their :orange[own custom tasks]. In the Year of Open Science, we\'re changing the game in knowledge-sharing and making it :orange[easier for researchers to contribute] to disaster response planning, environmental monitoring, and geospatial analytics. It\'s a game-changer in how we conduct and share science.', unsafe_allow_html=True)

# subheader Land Cover segmentation 
st.markdown('<p style="font-size:25px;"><b>Land Cover Segmentation</b></p>', unsafe_allow_html=True)


st.markdown('- <u>**Data Curation and Creation:**</u> We gathered HLS geospatial data, comprising 8 images from different cityscapes and landscapes. These were manually annotated to create multi-class masks. Each original image was subdivided into 366x366 segments, expanding our dataset to 800 images.', unsafe_allow_html=True)


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
st.markdown('<p style="font-size:20px;"><b>Key Features</b></p>', unsafe_allow_html=True)
st.write("Our solution comes with the following key features:")

# List of key features
st.markdown("- :orange[Prithvi-100m] foundational model fine-tuned for land cover classification", unsafe_allow_html=True)
st.markdown("- The platform allows users to observe :orange[before-and-after changes]", unsafe_allow_html=True)
st.markdown("- Uses only :orange[8 images] in total", unsafe_allow_html=True)
st.write("- The platform allows researchers to :orange[upload their own dataset] to annotate and fine-tune the model achieving high accuracy with less data and time")


# Model output segmentated image subheading
st.markdown('<p style="font-size:20px;"><b>Land cover segmentation model output</b></p>', unsafe_allow_html=True)
st.warning('**Requires user interaction:** Use the slider on the image to view the model predicted multi-segmentation mask', icon="📜")

image_comparison(
    img1="2023.jpg",
    img2="overlay.png",
    label1="Mumbai",
    label2="Land Cover Segmented Output",
    width=700,
    starting_position=50,
    show_labels=True,
    make_responsive=True,
    in_memory=True,
)

st.markdown('<p style="font-size:25px;"><b>Landscape Change Detection for Environmental Awareness</b></p>', unsafe_allow_html=True)
st.markdown('Two images, Mumbai in 2017 and 2023, provide a clear visual of urban development over time. These side-by-side snapshots show the changes in the city, indicating the impact of human activity on green spaces and prompting a consideration of more environmentally conscious decisions.', unsafe_allow_html=True)

st.warning('**Requires user interaction:** Use the slider on the image to view before-and-after of the same landscape overtime', icon="📜")

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

st.markdown('<p style="font-size:25px;"><b>Empowering Open Science and Collaborative Research</b></p>', unsafe_allow_html=True)
st.markdown('<p style="font-size:20px;"><b>Upload your own dataset</b></p>', unsafe_allow_html=True)
st.warning('**OPTIONAL User interaction**', icon="📜")
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

st.markdown(
    """
    <style>
    .blue-box1 {
        background-color: rgba(128, 0, 128, 0.3); /* Blue with 60% opacity */
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #A98AA9; /* Dark blue border */
        width: 100%; /* Set the width to 30% of the container */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<p style="font-size:20px;"><b>Annotate your own dataset</b></p>', unsafe_allow_html=True)
# Create the blue-colored box with the text inside
st.markdown('<div class="blue-box1">❕Below Example dataset includes 2 images for demonstration purposes of the annotation feature.', unsafe_allow_html=True)
st.write('')
st.markdown('We offer a platform where you can annotate your own dataset with black patches similar to the Prithvi-100M model training approach. You can then use the annotated dataset to train your own models. We\'ll also provide you with the option to further train or infer using your models in the future.', unsafe_allow_html=True)

st.warning('**Requires User interaction: Create random rectangles on the image, and when you\'re done, click \'Complete\' to generate the output image with black patches. Click next for next image in the dataset**', icon="📜")

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
    st.write('Output images generated with black patches')
    # read the json and overlay it on the image
    col_1, co_l2 = st.columns(2)
    new_bounded_img = {}
    for img_name in annotation_json:
        bboxes = annotation_json[img_name]['bboxes']
        # make black patch for each bbox on the img
        # read the image
        img = cv2.imread(img_name)
        # loop over the bboxes
        for bbox in bboxes:
            # get the coordinates
            x, y, w, h = bbox
            # round 
            x1, y1, x2, y2 = int(x), int(y), int(x+w), int(y+h)
            # make the black patch
            img[y1:y2, x1:x2] = [0, 0, 0]
        # convert the image to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        new_bounded_img[img_name] = img

    # display the images
    # loop over the images in columns of 2
    for i in range(0, len(image_path_list), 2):
        # get the images
        img1 = new_bounded_img[image_path_list[i]]
        img2 = new_bounded_img[image_path_list[i+1]]
        # display the images
        with col_1:
            st.image(img1, caption='Image {}'.format(i+1), use_column_width=True)
        with co_l2:
            st.image(img2, caption='Image {}'.format(i+2), use_column_width=True)       
    st.markdown('<p style="font-size:25px;"><b>Model Training/Inference</b></p>', unsafe_allow_html=True)
    st.markdown('After completing the annotation process and preparing the dataset for model training, you have two options. We\'ll provide you with the choice of using either Amazon SageMaker to train your model using the annotated dataset you created above, or you can infer on test images from the model we will host in [huggingSpace](https://huggingface.co/spaces). This flexibility empowers you to select the approach that best suits your research needs', unsafe_allow_html=True)





hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
