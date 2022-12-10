import cv2
import sys
import numpy as np
def floodfill(i,j,op2,vis,n,m,con=8):
    stack=[]
    pnts=[]
    stack.append((i,j))
    pnts.append((i,j))
    vis[i,j]=1
    dx=[(-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,1),(1,-1),(-1,-1)]
    if con!=8:
        dx=dx[:4]
    while len(stack)>0:
        ix,jy=stack[-1]
        stack.pop()
        for x in dx:
            if ix+x[0]>= 0 and ix+x[0]< n and jy+x[1]>= 0 and jy+x[1]< m and op2[ix+x[0],jy+x[1]]==255:
                if vis[ ix+x[0], jy+x[1] ]==0:
                    stack.append((ix+x[0],jy+x[1]))
                    pnts.append(((ix+x[0],jy+x[1])))
                    vis[ix+x[0],jy+x[1]]=1
    return pnts



#to run the script python3 1.py <imgpath>
# or just change the sys.argv[1] to <imgpath> in the code

def main():
    img= cv2.imread(sys.argv[1])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    vis=np.zeros(img.shape,dtype='int')
    n,m=img.shape
    boundingboxes=[]
    bdbxs=[]
    for i in range(n):
        for j in range(m):
            if vis[i,j]==0 and img[i,j]==255:
               bdbxs.append(floodfill(i,j,img,vis,n,m))
    
    for bxs in bdbxs:
        bds=np.array(bxs)
        minx=min(bds[:,0])
        maxx=max(bds[:,0])
        miny=min(bds[0,:])
        maxy=max(bds[0,:])
        w=maxx-minx+1
        h=maxy-miny+1
        if(h>10 and w>10):
            boundingboxes.append([(minx+maxx)//2,(miny+maxy)//2,w,h])
    
    print(boundingboxes)



if __name__ == "__main__":
    main()