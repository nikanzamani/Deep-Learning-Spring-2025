from os import path,walk,chdir

def tester(DS_path="DataSet",P_path="Predictions",onlySecret=False):
    chdir(path.dirname(__file__))
    TC_files=[]
    for tc in [path.join(dirs[0],file) for dirs in 
               walk(DS_path if not onlySecret else path.join(DS_path,"secret")) for file in dirs[2]]:
        if tc.endswith("out") and path.isfile(tc):
            TC_files.append(path.splitext(tc)[0])
    tc_count=len(TC_files)
    avr_acc=0
    for idx,tc in enumerate(TC_files):
        print(f"{idx+1}/{tc_count} {tc}:",end=" ")
        acc=0
        try:
            with open(tc.replace(DS_path,P_path)+".predict","r") as f:
                propose=list(map(float,f.readline().split()))
        except Exception as e:
            print("runtime error ",e)
            continue
        with open(tc+".out","r") as f:
            answer=list(map(float,f.readline().split()))
        
        n=len(answer)
        for i in range(min(n,len(propose))):
            acc+=(1-abs(propose[i]-answer[i])/30)

        acc/=n

        avr_acc+=acc
        print(f"{acc*100}% accurate")

    print(f"average accuracy:{avr_acc/tc_count*100:.2f}%")
    return avr_acc/tc_count*100

if __name__=="__main__":
    tester()