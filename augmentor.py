import os
import Augmentor

# Specify the path to the folder containing the original images
image_folder = "./original_image_directory/Argulus/"

# Check if the directory exists
if not os.path.isdir(image_folder):
    print(f"The directory '{image_folder}' does not exist.")
    exit()  # Exit the script if the directory does not exist

# Create an Augmentor pipeline with an output directory
output_directory = "/generated_Images"  # Specify the desired output directory
p = Augmentor.Pipeline(image_folder, output_directory=output_directory)

# Define augmentation operations
p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)

# Generate augmented images
p.sample(50)  # Generate 50 augmented samples for each original image

# Process the pipeline (apply augmentations to all images)
p.process()
