import cv2
import os
import numpy as np

def reverse_perspective_warp(image_path, output_dir, show_image=False):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    rows, cols, _ = image.shape

    src_points = np.float32([
        [cols * 0.1, rows * 0.2],
        [cols * 0.9, rows * 0.1],
        [cols * 0.2, rows * 0.9],
        [cols * 0.8, rows * 0.8],
    ])

    dst_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])

    matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    restored_image = cv2.warpPerspective(image, matrix, (cols, rows))

    output_path = os.path.join(output_dir, os.path.basename(image_path))
    cv2.imwrite(output_path, restored_image)
    print(f"Restored image saved to: {output_path}")

    if show_image:
        cv2.imshow("Restored Image", restored_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


reverse_perspective_warp("D:\heic\ConvertedFiles\IMG_4922.jpg", "D:/heic/fixed", show_image=False)