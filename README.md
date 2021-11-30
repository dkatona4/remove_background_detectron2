### General
This tiny script let you to remove background around the object.

### Jupyter notebooks:
 - [bg-remove-original.ipynb](https://github.com/dkatona4/remove_background_detectron2/blob/main/bg-remove-original.ipynb)
	+ This scipt made by [DDemmer1](https://github.com/DDemmer1/ai-background-remove/commits?author=DDemmer1 "View all commits by DDemmer1")
 - [bg_remove-fast-latest.ipynb](https://github.com/dkatona4/remove_background_detectron2/blob/main/bg_remove-fast-latest.ipynb "bg_remove-fast-latest.ipynb")
	 +	Automatically creates folder structure if it necessary
	 +	Creates two files:
		 +	Masked image (the background color depends on definition)
		 +	Cropped image 
	+  Take only one object from each photos. The largest pixel area will be taken.
	+  Faster masking. The script uses matrix operations, which makes the code quite fast.


### How to use:
 - First you need to run the detectron2 algorihm
 - 
