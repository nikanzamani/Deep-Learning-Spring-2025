import numpy as np
import random
from os import chdir,path
from answer import main

data_set_path="./DataSet/"
chdir(path.dirname(__file__))

def generate_one(file_path):
    n=random.randint(100,500)
    m=random.randint(50,n)
    k=random.randint(1,m//4)
    x=random.randint(m//10,m-k)
    inds=random.sample(range(m),k)
    PCs=np.random.uniform(-500,500,(n,k))
    coff=np.random.uniform(-10,10,k)
    last=np.dot(PCs[:,:-1],coff[:-1])+np.ones(n)*coff[-1]
    PCs[:,-1]=last
    vectors= np.dot(np.ones((n,1)),np.random.uniform(-500,500,(1,m))) 
    vectors[:,inds]=PCs
    noise=np.random.uniform(-5,5,(n,m))
    vectors+=noise
    vectors_str=[" ".join(map(str,row))+"\n" for row in vectors]
    with open(file_path+".in","w") as f:
        f.write(f"{n} {m} {x}\n")
        f.writelines(vectors_str)
    ans=main(n,m,x,vectors)
    ans_str=[" ".join(map(str,row))+"\n" for row in ans]

    with open(file_path+".out","w") as f:
        f.writelines(ans_str)   
def generate_all(public=3,secret=7):
    for i in range(public):
        file_path=path.join(data_set_path,"public",f"TC{i+1:02d}")
        generate_one(file_path)
    for i in range(secret):
        file_path=path.join(data_set_path,"secret",f"TC{i+1:02d}")
        generate_one(file_path)
 

if __name__=="__main__":
    generate_all()