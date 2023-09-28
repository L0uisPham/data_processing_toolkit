import cv2
import numpy as np
import os

# Display an image
def show_image(image, title='image'):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Crop an image
def cropping(annotations, images, image_count):
    image_height, image_width, _ = images.shape
    for objects in range(annotations.shape[0]):
        x_center = annotations[:, 1]
        y_center = annotations[:, 2]
        width = annotations[:, 3]
        height = annotations[:, 4]

        x_min = int((x_center[objects] - width[objects] / 2) * image_width)
        y_min = int((y_center[objects] - height[objects] / 2) * image_height)
        x_max = int((x_center[objects] + width[objects] / 2) * image_width)
        y_max = int((y_center[objects] + height[objects] / 2) * image_height)

        cropped_image = images[y_min:y_max, x_min:x_max]
        output_dir = r"/home/kayos/Documents/segmentation/images"
        output_name = "cropped_image_" + str(image_count) + ".png"
        image_count += 1
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file = os.path.join(output_dir, output_name)
        try:
            cv2.imwrite(output_file, cropped_image)
            print(str(output_name) + " has been created!")
        except cv2.error as e:
            print(str(output_name) + " has failed!")
    return image_count

# Crop all images
def crop_all_images():
    image_path = "/home/kayos/Documents/segmentation/YOLODataset/images/"
    label_path = "/home/kayos/Documents/segmentation/YOLODataset/labels/"
    image_count = 0
    for image in os.listdir(image_path):
        for label in os.listdir(label_path):
            if os.path.splitext(str(image))[0] == os.path.splitext(str(label))[0]:    
                annotations_file = r""+label_path+str(label)
                image_file = r""+image_path+str(image)
                annotations = np.loadtxt(annotations_file, delimiter=" ")
                images = cv2.imread(image_file)
                print(str(image) + " is pairing with " + str(label) + "...")
                image_count = cropping(annotations, images, image_count)
    return

#Crop all the images and store them inside images folder
crop_all_images()





