### General
This tiny script let you to remove background around the object.

### Jupyter notebooks:
 - [bg-remove-original.ipynb](https://github.com/dkatona4/remove_background_detectron2/blob/main/bg-remove-original.ipynb)
	+ This scipt made by [DDemmer1](https://github.com/DDemmer1/ai-background-remove "View codes by DDemmer1")
 - [bg_remove-fast-latest.ipynb](https://github.com/dkatona4/remove_background_detectron2/blob/main/bg_remove-fast-latest.ipynb "bg_remove-fast-latest.ipynb")
	 +	Automatically creates folder structure if it necessary
	 +	Creates two files:
		 +	Masked image (the background color depends on definition)
		 +	Cropped image 
	+  Take only one object from each photos. The largest pixel area will be taken.
	+  Faster masking. The script uses matrix operations, which makes the code quite fast.


### How to use:
 - First you need to install [ai-background-remove](https://github.com/DDemmer1/ai-background-remove) [written by DDemmer1]
 - Follow the installation steps

### Run the pretrained model

1. Copy your images with the objects to extract to ai-background-remove/input

2. Run the following network: 
(If you use a Python version **other than 3.7**. Make sure to change the version in the path )


```
python detectron2/demo.py --config-file detectron2/lib/python3.7/site-packages/detectron2/model_zoo/configs/COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml --input input/* --output output  --opts MODEL.DEVICE cpu MODEL.WEIGHTS detectron2://COCO-PanopticSegmentation/panoptic_fpn_R_101_3x/139514519/model_final_cafdb1.pkl
```

3. Detected objects are marked and a visualization is saved in your /output folder. 

### How to run:

1. Modify the parameters in [bg_remove-fast-latest.ipynb](https://github.com/dkatona4/remove_background_detectron2/blob/main/bg_remove-fast-latest.ipynb "bg_remove-fast-latest.ipynb")
