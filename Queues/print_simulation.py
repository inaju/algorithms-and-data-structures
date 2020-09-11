import queue
import printer
import task
import random

def simulation(num_seconds, pages_per_minuite):
    printers=printer.Printer(200)
    printers.tick()
    print('after ticking')

    lab_printer =  printer.Printer(pages_per_minuite)
    print_queue = queue.Queue()
    waiting_times= []

    for current_second in range(num_seconds):
        if new_print_task():
            tasks = task.Task(current_second)
            print_queue.enqueue(tasks)
            print("this is the current task: ", print_queue.dequeue())
		

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            print("this is the new task ", next_task)
            
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)
            print("this is waiting time ", waiting_times)

            lab_printer.tick()
            

        average_wait = sum(waiting_times) / len(waiting_times)
        print("Average Wait %6.2f secs %3d tasks remaining." %
              (average_wait, print_queue.size()))
        print(waiting_times)

def new_print_task():
    num=random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

    

for i in range(1):
    simulation(3600, 20)
