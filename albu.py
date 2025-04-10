import albumentations as A
import cv2

num_imgs = 0
Height = 123
Width = 133

output_path=data_path+'../'+'albued_aug_imset/'

# Resize and crop, is resize needed?
img_transform = A.compose([
    A.SmallestMaxSize(max_size=Width, p=1.0),
    A.RandomCenterCrop(height=Height, width=Width, p=1.0)
])

with open(data_path + 'labels.txt', 'r') as f:
    reader = csv.reader(f)
    lines = list(reader)
    num_imgs = len(lines)

aug_data_set = 0
# with open(output_path+'labels.txt', "w") as file:
# Reset the labels.txt file in the destination folder
open(output_path+'labels.txt', 'w').close()
for i,line in enumerate(lines):
    # read image
    im = cv2.imread(data_path+line[0]+'.png')
    im_label = line[1]

    # save base image to the destination folder
    cv2.imwrite(output_path+f"{aug_data_set}.png",im)
    with open(output_path+'labels.txt', 'a') as f:
        f.write(f"{aug_data_set}, {im_label}\n")
    aug_data_set += 1
    # make 5 more variations to the images
    for i in range(5):
        aug_data = img_transform(image=im)
        aug_img = aug_data['image']
        cv2.imwrite(output_path+f"{aug_data_set}.png",aug_img)
        with open(output_path+'labels.txt', 'a') as f:
            f.write(f"{aug_data_set}, {im_label}\n")
        aug_data_set += 1
