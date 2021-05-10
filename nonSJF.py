# Non Pre-emptive shortest job first schedualing method

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

def execute (to_draw_list,ind_list):
    start = 0
    end = 0
    total_time_so_far = 0
    total_waiting_time = 0
    
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()
    # Setting Y-axis limits
    gnt.set_ylim(0, 30)
    # Setting X-axis limits
    gnt.set_yticks([])
    #gnt.set_xlim(0, 150)  
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Time')
    # Setting graph attribute
    gnt.grid(False)
    # Declaring multiple bars in at same level and same width
    height=max(to_draw_list, key = lambda t: t[1])[1]
    
    # Drawing loop
    for i in range (len(to_draw_list)):
        if to_draw_list[i][0]<=total_time_so_far :
            start += end
        else:
            start=to_draw_list[i][0]
        end = to_draw_list[i][1]

        total_time_so_far=(start+end)
        gnt.broken_barh([(start,end)], (0, height),facecolors = ( random.uniform(0.09, 0.93) , random.uniform(0.09, 0.93) , random.uniform(0.09, 0.93)))
        gnt.annotate('P'+str(ind_list[ i ]) , ( start + to_draw_list[ i ][ 1 ] / 2 , height/2 ),horizontalalignment='center', verticalalignment='center', fontsize=15)
        total_waiting_time += (start - to_draw_list[i][0])
    
    gnt.set_xlim(0, total_time_so_far)
    gnt.set_ylim(0, height)
    plt.title("Average waiting time = " + str(total_waiting_time/len(to_draw_list) ) + " unit time" )
    plt.savefig("gantt1.png")
    image = mpimg.imread("gantt1.png")
    plt.imshow(image)
    plt.show()
    

def non_pre_epmtive_SJF(arrival_time,duration):

    waiting_list = []
    list_of_p = []
    current_pair = []
    to_draw_list = []
    ind_list = []
    consumed_time = 0

    for i in range (len(arrival_time)):
        list_of_p.append([arrival_time[i],duration[i]])
    
    temp = list_of_p.copy()
    
    consumed_time += min(list_of_p)[1] 
    to_draw_list.append(min(list_of_p))
    #execute(min(list_of_p),consumed_time)
    list_of_p.remove(min(list_of_p))

    while len(waiting_list) > 0 or len(list_of_p) > 0 :
        for i in range (len(list_of_p)):
            if list_of_p[i][0]<=consumed_time:
                waiting_list.append(list_of_p[i])

        if len(waiting_list) == 0:
            waiting_list.append(min(list_of_p))

        for i in range (len(waiting_list)):
            if waiting_list[i] in list_of_p :
                list_of_p.remove(waiting_list[i])

        current_pair = min(waiting_list, key = lambda t: t[1])
        consumed_time+=current_pair[1]
        to_draw_list.append(current_pair)
        #execute(current_pair,consumed_time)
        waiting_list.remove(current_pair)

    for i in range (len(to_draw_list)):
        ind_list.append(temp.index(to_draw_list[i])+1)
        temp[temp.index(to_draw_list[i])] = [0,0]
    execute(to_draw_list,ind_list)
