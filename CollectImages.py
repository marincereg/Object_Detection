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

LogCreator.SW_InRun()
LogCreator.Log_MSG("[CollectImages.py ] Software started " )
# Main Looop
ExitRequest = False
while ExitRequest == False:
    #Console HMI
    print(" Well hello lad, please pick one of the following :")  
    print(" For Creating New Label with images Press 1")
    print(" For Labeling Existing Images Press 2")
    print(" For Exit Press any other button ")
    Name = input("Enter your choice : ")
    # Iteration with user
    try:
        Case = int(Name)
    except:
        Case = 25
        LogCreator.Log_Warning("[CollectImages.py Line 24] Choice Entered is not valid - decimal,string or character inside Enter your choice")
    
    LogCreator.Log_MSG("[CollectImages.py ] User Choice Parametars : " + "InputChoice = " + str(Name))
    if Case == 1:
        print(" You pick Creating New Label with images ")
        LogCreator.Log_MSG("[CollectImages.py ] Creating New Label with images")
        LabelName = input("Please Insert Label Name : ")
        NumOfImg_Temp = input("Please insert number of images you want to take : ")
        
        LogCreator.Log_MSG("[CollectImages.py ] User Choice Parametars : " + "LabelName = " + LabelName + "  "+ "NumOfImg_Temp = " + NumOfImg_Temp)
        #Check input
        try:
            NumOfImg = int(NumOfImg_Temp)
            # exit if input is incorrect
            if NumOfImg < 1:
                Case = 25
                LogCreator.Log_Fault("[CollectImages.py Line 35 ] inserted number of images is invalid ! ")
        # exit if input is incorrect
        except:
            Case = 25
        
    elif Case == 2:
        print(" You pick Labeling Existing Images ")
        LogCreator.Log_MSG("[CollectImages.py ] Labeling Existing Images")
      
    else:
        print(" Later dude")
        LogCreator.Log_MSG("[CollectImages.py ] CLosing SW" )
        ExitRequest = True
    
    # Program Logic 
    if Case == 1:
        print("Collecting images for " + LabelName)
        IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')
        path = os.path.join(IMAGES_PATH, LabelName)
        if not os.path.exists(path):
            os.mkdir(path)  
            LogCreator.Log_MSG("[CollectImages.py Line 58 ] New Directory for collecting images created")
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
            LogCreator.Log_MSG("[CollectImages.py ] Image Taken : " + str(LabelName) + "  " + str(ImgCnt))
            
            time.sleep(3)
    
            if cv2.waitKey(1) & 0xFF == ord('q'):
                LogCreator.Log_MSG("[CollectImages.py Line 74 ] Image Collection aborted by User")
                break
        cap.release()
        cv2.destroyAllWindows()
        
    if Case == 2:
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
            LogCreator.Log_Fault("[CollectImages.py Line 82 ] Runing the labelImg.py unsucessfull - check library or labelimg\labelImg.py")
    
    """
    Will be present in SW part 2
    if Case == 3:
        TRAIN_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'train')
        TEST_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'test')
        LogCreator.Log_MSG("[CollectImages.py ] Creating Folders for test and train ")
        os.mkdir(TRAIN_PATH)
        os.mkdir(TEST_PATH)
        TrainTestPerct_Temp = input("Insert percentage of Train data : ")
        TrainTestPerct = float(TrainTestPerct_Temp)
        LogCreator.Log_MSG("[CollectImages.py ] Input by client : percentage of Train data = " +  str(TrainTestPerct_Temp))
    """   
    print ("\n")
