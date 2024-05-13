import sys

deque = []

def push_front(x):
    deque.insert(0, x)

def push_back(x):
    deque.append(x)
    
def pop_back():
    if len(deque) == 0:
        return "-1"
    else:
        item = deque.pop()
        return str(item)
    
def pop_front():
    if len(deque) != 0:
        item = deque[0]
        del deque[0]
        return str(item)
    else:
        return "-1"
        
def size():
    return str(len(deque))

def empty():
    if size() == '0':
        return "1"
    else:
        return "0"

def front():
    if len(deque) == 0:
        return "-1"
    else:
        return str(deque[0])

def back():
    if len(deque) == 0:
        return "-1"
    else:
        return str(deque[-1])

N = int(sys.stdin.readline().rstrip())
commands = []
for i in range(N):
    commands.append(sys.stdin.readline().rstrip().split())

result = []
for command in commands:
    if command[0] == "push_back":
        push_back(int(command[1]))
    elif command[0] == "push_front":
        push_front(int(command[1]))
    elif command[0] == "pop_front":
        result.append(pop_front())
    elif command[0] == "pop_back":
        result.append(pop_back())
    elif command[0] == "size":
        result.append(size())
    elif command[0] == "empty":
        result.append(empty())
    elif command[0] == "front":
        result.append(front())
    elif command[0] == "back":
        result.append(back())

print('\n'.join(result))
