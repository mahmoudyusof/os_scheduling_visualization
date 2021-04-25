# Importing the matplotlb.pyplot
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# Importing random
import random as rand
import math

##waiting time has some issue

def RR(p_a_time, p_duration, q_time):
    # process number
    process_number = len(p_a_time)


    # generate procces names list
    p_name = []
    for i in range(1 ,process_number + 1):
        p_name.append( 'P' + str( i ) )  



    # list of ( arrival time , duration , process name )
    list_of_p =[]
    for i in range (process_number):
            list_of_p.append([p_a_time[i], p_duration[i], p_name[i]])

    # sorting the list
    list_of_p.sort(key=lambda tup: tup[1])

    bar_width = list_of_p[process_number - 1][1]
    
    list_of_p.sort(key=lambda tup: tup[0])

    # print (list_of_p)

    # waiting time
    total_waiting_time = 0

    
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()
    
    # Setting Y-axis limits
    gnt.set_ylim(0, 30)
    
    # Setting X-axis limits
    xaxis = 200
    gnt.set_xlim(0, xaxis)

    
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Time')

    # Setting ticks on y-axis
    gnt.set_yticks([])

    # Drawing the gantt chart
    start_cursor = list_of_p[0][0] #setting the cursor
    x = 0
    color = [(rand.uniform(0.1, 0.9), rand.uniform(0.1, 0.9), rand.uniform(0.1, 0.9)) for _ in range(20)]
    # first_loop_finished = False
    while (1):
        # gnt.broken_barh([(start_cursor , q_time)], (0, bar_width), facecolors = ( (rand.uniform(0.1, 0.9), rand.uniform(0.1, 0.9), rand.uniform(0.1, 0.9) ) ) )
        # gnt.annotate(list_of_p[x][2], (start_cursor + q_time / 2, bar_width / 2), horizontalalignment = 'center', verticalalignment = 'center')
        # total_waiting_time += (start_cursor -  list_of_p[x][0]) 
        if (list_of_p[x][1] <= 0 and x == (process_number - 1)):
            break
        if (list_of_p[x][1] >= q_time and list_of_p[x][1] > 0):
            gnt.broken_barh([(start_cursor , q_time)], (0, bar_width), facecolors = ( color[x] ) )
            gnt.annotate(list_of_p[x][2], (start_cursor + q_time / 2, bar_width / 2), horizontalalignment = 'center', verticalalignment = 'center')
            if (list_of_p[x][1] > 0):
                start_cursor += q_time
        elif (list_of_p[x][1] < q_time and list_of_p[x][1] > 0):
            gnt.broken_barh([(start_cursor , list_of_p[x][1])], (0, bar_width), facecolors = ( color[x] ) )
            gnt.annotate(list_of_p[x][2], (start_cursor + list_of_p[x][1] / 2, bar_width / 2), horizontalalignment = 'center', verticalalignment = 'center')
            if (list_of_p[x][1] > 0):
                start_cursor += list_of_p[x][1]
            total_waiting_time += start_cursor - (list_of_p[x][0] + list_of_p[x][1])
        # if (not first_loop_finished):
        #     total_waiting_time += (start_cursor -  list_of_p[x][0])
        # else:
        #     total_waiting_time += list_of_p[x][1]
        list_of_p[x][1] -= q_time
        x += 1
        if (x > (process_number - 1)):
            x = 0
            # first_loop_finished = True
        # if (x < (process_number - 1)):
        #     if start_cursor < list_of_p[x + 1][0]:
        #         start_cursor = list_of_p[x + 1][0]
        
         
    gnt.set_xlim(0, start_cursor)  
    gnt.set_ylim(0, bar_width)           

    # showing average waiting time
    average_waiting_time = total_waiting_time / process_number
    # gnt.annotate("Average waiting time = " + str(average_waiting_time) , ( start_cursor / 2 , 20 ),horizontalalignment='center', verticalalignment='center')
    plt.title("Average waiting time = " + str(average_waiting_time) + " unit time")

    # showing the gantt chart
    plt.savefig("gantt1.png")
    image = mpimg.imread("gantt1.png")
    plt.imshow(image)
    plt.show()
    
# RR([0,2,4], [9,6,9], 4)