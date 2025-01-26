import cv2
import os
import numpy as np

def restore_decreased_brightness(image_path, output_dir, show_image=False):
    factor = 0.4  # fix decrease to 27%
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    restored_image = np.clip(image / factor, 0, 255).astype(np.uint8)
    
    output_path = os.path.join(output_dir, os.path.basename(image_path))
    cv2.imwrite(output_path, restored_image)
    print(f"Restored image saved to: {output_path}")
    
    if show_image:
        cv2.imshow("Restored Image", restored_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

restore_decreased_brightness("P:/Python programs/BNA-2025/src/Round1/dataset/val/images/IMG_5057.jpg", "P:/Python programs/BNA-2025/src/Round1/dataset", show_image=False)