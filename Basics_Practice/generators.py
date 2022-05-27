# generators typically yield a subset right away
# lets run a generator to get subset lists of a master list
def row_generator(master_list, sub_list_size):  # defining generator function with a master list and sublist size
    curr = 0  # initialize traversing at zero
    while True: # while statement to keep yielding unlimited times
        yield master_list[curr:curr+sub_list_size]  # yield a sublist starting with current value and with sublist size
        curr += sub_list_size  # updating current value to the end of sublist


iters = row_generator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 3)
# iters is an instance of row_generator function object
# do not initiate it accidentally inside the below while loop as it can get re-initialized every iteration
while True:  # keep calling generator as long as return list has values
    curr_sub_list = next(iters)  # very important to assign this next to a variable and use that variable instead of calling next every time
    if curr_sub_list:  # non null sublist
        print(curr_sub_list)  # print current sublist, you can also append it to another master list
    else:  # null sublist returned
        break  # end the loop as we don't have any elements left

# you can call the yield directly from runtime using the following steps
# change directory to the location where this code is sitting
# type this command to access console for this code 'python -i generators.py'
# this will run the code and followed by opening of console
# console is now initiated with objects in the code, like row_generator() function
# enter code for generator initialization, example, 'a=row_generator([1,3,5,2,8],2)'
# once function is initialized, use next(a) to yield
# you can keep yielding as many times as you want
# once the list runs out of values, empty lists will be generated
