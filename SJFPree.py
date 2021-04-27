import matplotlib
import matplotlib.pyplot as plt
import copy

def SJFPRE():

    TaskList=[]
    WaitList=[]
    a=[0,1,2]
    d=[5,7,3]
    timeConsumed=0
    x=1
    for i in range(len(a)):
        TaskList.append([x,a[i],d[i]])
        x=x+1

    allTasks=copy.deepcopy(TaskList)
    cs = list(matplotlib.colors.get_named_colors_mapping())
    facecolors=[cs[x[0]] for x in TaskList]
    facecolors.append(cs[100])
    currentTask= min(TaskList, key = lambda t: t[1])
    TaskList.remove(currentTask)
    

    endDrawTimer=0
    startDrawTimer=0
    total_waiting_time=0
    prevTask=currentTask
    actualProcess=[]

    print(allTasks)
    while(len(TaskList)>0 or len(WaitList)>0 or currentTask[2]>0):
        print(currentTask)
        print(timeConsumed)
        timeConsumed=timeConsumed+1
        index=currentTask[0]
        endDrawTimer+=1
        currentTask[2]-=1
        WaitList+=[x for x in TaskList if x[1]<=timeConsumed]
        WaitList.append(currentTask)
        TaskList=[x for x in TaskList if x not in WaitList]
        WaitList=[x for x in WaitList if x[2]>0]
        plt.broken_barh([[timeConsumed-1,1]], (5, 5), facecolors =facecolors[currentTask[0]])
        if len(WaitList) == 0: 
            continue
        prevTask = currentTask
        currentTask= min(WaitList, key = lambda t: t[2])
        
        if currentTask[0] != index:
            if prevTask[2]==0:
                prevTask.append(timeConsumed)
                actualProcess.append(prevTask)
            #print("start =",startDrawTimer, " end = ",endDrawTimer)
            plt.annotate('P'+str(index) , (  (startDrawTimer + (startDrawTimer + endDrawTimer))/2 , 10-5/2 ),horizontalalignment='center', verticalalignment='center')
            endDrawTimer=0
            startDrawTimer=timeConsumed
        
        


        
        WaitList.remove(currentTask)

        if len(TaskList)== 0 and len(WaitList)== 0 and currentTask[2]==1:
            prevTask.append( timeConsumed+1)
            actualProcess.append(prevTask)
            
            if currentTask[0] == index:
                print("start =",startDrawTimer, " end = ",endDrawTimer)
                
                plt.annotate('P'+str(index) , ( (startDrawTimer + (startDrawTimer + endDrawTimer+1))/2 , 10-5/2 ),horizontalalignment='center', verticalalignment='center')
                endDrawTimer=0
                startDrawTimer+=timeConsumed

        
        
    waitingTime=0

    

    for x in actualProcess:
        x[2]=x[3]-x[1]

   
    for x,y in zip(actualProcess,allTasks):
        waitingTime+= x[2]-y[2]

    plt.title("Average waiting time = " + str(waitingTime/len(a) ) )
    print("waiting",waitingTime/len(a))
    plt.ylim(0, 15)
    plt.show()


SJFPRE()