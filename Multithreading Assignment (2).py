#!/usr/bin/env python
# coding: utf-8

# Q-1 What is multiprocessing in python ? Why is it useful ?

# Ans-1 Multiprocessing is ability of a system to support more than one processor at the same time .
#  application in multiprogramming system are broken into smaller that run independently.
#  os alocate these threads to processors improving performance of system.
#  consider a computer system with a single processor . if it assigned saveral processes at same time, it will have to internal each task and switch breifly to another to keep all processess going .
#  this dituation id just like chef working in kitchen alone he has to do saveral task like baking ,stirring , kneading doughet
#  the more taks you do at once , the ,more difficult it gets to track them all , and keeping the timing right became more of chat
#  this is where the concept of multiprocessing arises.

# Q-2 What are the differences between multiprocessing and multithreading ?

# Ans-2  1. In multiprocessing cpu are added for increasing computer power and while in multithreading many threads are created of a single process process for increasing computer power.
# 2. In multiprocessing many processes are executed simultaneously , and while in multithreading many threads of process are executed simaltaneously.
# 3. multiprocessing  are classified into asymmetric and while in multithreading is not classified into any categorical.
# 4. multiprocessing  is time consuming process and process and process creation  are economical.
# 

# Q-3 Write a python code to create process using the multiprocessing module.

# In[1]:


import threading
def print_cube(num):
    print("cube:{}",format(num*num*num))
def print_square(num):
    print("square:{}",format(num*num))
    
if __name__=="__main__":
    t1=threading.Thread(target=print_square , args=(10,))
    t2=threading.Thread(target=print_cube, args=(10,))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")


# Q-4 What is a multiprocessing pool in python ? Why is it used ?

# Ans-5 Multiprocessing pool class allows you to create and manage process pools in python. A pool is responsible for fixed number       of processes . It controls when they are created , such as when they are needed . It also control what they should do when they are used such as making them wait. 

# In[ ]:




