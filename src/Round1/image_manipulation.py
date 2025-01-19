"""This Document will contain all the functions necessary for image manipulation using Pillow and OpenCV"""

def invert_color(image_path, destination_path):
    """
    Image inversion is the process of changing the RGB values of a image by subtracting them from the maximum value(255) 
    for each channel. This will result in the image being 'inverted'

    Parameters:
        image_path (str): The file path to the input image.
        destination_path (str): The file path to save the inverted image.

    Returns:
        None
    """
    # Image inversion is the process of changing the RGB values of a image by subtracting them from the maximum value(255) for each 
    # channel. This will result in the image being 'inverted'
    from PIL import Image, ImageOps
    
    # Open the image
    inverted_image = Image.open(image_path)
    # Invert the image
    restored_image = ImageOps.invert(inverted_image)
    restored_image.save(destination_path)
    
def remove_random_noise(image_path, destination_path):
    """
    Removes random noise from an image using a median filter and saves the denoised image to the specified destination.
    Random noise refers to black or white pixels that appear on the screen, similar to old school TVs. This noise can occur due to 
    electromagnetic interference, damaged image sensors, or data corruption. The median filter removes this noise by changing the 
    value of a distorted pixel to the median value of the pixels around it.
    Args:
        image_path (str): The file path of the noisy image.
        destination_path (str): The file path where the denoised image will be saved.
    Returns:
        None
    """
    from PIL import Image
    import numpy as np, cv2

    # Open the image with noise
    noisy_image = Image.open(image_path)
    # Convert to NumPy array
    noisy_image_array = np.array(noisy_image)
    # Apply median filter to remove noise
    denoised_image_array = cv2.medianBlur(noisy_image_array, 3)
    # Convert back to PIL image
    denoised_image = Image.fromarray(denoised_image_array)
    # Save the denoised image
    denoised_image.save(destination_path)
    
def change_brightness(image_path, destination_path, brightness_factor):
    """
    Extreme Brightness levels can either make images too dim making dark parts equal or too bright causing overexposure
    and washing out of details. This function will adjust the brightness of an image by a specified factor.

    Parameters:
        image_path (str): The file path to the input image.
        destination_path (str): The file path to save the adjusted image.
        brightness_factor (float): A factor by which to adjust the brightness. 
                                Values > 1.0 increase brightness, 
                                values < 1.0 decrease brightness.

    Returns:
        None
    """
    from PIL import ImageEnhance, Image

    # Open the distorted image
    dim_image = Image.open(image_path)
    # Restore brightness
    enhancer = ImageEnhance.Brightness(dim_image)
    restored_image = enhancer.enhance(brightness_factor)
    restored_image.save(destination_path)
    
def fix_perspective(image_path, destination_path, resolution):
    """
    Corrects the perspective of a skewed image which is image that is stretches in a particular direction. This function will
    correct that transformation to make it match the specified resolution and aspect ratio.
    
    Args:
        image_path (str): The file path of the skewed image to be corrected.
        destination_path (str): The file path where the restored image will be saved.
        resolution (tuple, optional): The resolution (width, height) of the restored image. 
        
    Returns:
        None
    """
    import cv2, numpy as np
    
    # Read the skewed image
    skewed_image = cv2.imread(image_path)
    rows, cols, ch = skewed_image.shape
    # Define points for reverse perspective transformation
    src_points = np.float32([[50, 0], [cols - 50, 0], [0, rows - 1], [cols - 1, rows - 1]])
    # Calculate the aspect ratio of the destination resolution
    dst_width, dst_height = resolution
    dst_points = np.float32([[0, 0], [dst_width - 1, 0], [0, dst_height - 1], [dst_width - 1, dst_height - 1]])
    # Apply the reverse perspective warp
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    restored_image = cv2.warpPerspective(skewed_image, matrix, (dst_width, dst_height))

    # Save the restored image
    cv2.imwrite(destination_path, restored_image)
    
def crop_image(image_path, destination_path, crop_box):
    """
    Crops an image to a specified box and saves the cropped image to the specified destination.
    
    Parameters:
        image_path (str): The file path to the input image.
        destination_path (str): The file path to save the cropped image.
        crop_box (tuple): A tuple (left, upper, right, lower) defining the box to crop.
        
    Returns:
        None
    """
    from PIL import Image
    
    # Open the image
    image = Image.open(image_path)
    # Crop the image using the provided box
    cropped_image = image.crop(crop_box)
    # Save the cropped image
    cropped_image.save(destination_path)

def resize_image(image_path, destination_path, size):
    """
    Resizes an image to the specified size and saves the resized image to the specified destination.
    
    Parameters:
        image_path (str): The file path to the input image.
        destination_path (str): The file path to save the resized image.
        size (tuple): The desired size as (width, height).
        
    Returns:
        None
    """
    from PIL import Image
    
    # Open the image
    image = Image.open(image_path)
    # Resize the image
    resized_image = image.resize(size)
    # Save the resized image
    resized_image.save(destination_path)

def rotate_image(image_path, destination_path, angle):
    """
    Rotates an image by the specified angle and saves the rotated image to the specified destination.
    
    Parameters:
        image_path (str): The file path to the input image.
        destination_path (str): The file path to save the rotated image.
        angle (float): The angle in degrees to rotate the image.
        
    Returns:
        None
    """
    from PIL import Image
    
    # Open the image
    image = Image.open(image_path)
    # Rotate the image by the specified angle
    rotated_image = image.rotate(angle)
    # Save the rotated image
    rotated_image.save(destination_path)

def adjust_contrast(image_path, destination_path, contrast_factor):
    """
    Adjusts the contrast of an image by the specified factor and saves the adjusted image to the specified destination.
    
    Parameters:
        image_path (str): The file path to the input image.
        destination_path (str): The file path to save the adjusted image.
        contrast_factor (float): The factor by which to adjust the contrast. 
                                 Values > 1.0 increase contrast, values < 1.0 decrease contrast.
        
    Returns:
        None
    """
    from PIL import ImageEnhance, Image
    
    # Open the image
    image = Image.open(image_path)
    # Enhance the contrast of the image
    enhancer = ImageEnhance.Contrast(image)
    adjusted_image = enhancer.enhance(contrast_factor)
    # Save the adjusted image
    adjusted_image.save(destination_path)

def mirror_image(image_path, destination_path):
    """
    Mirrors an image horizontally and saves the mirrored image to the specified destination.
    
    Parameters:
        image_path (str): The file path to the input image.
        destination_path (str): The file path to save the mirrored image.
        
    Returns:
        None
    """
    from PIL import Image
    
    # Open the image
    image = Image.open(image_path)
    # Mirror the image horizontally
    mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    # Save the mirrored image
    mirrored_image.save(destination_path)

def convert_color_scheme(image_path, destination_path, color_mode):
    """
    Converts the color scheme of an image to the specified mode (e.g., 'RGB', 'L', 'CMYK') and saves the converted image.
    
    Parameters:
        image_path (str): The file path to the input image.
        destination_path (str): The file path to save the converted image.
        color_mode (str): The desired color mode ('RGB', 'L', 'CMYK', etc.).
        
    Returns:
        None
    """
    from PIL import Image
    
    # Open the image
    image = Image.open(image_path)
    # Convert the image to the specified color mode
    converted_image = image.convert(color_mode)
    # Save the converted image
    converted_image.save(destination_path)
