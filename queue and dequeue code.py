queue = [1, 2, 3, 4, 5]

maxSize = 5                                                                 # max length of the queue is 5 elements, queue starts out full

def dequeue():                                                              # function for dequeueing an element
    size = len(queue)
    if queue:
        dequeued_element = queue.pop(0)
        size = size - 1
        print(f"Dequeued element: {dequeued_element}")
    else:
        print("Queue is empty.")

    print(queue)

def enqueue(newItem):                                                       # function for queueing an element
    size = len(queue)
    if size == maxSize:
        print("Queue is full")
    else:
        user_int = int(input("Add to queue: "))
        size = size + 1
        queue.append(user_int)
        print("Queue:", queue)

while True:
    user_input = input("Enter something (type 'exit' to quit): ")           # takes a user input, either queue or dequeue
    if user_input.lower() == 'exit':
        print("Exiting loop.")                                              # entering exit stops the loop
        break
    else:
        print(f"You entered: {user_input}")
        if user_input.lower() == 'queue':
            enqueue(user_input)
        else:
            dequeue()