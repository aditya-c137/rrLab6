import albumentations as A
import cv2

Height = 123
Width = 133
modified_versions_to_save = 5

output_path=data_path+'../'+'albued_aug_imset/'

# Resize and crop, is resize needed?
img_transform = A.compose([
    A.SmallestMaxSize(max_size=Width, p=1.0),
    A.RandomCrop(height=Height, width=Width, p=1.0)
])

# get all image ids and their labels
with open(data_path + 'labels.txt', 'r') as f:
    reader = csv.reader(f)
    lines = list(reader)

# id counter for modified dataset
aug_data_set_id = 0
# Reset the labels.txt file in the destination folder
open(output_path+'labels.txt', 'w').close()
for i,line in enumerate(lines):
    # read image
    im = cv2.imread(data_path+line[0]+'.png')
    # read the label of the image
    im_label = line[1]

    # save base image to the destination folder
    cv2.imwrite(output_path+f"{aug_data_set_id}.png",im)
    with open(output_path+'labels.txt', 'a') as f:
        f.write(f"{aug_data_set_id}, {im_label}\n")
    aug_data_set_id += 1
    # make 5 more variations to the images
    for i in range(modified_versions_to_save):
        aug_data = img_transform(image=im)
        aug_img = aug_data['image']
        cv2.imwrite(output_path+f"{aug_data_set_id}.png",aug_img)
        with open(output_path+'labels.txt', 'a') as f:
            f.write(f"{aug_data_set_id}, {im_label}\n")
        aug_data_set_id += 1
