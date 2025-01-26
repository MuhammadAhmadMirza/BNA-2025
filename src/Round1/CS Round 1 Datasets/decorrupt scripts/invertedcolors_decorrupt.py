import cv2
import os

def restore_colors(image_path, output_dir, show_image=False):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    restored_image = cv2.bitwise_not(image)
    
    output_path = os.path.join(output_dir, os.path.basename(image_path))
    cv2.imwrite(output_path, restored_image)
    print(f"Restored image saved to: {output_path}")
    
    if show_image:
        cv2.imshow("Restored Image", restored_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


restore_colors("P:/Python programs/BNA-2025/src/Round1/dataset/val/images/IMG_4972.jpg", "P:/Python programs/BNA-2025/src/Round1/dataset", show_image=False)