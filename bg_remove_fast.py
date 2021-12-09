import pickle
import cv2
import os.path
from os import path as p
import matplotlib.pyplot as plt
import numpy as np

# The pathes will automatically completed according to horse names
base_crop_path = "/home/SSD_TEMP/raw_picture_check/crop/drone/"           
base_black_path = "/home/SSD_TEMP/raw_picture_check/black/drone/"

# Modify background color
background_color = (0,0,0,255)                                            # black

# Read filelist
def fileopen(filelist, horse_name):
    txt = open(filelist, "r")
    print(horse_name)
    for line in txt:
        rm_bg_and_save(line.strip(),horse_name)

# Util method to convert the detectron2 box format
def xyxy_to_xywh(box):
    x1 = int(box[0])
    y1 = int(box[1])
    x2 = int(box[2])
    y2 = int(box[3])
    w = x2-x1
    h = y2-y1
    return [x1,y1,w,h]

def rm_bg_and_save(FILE,horse_name):
#Initialize variables
    basic_crop_path = base_crop_path + horse_name 
    basic_black_path = base_black_path + horse_name
    with open(FILE, 'rb') as fi:
        results = pickle.load(fi)
    
    # Available classes
    classes = results['classes']
    # Choose the object types you want to extract e.g.: dog,horse etc...
    class_filter = ["horse"]
    background_color = (0,0,0,255)
    # Cut out masks
    print("Extracting objects...")
    index = 0
    for count,path in enumerate(results['instances']):   
    # Automatically create folders if not exist
        if count == 0 and (not p.exists(basic_crop_path) or not p.exists(basic_black_path)):
            print("Folders created: \n   - " + basic_crop_path + "\n   - " + basic_black_path)
            os.mkdir(basic_crop_path)
            os.mkdir(basic_black_path)
        tensor_array = results['instances'][path].pred_boxes.tensor.cpu().numpy()
        # Get the rectangle with the largest area
        counter = 0
        max_index = 0
        for i in tensor_array:
            area = (i[2]-i[0])*(i[3]-i[1])
            if counter == 0:
                max = area
                max_index = counter
            elif max < area:
                max = area
                max_index = counter
            counter+=1

        # Path definition
        filename = os.path.basename(path)
        
        # Mask definition
        mask = results['instances'][path].pred_masks[max_index]
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
        
        # Crop around the horse
        box = results['instances'][path].pred_boxes[max_index]
        box = box.tensor.cpu().numpy()[0]
        box = xyxy_to_xywh(box)
        original = img[box[1]:box[1]+box[3], box[0]:box[0]+box[2]]
        #crop_img_path = '/home/SSD_TEMP/raw_picture_check/crop/drone/' + horse_name + '/' + filename
        crop_img_path = base_crop_path + horse_name + '/' + filename
        cv2.imwrite(crop_img_path,original)
        print("CROP - Removed background from '" + path+"'. Saved object in '" + crop_img_path + "")
        
        # Set background color
        img[mask.cpu()!=True,:] = background_color
        
        # Cropping image to the size of the objects bounding box
        box = results['instances'][path].pred_boxes[max_index]
        box = box.tensor.cpu().numpy()[0]
        box = xyxy_to_xywh(box)
        img = img[box[1]:box[1]+box[3], box[0]:box[0]+box[2]]
        #new_img_path = '/home/SSD_TEMP/raw_picture_check/black/drone/' + horse_name + '/' + filename  
        new_img_path = base_black_path + horse_name + '/' + filename
        cv2.imwrite(new_img_path,img)
        print("BLACK - Removed background from '" + path+"'. Saved object in '" + new_img_path + "")
        
        index+=1

    print("Done...")        
        
# fileopen("/home/wildhorse_project/detectron_pic/pkl_lists/szazxszep.txt","szazxszep")   # 1
# fileopen("/home/wildhorse_project/detectron_pic/pkl_lists/thetisz.txt","thetisz")       # 2 
# fileopen("/home/wildhorse_project/detectron_pic/pkl_lists/panka.txt","panka")           # 3
