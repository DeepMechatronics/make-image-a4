from PIL import Image
import glob
import os
import numpy as np
import ntpath
cwd = os.getcwd() 
print("Current working directory:")
print()  
name=""
name_l=glob.glob(cwd+"/input/*.png")
print(name_l[1])


for x in name_l:
    print(x)
    im = Image.open(x)
    width, height = im.size    
    w_r=1   
    h_r=1.4142

    left = 0
    top = 0
    right = width
    bottom = 1.4142*width
    im1 = im.crop((left, top, right, bottom))
    im1.save(cwd+"/output/"+ntpath.basename(x))

