import streamlit as st
from streamlit_image_comparison import image_comparison
import rasterio


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
st.set_page_config(page_title="Image-Comparison Example", layout="centered")

# Title
st.title("Hackathon Solution Showcase")

# Subtitle
st.subheader("Welcome to our Hackathon Solution Showcase")

# Description
st.write("This is where we present our innovative solution from the hackathon.")

# Add an image to showcase your solution (replace 'solution.png' with your image file)
st.image("image1.jpg", caption="Our Hackathon Solution", use_column_width=True)

# Description of the solution
st.write("Our solution solves the following problems:")

# List of problems solved
st.write("1. Problem 1 description here.")
st.write("2. Problem 2 description here.")
st.write("3. Problem 3 description here.")



# Features or key points
st.subheader("Key Features")
st.write("Our solution comes with the following key features:")

# List of key features
st.write("- Feature 1 description here.")
st.write("- Feature 2 description here.")
st.write("- Feature 3 description here.")

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




hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
