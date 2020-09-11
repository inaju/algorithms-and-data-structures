from deque import Deque

def pal_checker(word):
    d = Deque()
    
    for i in word:
        d.add_front(i)
    
    for i in range(len(d.show())):

        while d.size() != 1:
            print(d.size())
            rear = d.remove_rear()
            front = d.remove_front()

            if rear is front:
                print("it's a pan",rear, front )

            else:
                print("it's not a pan")



    return d.show()



pal_checker('madam')
