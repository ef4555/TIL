from collections import deque

queue = [0]*10
front = -1
rear = -1


def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data
    
def dequeue():
    global front
    front += 1
    return queue[front]   


rear += 1 # enqueue(1)
queue[rear] = 1
enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())

if front != rear:
    print(dequeue())
if front != rear:
    print(dequeue())
    
    
q1 = deque()
q1.append(100)
q1.append(200)
q1.append(300)
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())