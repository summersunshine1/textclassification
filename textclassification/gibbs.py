# -*- coding: UTF-8 -*-
import random

def updatetheme(k,alpha,beta,totalnm,totalnk,nm,nk,docindex,wordindex,v1):
    maxi=-1
    maxp=0
    for i in range(k):
        p=((nm[docindex][i]+alpha)/(totalnm[docindex]+k*alpha))*(nk[i][wordindex]+beta)/(totalnk[i]+v1*beta)
        if p>maxp:
            maxp=p
            maxi=i
    return maxi

def sampleperiod(totalnm,totalnk,nm,nk,w,alpha,beta,k,v,zarr,d):
    m=len(w)
    v1=len(v)

    for i in range(m):
        wordarr=w[i]
        n=len(wordarr)
        for j in range(n):
            if not w[i][j] in d:
                continue
            wordindex=d[w[i][j]]
            z=zarr[i][j]
            totalnm[i]-=1
            nm[i][z]-=1
            totalnk[z]-=1
            nk[z][wordindex]-=1
            #update
            zarr[i][j]=updatetheme(k,alpha,beta,totalnm,totalnk,nm,nk,i,wordindex,v1)
            z=zarr[i][j]
            totalnm[i]+=1
            nm[i][z]+=1
            totalnk[z]+=1
            nk[z][wordindex]+=1
    return nm,nk,totalnm,totalnk
    
def getfi(fi,beta,nk,totalnk,v,k):
    v1=len(v)
    for z in range(k):
        for wordindex in range(v1):
            fi[z][wordindex]= (nk[z][wordindex]+ beta)/(totalnk[z]+v1*beta)
    return fi

def gettheta(theta,alpha,nm,totalnm,w,k):
    m=len(w)
    for i in range(m):
        for z in range(k):
            theta[i][z]=(nm[i][z]+alpha)/(totalnm[i]+k*alpha)
    return theta

def gibbssample(w,alpha,beta,k,v,maxiter,epsino):#w document*word(m,n) alpha 1*k beta 1*size(v) k:topic number v:size of vocab
    m=len(w)
    v1=len(v)

    #initialize
    totalnm=[]
    totalnk=[]
    nm=[]
    nk=[]
    theta=[]
    fi=[]
    zarr=[]
    d=dict()
    print("begin init") 
    for i in range(m):
        totalnm.append(0)
        nm.append([0]*k)
        theta.append([0]*k)
        
        l=len(w[i])
        zarr.append([0]*l)
      
    for i in range(k):
        totalnk.append(0)
        nk.append([0]*v1)
        fi.append([0]*v1)
        
    for i in range(v1):#replace python index
        d[v[i]]=i
    print('initial params')
    for i in range(m):
        n=len(w[i])
        for j in range(n):
            if not w[i][j] in d:
                continue
            wordindex=d[w[i][j]]
            z=random.randint(0,k-1)
            totalnm[i]+=1;
            nm[i][z]+=1;
            totalnk[z]+=1;
            nk[z][wordindex]+=1;
            zarr[i][j]=z;

    print("begin sample period")      
    #sample period
    old_theta=0;
    old_fi=0;
    for i in range(maxiter):
        (nm,nk,totalnm,totalnk)=sampleperiod(totalnm,totalnk,nm,nk,w,alpha,beta,k,v,zarr,d);
        # if abs(theta-old_theta)<epsino && abs(fi-old_fi)<epsino
            # break;
        print("period end")
    
    theta=gettheta(theta,alpha,nm,totalnm,w,k)
    fi=getfi(fi,beta,nk,totalnk,v,k)
    return theta,fi

    


