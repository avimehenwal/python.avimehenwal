#!/usr/bin/env python

# DATE      :   26-march-2014
# AUTHOR    :   Avi Mehenwal
# PURPOSE   :   Threading based on super class inheritance


import threading
import datetime


class Worker(threading.Thread):
    ''' Subclasses Worker from threading.Thread Class '''
    
    def __init__(self, name):        
        threading.Thread.__init__(self)
        self.name = name
        # can add more subclass attributes here

    def thread_function(self):
        for i in range(1000000):
            pass
        return 0
        
    def run(self):
        ''' Defines the block of code to be executes in notexplicitlly specified'''

        t1 = datetime.datetime.now()
        print "Starting Thread {%s} \n"%(self.name)
        self.thread_function()
        t2 = datetime.datetime.now()
        diff = t2 - t1
        print "Exiting Thread {%s} \t Time taken = %s\n"%(self.name,diff)


if __name__ == '__main__':
    threads = []
    no_of_threads = 10
    for i in range(no_of_threads):
        threads.append(Worker(i))
        # print "threads spawned and pushed to list queue but not yet started"
        

    for i in threads:
        # Tells threading to start ecexuting the thread function run()
        p = i.start()
        
                
    for i in threads:
        # Blocks the code until all threads are executed.
        i.join()


    
