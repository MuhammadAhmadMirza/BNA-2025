import cv2
import os
import numpy as np

def remove_random_noise(image_path, output_dir, show_image=False):
    noise_intensity = 0.6  # 60% of the image pixels were affected
    seed = 42
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    np.random.seed(seed)

    noise = np.random.choice([0, 255], size=image.shape, p=[1 - noise_intensity, noise_intensity]).astype(np.uint8)
    
    restored_image = cv2.subtract(image, noise)

    output_path = os.path.join(output_dir, os.path.basename(image_path))
    cv2.imwrite(output_path, restored_image)
    print(f"Restored image saved to: {output_path}")
    
    if show_image:
        cv2.imshow("Restored Image", restored_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


remove_random_noise("P:/Python programs/BNA-2025/src/Round1/dataset/train/images/IMG_4917.jpg", "P:/Python programs/BNA-2025/src/Round1/dataset", show_image=False)