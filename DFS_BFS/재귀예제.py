cnt=0

def recur():
    global cnt
    
    if cnt==5:
        return
    print('recursive')
    cnt+=1
    recur()
    

recur()