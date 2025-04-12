import importlib
from os import path,walk,chdir
eps=1e-3

def tester(file_path="answer",DS_path="DataSet"):
    chdir(path.dirname(__file__))
    mod=importlib.import_module(file_path)
    TC_files=[]
    for tc in [path.join(dirs[0],file) for dirs in walk(DS_path) for file in dirs[2]]:
        if tc[-2:]=="in" and path.isfile(tc) and path.isfile(tc[:-2]+"out"):
            TC_files.append(".".join(tc.split(".")[:-1]))
    
    tc_count=len(TC_files)
    cnt=0
    for idx,tc in enumerate(TC_files):
        print(f"{idx+1}/{tc_count} {tc}:",end=" ")
        with open(tc+".in","r") as f:
            n,m,x=map(int,f.readline().split())
            vectors=[[float(x) for x in row.split()] for row in f.readlines()]
        try:
            propose=mod.main(n,m,x,vectors)
        except Exception as e:
            print("runtime error ",e)
            continue
        with open(tc+".out","r") as f:
            answer=[[float(x) for x in row.split()] for row in f.readlines()]
        correct=True
        for row in range(len(answer)):
            for cell in range(len(answer[0])):
                if abs(answer[row][cell]-propose[row][cell])>eps:
                    correct=False

        cnt+=correct
        print("Passed" if correct else "Failed")

    print(f"test cases passed: {cnt}/{tc_count} \nyour score:{cnt/tc_count*100:.2f}%")
    return cnt/tc_count*100
if __name__=="__main__":
    tester()