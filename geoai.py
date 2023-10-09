import streamlit as st
from streamlit_image_comparison import image_comparison
import rasterio
import os

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
uploaded_zip = st.file_uploader("Upload a ZIP file containing data:", type=["zip"])

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



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
