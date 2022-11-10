# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 17:39:18 2022

@author: marin
"""

#library Manager
import cv2 
import uuid
import os
import time
import LogCreator
import HMI

# Main Looop

def CollectImage (LabelName,NumOfImg):
    print("Collecting images for " + LabelName)
    LogCreator.Log_MSG("[CollectImages.py ] Start to collect image in " + str(LabelName))
    IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')
    path = os.path.join(IMAGES_PATH, LabelName)
    if not os.path.exists(path):
        os.mkdir(path)  
        LogCreator.Log_MSG("[CollectImages.py ] New Directory for collecting images created")
    print("Image Collecting is starting ...")      
    cap = cv2.VideoCapture(0)
    # Wait until cv2 is started and initialized
    time.sleep(5)
    for ImgCnt in range(0,NumOfImg):
        print("Collecting image no : " + str(ImgCnt + 1))
        ret, frame = cap.read()
    
        imgname = os.path.join(IMAGES_PATH,LabelName,LabelName+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        LogCreator.Log_MSG("[CollectImages.py ] Image Taken : " + str(LabelName) + "  " + str(ImgCnt+1) + " of "  + str(NumOfImg) )
        
        time.sleep(3)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            LogCreator.Log_MSG("[CollectImages.py ] Image Collection aborted by User")
            break
    cap.release()
    cv2.destroyAllWindows()
        
def StartLabelingApp ():
    #from "labelimg\labelImg.py" import labelImg.py
    try:
        import subprocess
        cmd = 'python labelimg\labelImg.py'
        
        LogCreator.Log_MSG("[CollectImages.py ] Opening Labeling.py")
        # python labelimg is sw downloaded from Github for labeling image 
        # Copyright (C) 2013  MIT, Computer Science and Artificial Intelligence Laboratory. Bryan Russell, Antonio Torralba, William T. Freeman
        #Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    except:
        print("Should log this - Fault in opening labeling app")
        LogCreator.Log_Fault("[CollectImages.py Line 50 ] Runing the labelImg.py unsucessfull - check library or labelimg\labelImg.py")
