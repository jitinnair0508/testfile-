import cv2
import numpy as np
import natsort
import os


filelist=os.listdir(r'C:\Users\Dell\Desktop\Rectangle Detection\input')
for fichier in filelist[:]: 
    if not(fichier.endswith(".png")):
        filelist.remove(fichier)
finallist = natsort.natsorted(filelist,reverse=False)

counter = 0 




for counter in range(0, len(finallist)-1):

    imglist = finallist[counter]        
    img = cv2.imread(imglist,-1)

    cnts, hier = cv2.findContours(img[:,:,3], cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
    for c in cnts:    
        x,y,w,h = cv2.boundingRect(c)    
        region = img[y:y+h, x:x+w] 
        areabbox = h * w 
           
        counter = counter + 1

        n_black_pix = np.sum(region == 0)
        ratio = (n_black_pix/areabbox)

        if (ratio < 0.050):
            print("Image{} is Rectangle".format(counter))
            

               

            

    

    #print('Number of black pixels:', n_black_pix)
    #print(ratio)
    
    #cv2.rectangle(img, (x, y), (x+w, y+h), (200, 255, 0), 2)
    #cv2.imwrite("test.png", img)
    

