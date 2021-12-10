#!/usr/bin/env python
# coding: utf-8

# In[2]:


import asyncio
import random


# In[8]:


def user_connection(username: str):
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"


def establish_connection(auth: bool = True):
    id = f"{random.randint(0,100000000):010}"

    if auth:
        yield f"auth {id}"

    yield from user_connection(id)

    if auth:
        yield f"disconnect {id}"
        
def connection():
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))

    while len(connections) > 0:
        connection = random.choice(connections)

        try:
            yield next(connection)
        except StopIteration:
            del connections[connections.index(connection)]
            
def write_to_file(file):
    message = yield
    file.write(message)

def connect_user(username):
    file = open(f'{username}.txt', 'w')
    message = yield
    yield from write_to_file(file)
    file.close()

    
for i in connection():
    print(i)

