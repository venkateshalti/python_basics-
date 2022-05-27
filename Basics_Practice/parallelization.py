# In python, we achieve both multithreading and multiprocessing
# Lets understand the concepts of multithreading and multiprocessing below:
'''
A program is an executable file which consists of a set of instructions to perform some task and
is usually stored on the disk of your computer.

A process is what we call a program that has been loaded into memory along with all the resources
it needs to operate. It has its own memory space.

A thread is the unit of execution within a process. A process can have multiple threads running as
a part of it, where each thread uses the process’s memory space and shares it with other threads.

Multithreading is a technique where multiple threads are spawned by a process to do different tasks,
at about the same time, just one after the other. This gives you the illusion that the threads are
running in parallel, but they are actually run in a concurrent manner. In Python, the Global Interpreter Lock (GIL)
prevents the threads from running simultaneously.

Multiprocessing is a technique where parallelism in its truest form is achieved. Multiple processes are run
across multiple CPU cores, which do not share the resources among them. Each process can have many threads
running in its own memory space. In Python, each process has its own instance of Python interpreter doing
the job of executing the instructions.
'''
# simple delayed program without any multiprocessing or multithreading
# here, we are simulating IO bound calls with 10 second delay and CPU bound call with 200000000 iteration delay
import time, os  # time module has a delay method and OS has a process ID method
from threading import Thread, current_thread  # threading module implements multi threading
from multiprocessing import Process, current_process  # multiprocessing module implements multi processing

COUNT = 200000000  # iteration count to iterate over
SLEEP = 10  # sleep time for 10 seconds


def io_bound(sec):  # this function will call timer delay to simulate an IO calls delay
    pid = os.getpid()  # this will get current process ID
    threadName = current_thread().name  # name of current thread
    processName = current_process().name  # name of current process

    print(f"{pid} * {processName} * {threadName} \
        ---> Start sleeping...")  # printing thread and process details before time delay
    time.sleep(sec)  # waiting 10 seconds, this simulates a situation where IO operation is running for 10 seconds
    print(f"{pid} * {processName} * {threadName} \
        ---> Finished sleeping...")  # printing thread and process details before time delay


def cpu_bound(n):  # this function will call iteration delay to simulate a CPU overhead
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(f"{pid} * {processName} * {threadName} \
        ---> Start counting...")  # printing thread and process details before iteration delay

    while n > 0:  # running 200000000 iterations, this simulates a situation where CPU overhead is created
        n -= 1

    print(f"{pid} * {processName} * {threadName} \
        ---> Finished counting...")  # printing thread and process details after iteration delay


if __name__ == "__main__":
    # checking time of IO task/operation without multi threading
    start = time.time()  # start time
    io_bound(SLEEP)  # function call first time
    io_bound(SLEEP)  # function call 2nd time after first one ended
    end = time.time()  # end time
    print('Time taken in seconds -', end - start)  # time taken for sequential 'IO call' without threading

    # checking time of IO operation with multi threading
    start = time.time()  # start time
    t1 = Thread(target=io_bound, args=(SLEEP,))  # first thread instantiation with function name and arguments
    t2 = Thread(target=io_bound, args=(SLEEP,))  # second thread instantiation with function name and arguments
    t1.start()  # start first thread
    t2.start()  # start second thread without wait
    t1.join()  # t1 will complete first but wait for t2
    t2.join()  # t2 will complete and both t1 and t2 will together return
    end = time.time()  # end time
    print('Time taken in seconds -', end - start)  # time taken for IO call with multithreading is lesser than before
    # note that the time is lesser in the second case only because it's an IO operation without CPU overhead
    # the CPU idle time is efficiently used by calling another function instance in the same period

    # checking time of IO operation with multiprocessing(each process runs on each core, subject to availability)
    start = time.time()  # start time
    p1 = Process(target = io_bound, args =(SLEEP, ))  # first process instantiation with function name and arguments
    p2 = Process(target = io_bound, args =(SLEEP, ))  # second process instantiation with function name and arguments
    p1.start()  # start first process
    p2.start()  # start second process without wait
    p1.join()  # p1 will complete first but wait for p2
    p2.join()  # p2 will complete and both p1 and p2 will together return
    end = time.time()  # end time
    print('Time taken in seconds -', end - start)
    # time taken for IO call with multiprocessing is better than sequential but not as good as multithreading
    # this is because of separate initialization times and overheads on 2 different cores

    # checking time of CPU bound task/operation without multiprocessing or multi threading
    start = time.time()  # start time
    cpu_bound(COUNT)  # function call first time
    cpu_bound(COUNT)  # function call 2nd time after first one ended
    end = time.time()  # end time
    print('Time taken in seconds -', end - start)  # time taken for sequential 'CPU call'

    # checking time of CPU operation with multi threading instead of multiprocessing
    start = time.time()  # start time
    t1 = Thread(target=cpu_bound, args=(COUNT,))  # first thread instantiation with function name and arguments
    t2 = Thread(target=cpu_bound, args=(COUNT,))  # second thread instantiation with function name and arguments
    t1.start()  # start first thread
    t2.start()  # start second thread without wait
    t1.join()  # t1 will complete first but wait for t2
    t2.join()  # t2 will complete and both t1 and t2 will together return
    end = time.time()  # end time
    print('Time taken in seconds -', end - start)
    # time taken for CPU call with multithreading is more than before
    # this is because multithreading stopped the operations running on thread 1 to make way for thread 2
    # There is no CPU idle time in this case, hence control should come back to thread 1 after completing thread 2
    # and complete remaining iterations in thread 1 further slowing down whole operations

    # checking time of CPU operation with multiprocessing
    start = time.time()  # start time
    p1 = Process(target = cpu_bound, args =(COUNT, ))  # first process instantiation with function name and arguments
    p2 = Process(target = cpu_bound, args =(COUNT, ))  # second process instantiation with function name and arguments
    p1.start()  # start first process
    p2.start()  # start second process without wait
    p1.join()  # p1 will complete first but wait for p2
    p2.join()  # p2 will complete and both p1 and p2 will together return
    end = time.time()  # end time
    print('Time taken in seconds -', end - start)
    # time taken for CPU call with multiprocessing is better than both multithreading and sequential
    # this is because CPU load of each process is separately run on each core, this is not possible in multithreading

