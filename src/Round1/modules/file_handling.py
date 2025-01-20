import os, shutil, yaml, subprocess

def label_images():
    """ This function will launch LabelImg gui """
    # Command you want to run
    command = 'labelImg'

    # Run the command and simulate pressing Enter
    subprocess.run(command, shell=True)


def rename_files_in_folder(folder_path):
    """This function will rename all files in a folder from 1 onwards in the order they are sorted for intuitive ordering.

    Args:
        folder_path (string): The path to the folder containing the files to be renamed.
    """
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Sort files to ensure they are renamed in order
    files.sort()

    # Rename each file
    for index, file in enumerate(files, start=1):
        # Split the file name and extension
        file_name, file_extension = os.path.splitext(file)
        
        # Generate new file name
        new_name = f"{index}{file_extension}"
        
        # Construct full file paths
        old_file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)

def clear_folder(folder_path):
    """Helper function to clear all contents of a folder."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Remove subdirectories
            else:
                os.remove(file_path)  # Remove files
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
            
import os
import shutil

def split_raw_dataset(source_folder, train_folder, test_folder, train_ratio=0.8):
    """This function splits the dataset containing image and label pairs into training and testing datasets.
    It also moves images without corresponding label files and excludes non-image files like classes.txt.

    Args:
        source_folder (string): The path to the source folder containing the dataset (images and labels).
        train_folder (string): Path to the training folder.
        test_folder (string): Path to the testing folder.
        train_ratio (float, optional): The ratio of training to testing data. Defaults to 0.8.
    """
    # Define common image file extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    
    # Get a list of all image files with common extensions
    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(image_extensions)]
    print(f"Found {len(image_files)} image files in source folder: {source_folder}")

    # Sort the image files numerically based on their filenames (assuming filenames are like '1.jpg', '2.jpg', etc.)
    image_files.sort(key=lambda x: int(x.split('.')[0]))  # Sort based on numeric value of the filename
    print(f"Sorted image files: {image_files}")

    # Calculate the split index based on the ratio
    split_index = int(len(image_files) * train_ratio)
    print(f"Training set size: {split_index} images, Testing set size: {len(image_files) - split_index} images.")

    # Split the files into training and testing sets based on the order
    train_images = image_files[:split_index]
    test_images = image_files[split_index:]

    # Clear the contents of the training and testing folders
    if os.path.exists(train_folder):
        clear_folder(train_folder)
    if os.path.exists(test_folder):
        clear_folder(test_folder)
    
    # Create directories if they don't exist
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    print(f"Training folder created or exists: {train_folder}")
    print(f"Testing folder created or exists: {test_folder}")

    # Check for classes.txt and move it to the parent directory of the training folder
    if 'classes.txt' in os.listdir(source_folder):
        classes_file_path = os.path.join(source_folder, 'classes.txt')  # Correct source path
        parent_train_folder = os.path.dirname(train_folder)  # Get parent directory of the training folder
        shutil.copy(classes_file_path, os.path.join(parent_train_folder, 'classes.txt'))  # Copy to parent directory
        print(f"Moved classes.txt to {parent_train_folder}")

    # Copy images and corresponding labels to the training folder
    for image_file in train_images:
        label_file = image_file.rsplit('.', 1)[0] + '.txt'  # Replace image extension with .txt
        # Move the image to the training folder
        shutil.copy(os.path.join(source_folder, image_file), os.path.join(train_folder, image_file))
        print(f"Moved {image_file} to training folder.")
        
        # If label file exists, move it as well
        if os.path.exists(os.path.join(source_folder, label_file)):
            shutil.copy(os.path.join(source_folder, label_file), os.path.join(train_folder, label_file))
            print(f"Moved {label_file} to training folder.")
        else:
            print(f"Label file {label_file} not found for image {image_file}, skipping.")

    # Copy images and corresponding labels to the testing folder
    for image_file in test_images:
        label_file = image_file.rsplit('.', 1)[0] + '.txt'  # Replace image extension with .txt
        # Move the image to the testing folder
        shutil.copy(os.path.join(source_folder, image_file), os.path.join(test_folder, image_file))
        print(f"Moved {image_file} to testing folder.")
        
        # If label file exists, move it as well
        if os.path.exists(os.path.join(source_folder, label_file)):
            shutil.copy(os.path.join(source_folder, label_file), os.path.join(test_folder, label_file))
            print(f"Moved {label_file} to testing folder.")
        else:
            print(f"Label file {label_file} not found for image {image_file}, skipping.")
    
    print("Dataset split complete.")
    
def prepare_yaml(dataset_path, train_path, val_path, classes_file_path):
    # Path to the data.yaml file
    yaml_file_path = os.path.join(dataset_path, 'data.yaml')

    # Delete the old data.yaml if it exists (ignore if it doesn't exist)
    if os.path.exists(yaml_file_path):
        os.remove(yaml_file_path)
        print(f"Deleted old data.yaml at {yaml_file_path}")

    # Check if the classes.txt file exists
    if not os.path.exists(classes_file_path):
        print(f"Error: {classes_file_path} does not exist.")
        return

    # Read the classes from classes.txt
    with open(classes_file_path, 'r') as file:
        class_names = file.readlines()

    # Clean up class names (remove extra whitespace and newlines)
    class_names = [name.strip() for name in class_names]

    # Count the number of classes
    num_classes = len(class_names)

    # Prepare the YAML content in the correct order
    data_yaml = {
        'train': train_path,
        'val': val_path,
        'nc': num_classes,
        'names': {i: class_names[i] for i in range(num_classes)},
        'is_coco': False  # Set is_coco to false
    }

    # Save the new data.yaml file
    os.makedirs(dataset_path, exist_ok=True)  # Ensure the dataset_path exists
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.dump(data_yaml, yaml_file, default_flow_style=False, sort_keys=False)

    print(f"New data.yaml file created at {yaml_file_path}")
