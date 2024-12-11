#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 20:01:45 2022

@author: gouiffes
"""
# librairies
import math
import time
import cv2
import numpy as np



def myResize(frame, scale_percent):
    my_h, my_w = frame.shape[0], frame.shape[1]
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    im = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    return(im)



""" Conversion espace couleur normalise rgb
    im : image codee en BGR
    r=R/(R+G+B)
    g=G/(R+G+B)
    b=B/(R+G+B)
     """
def myConvert(im):
    B= np.float32(im[:,:,0])
    G= np.float32(im[:,:,1])
    R= np.float32(im[:,:,2])
    den = np.float32(R+G+B+0.0001)
    imrgb=im #np.float32(im)

    imrgb[:,:,0]=np.uint8(255*cv2.divide(B, den))
    imrgb[:,:,1]=np.uint8(255*cv2.divide(G, den))
    imrgb[:,:,2]=np.uint8(255*cv2.divide(R, den))
    return(imrgb)



""" Mise en forme des donnees pour appliquer le kmeans
 renvoie :
     - une image de labels de classes 0, 1, 2...K-1
     - une images de K couleurs (1 couleur = 1 centre de classe)
     """
def myKmeans(im, k):
    couleurs = im.reshape((-1, 3))
    couleurs = np.float32(couleurs)
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 0.2)
    _, labels, centers = cv2.kmeans(couleurs, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)   
    imlabels=np.zeros( ( im.shape[0], im.shape[1]),  np.uint8)
    imlabels =np.uint8( labels.reshape(imlabels.shape))
    imclasses = (centers[labels.flatten()])
    imclasses = imclasses.reshape(im.shape)

    return(imlabels, imclasses, centers)

"""
type couleur renvoit un tableau de K valeurs indiquant la couleur de pièces : red, green, blue, yellow, other
"""
def display_nb_color(centers, tab_nb_regions):
    k=len(centers)
    for i in range(1, k):
        r=centers[i][2]
        g=centers[i][1]
        b=centers[i][0]
  
        if( r/b>1.5  and r/g>1.5) :
            col='rouge'
        elif(g/r>1.5 and g/b>1.5 ):
            col='verte'
        elif(b/r>1.5 and b/g>1.5 ):
            col='bleue'
        elif(g/b>1.5 and r/b>1.5):
            col='jaune'
        else :
            col='autre'
        print('Il y a ', tab_nb_regions[i-1]-1, 'pièce(s) de couleur', col)

