# -*- coding: UTF-8 -*-
import codecs
import numpy as np

def getdocword():
    phipath="F:/model/model-final.phi"
    phi_file = codecs.open(phipath,'r','utf-8')
    phi=[]
    try:
        for line in phi_file:
            arr=line.split()
            phi.append(arr)      
    finally:
        phi_file.close()
        
    thetapath="F:/model/model-final.theta"
    theta_file = codecs.open(thetapath,'r','utf-8')
    theta=[]
    try:
        for line in theta_file:
            arr=line.split()
            theta.append(arr)      
    finally:
        theta_file.close()
    m = len(theta)
    n = len(phi)
    for i in range(m):
        theta[i] = list(map(float, theta[i]))
    for j in range(n):
        phi[j] = list(map(float, phi[j]))
    docword = np.dot(theta, phi)
    # docword = []
    # newphi = np.transpose(phi)
    # v=len(newphi)
    # for i in range(m):
        # docword.append([0]*v)
        # for j in range(v):
            # docword[i][j] = np.dot(theta[i], newphi[j])
    # for i in range(m):
        # docword.append([0]*v)
        # doctopic = theta[i]
        # doctopicnum = len(doctopic)
        # for j in range(v): 
            # topicword = newphi[j]
            # topicwordnum = len(topicword)
            # for x in range(doctopicnum):
                # for y in range(topicwordnum):
                    # docword[i][j] = doctopic[x]*topicword[y]
    docwordpath="F:/model/docword.txt"
    docfile = codecs.open(docwordpath,'w','utf-8')
    m= len(docword)
    for i in range(m):
        n = len(docword[i])
        for j in range(n):
            docfile.write(str(docword[i][j]))
            docfile.write(' ')
        docfile.write('\n')
    docfile.close()

getdocword()