
import os
import numpy as np


def get_train_list(path,trainPercentage=0.8):
    f = []
    l = []
    assert (os.path.isdir(path) == True),"path is not exist"
    for root,dirs,files in os.walk(path):
        for i in files:
            label = i.split('_')
            if label[-1] == 'OK.png':
                l.append('0')
            else:
                l.append('1')                    
            f.append(os.path.join(root,i))
    
    temp = np.array([f,l])
    temp=temp.transpose()
    np.random.shuffle(temp)
    f = list(temp[:,0])
    l = list(temp[:,1])
    trainList = 'train.txt'
    testList = 'test.txt'
    print('Total has %s'%len(f))
    trainLen = int(len(f)*trainPercentage)
    testLen = len(f)-trainLen
    print('Train set has %s'%trainLen)
    print('test set has %s'%testLen)
    
    with open(trainList,'w') as txt:
        for i in range(trainLen):
            txt.write(f[i]+'\t'+l[i]+'\n')
    with open(testList,'w') as txt:
        for i in range(testLen):
            txt.write(f[trainLen+i]+'\t'+l[trainLen+i]+'\n')
        



get_train_list("shuijingPatch01")
    
