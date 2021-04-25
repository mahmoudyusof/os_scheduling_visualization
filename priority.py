import matplotlib
import matplotlib.pyplot as plt

class Process():
    def __init__(self, start, priority, duration, tid):
        self.tid = tid
        self.start = start
        self.priority = priority
        self.duration = duration
        self.wait = None
        self.actual_start = None
        self.break_points = []
        self.restarts = []

    def __lt__(self, other):
        return (self.start, self.priority, self.duration) < (other.start, other.priority, other.duration)

    def __gt__(self, other):
        return (self.start, self.priority, self.duration) > (other.start, other.priority, other.duration)

    def __eq__(self, other):
        return (self.start, self.priority, self.duration) == (other.start, other.priority, other.duration)

    def set_wait_and_actual_start(self, actual_start):
        self.actual_start = actual_start
        self.wait = actual_start - self.start

    def __repr__(self):
        return repr((self.start, self.priority, self.duration, self.tid))

    def calculate_total_waiting(self):
        wait = self.wait
        if len(self.break_points) != 0:
            for i in range(len(self.break_points)):
                wait += self.restarts[i] - self.break_points[0]
        return wait




def priority_non_preemptive(start_times, durations, priorities):
    combined = [Process(start_times[tid], priorities[tid], durations[tid], tid) for tid in range(len(start_times))]
    combined.sort(reverse=True)

    queue = []
    for i in range(len(combined)-1, -1, -1):
        if combined[i].start == 0:
            queue.append(combined.pop(i))
        else:
            break

    passed_time = 0
    final = []
    while True:
        queue.sort(key=lambda x: x.priority)
        if len(queue):
            task = queue.pop(0)
            task.set_wait_and_actual_start(passed_time)
            passed_time += task.duration
            for i in range(len(combined)-1, -1, -1):
                if combined[i].start <= passed_time:
                    queue.append(combined.pop(i))
            
            final.append(task)
        elif len(combined):
            passed_time += 1
            for i in range(len(combined)-1, -1, -1):
                if combined[i].start <= passed_time:
                    queue.append(combined.pop(i))
        else:
            break
    
    plt.figure(figsize=(15, 5))
    plt.ylim([-5, 10])

    waitings = []
    for task in final:
        waitings.append(task.calculate_total_waiting())

    plt.title("Average Waiting Time is: {}".format(sum(waitings)/ len(waitings)))

    cs = list(matplotlib.colors.get_named_colors_mapping())

    plt.broken_barh([(task.actual_start, task.duration) for task in final], (0, 5), facecolors=[cs[task.tid+task.tid**2] for task in final])

    for task in final:
        plt.text(
            x=task.actual_start + task.duration/2, 
            y=2.5,
            s=task.tid, 
            ha='center', 
            va='center',
            color='white',
            fontsize=15
        )


def priority_preemptive(start_times, durations, priorities):
    combined = [Process(start_times[tid], priorities[tid], durations[tid], tid) for tid in range(len(start_times))]
    combined.sort(reverse=True)

    queue = []
    for i in range(len(combined)-1, -1, -1):
        if combined[i].start == 0:
            queue.append(combined.pop(i))
        else:
            break
    passed_time = 0
    final = []
    task = None
    while True:
        for i in range(len(combined)-1, -1, -1):
            if combined[i].start <= passed_time:
                queue.append(combined.pop(i))
            else:
                break
        queue.sort(key=lambda x: x.priority)

        if len(queue):
            if task is None:
                task = queue.pop(0)
                task.set_wait_and_actual_start(passed_time)
                
                for i in range(len(combined)-1, -1, -1):
                    if combined[i].start <= passed_time:
                        queue.append(combined.pop(i))
                
            else:
                if max([task.actual_start,]+task.restarts ) + task.duration <= passed_time:
                    final.append(task)
                    task = queue.pop(0)
                    if task.actual_start is None:
                        task.set_wait_and_actual_start(passed_time)
                    elif len(task.break_points) > len(task.restarts):
                        task.restarts.append(passed_time)
                else:
                    if queue[0].priority < task.priority:
                        task.duration -= (passed_time - max([task.actual_start,]+task.restarts ))
                        task.break_points.append(passed_time)
                        tmp = task
                        task = queue[0]
                        queue[0] = tmp
                        if task.actual_start is None:
                            task.set_wait_and_actual_start(passed_time)
                        elif len(task.break_points) > len(task.restarts):
                            task.restarts.append(passed_time)

            passed_time += 1
                
        elif len(combined):
            passed_time += 1
            for i in range(len(combined)-1, -1, -1):
                if combined[i].start <= passed_time:
                    queue.append(combined.pop(i))
        else:
            if max([task.actual_start,]+task.restarts ) + task.duration <= passed_time:
                final.append(task)
                break
            else:
                passed_time += 1

    
    bars = []
    ids = []
    waiting_times = []

    for task in final:
        waiting_times.append(task.calculate_total_waiting())
        task.restarts.insert(0, task.actual_start)
        task.break_points.append(task.restarts[-1] + task.duration)
        task_broken_durations = [task.break_points[i] - task.restarts[i] for i in range(len(task.break_points))]
        bars += list(zip(task.restarts, task_broken_durations))
        ids += [task.tid for _ in range(len(task.break_points))]

    plt.figure(figsize=(30, 5))
    plt.ylim([-5, 5])
    plt.title("Average Waiting time is: {}".format(sum(waiting_times) / len(waiting_times)))

    cs = list(matplotlib.colors.get_named_colors_mapping())

    plt.broken_barh(bars, (-2.5, 5), facecolors=[cs[tid+tid**2] for tid in ids])

    for i, bar in enumerate(bars):
        plt.text(
            x=bar[0] + bar[1]/2, 
            y=0,
            s="P_" + str(ids[i]), 
            ha='center', 
            va='center',
            color='white',
            fontsize=15
        )
