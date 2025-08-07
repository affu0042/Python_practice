from PIL import Image      
# Import the Image module from Pillow to open and process images
from PIL.ExifTags import TAGS              
# Import TAGS to decode EXIF tag numbers into human-readable names


# Load the image (ensure the file exists and is correctly named)
image = Image.open("istockphoto-1268291803-612x612.webp")   
# Opens the image file using Pillow


# Print basic image information
print("Image Format:", image.format)       
# Displays the format of the image (e.g., JPEG, PNG, WEBP)
print("Image Size:", image.size)           
# Displays the dimensions (width, height) of the image in pixels
print("Image Mode:", image.mode)           
# Shows the color mode, e.g., RGB (color), L (grayscale)


# Check and extract EXIF metadata if available
if hasattr(image, "_getexif"):             
# Check if the image object has EXIF data support
    exif_data = image._getexif()           
# Extract EXIF metadata (returns a dictionary or None)


    if exif_data:                          
# If metadata is found
        print("\n📸 Metadata Found:")      
        for tag_id, value in exif_data.items():        
# Loop through all metadata tag ID and values
            tag_name = TAGS.get(tag_id, tag_id)        
# Convert tag ID to a readable name using TAGS dictionary
            print(f"{tag_name}: {value}")              
# Print each metadata tag name and its value
    else:
        print("⚠️ No metadata found.")     
# If _getexif() returned None (no metadata)
else:
    print("❌ This file does not have a valid image format or EXIF data.")  
# If image format doesn’t support EXIF
