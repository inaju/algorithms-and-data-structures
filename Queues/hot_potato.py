from queue import Queue

def hot(names, num):
    name_queue = Queue()
    for name in names:
        name_queue.enqueue(name)

    print(name_queue.show())

    

    while name_queue.size() > 1:
        for i in range(num):
            name_queue.enqueue(name_queue.dequeue())
        
        name_queue.dequeue()
    print('done')

    return print(name_queue.dequeue())
    




hot(['tobi','mary','fola','kenose'], 4)
