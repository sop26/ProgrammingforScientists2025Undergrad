import multiprocessing
import time

def main():
    print("Parallel and concurrent programming in Python.")
    # by default, Python uses one core
    # serial programs on multiple cores cannot be parallel
    print("Number of cores", multiprocessing.cpu_count())
    sum_example_two_procs()
    timing_comparison_serial_vs_multi_procs()

def timing_comparison_serial_vs_multi_procs():
    n = 100
    data = list(range(1, n+1))
    num_procs = multiprocessing.cpu_count()
    
    start_parallel = time.time()
    sum_multi_procs(data, num_procs)
    end_parallel = time.time()
    total_parallel = end_parallel - start_parallel
    print(f"Sum of first{n} integers using {num_procs} processes is:{total_parallel}")
    
    start_serial = time.time()
    sum_serial(data, num_procs)
    end_serial = time.time()
    total_serial = end_serial - start_serial
    print(f"Sum of first{n} integers using {num_procs} processes is:{total_serial}")

def sum_example_two_procs():
    # Gauss example, first n integers
    n = 100
    data = list(range(1, n+1))
    # split data into two halves
    mid = len(data) // 2
    
    data_slices = [data[:mid], data[mid:]]
    
    # a queue is like an array/list, but it's going to be a safe structure for communications with parallel programming
    result_queue = multiprocessing.Queue()
    # ^queue object
    
    # create two processes
    # workers take function name and arguments
    p0 = multiprocessing.Process(target=partial_sum, args= (data_slices[0], result_queue))
    p1 = multiprocessing.Process(target=partial_sum, args= (data_slices[1], result_queue))
    # we just defined p0, p1 as process objects. Now run
    p0.start()
    p1.start()
    # it's also concurrent - also runs on one core
    
    # call join to wait for process to finish
    p0.join()
    # doesn't proceed until p0 finishes
    p1.join()
    
    # doesn't matter which finishes first. both done - both in the queue. if i cared about what got in first, i would need to put a value and label in queue
    # collect results from queue
    val_a = result_queue.get()
    val_b = result_queue.get()
    print("Sum of array elements is", val_a + val_b)

def sum_example_multiple_procs():
    # split prob into number of pieces equal to num processors available
    n = 100
    data = list(range(1, n+1))
    
    num_procs = multiprocessing.cpu_count
    total = sum_multi_procs(data, num_procs)
    
    print(f"Sum of first {n} integers using {num_procs} processes is: {total}")
    
def sum_multi_procs(data: list[int], num_procs: int) -> int:
    """
    Divides the work of summing all values in a list over num_procs concurrent (and hopefully parallel) processes
    """
    # divide data into equally sized chunks
    chunk_size = len(data) // num_procs
    run_off = len(data) % num_procs
    data_slices = []
    # for i in range(num_procs):
    #     start_index = i * chunk_size
    #     if run_off > 0:
    #         end_index = (i+1) * chunk_size + 1
    #         run_off -= 1
    #     else:
    #         end_index = (i+1) * chunk_size
    #     current_list = data[start_index: end_index]
    #     data_slices.append(current_list)
    
    data_slices = []
    for i in range(num_procs):
        start_index = i * chunk_size
        end_index = (i+1) * chunk_size + 1
        if i == num_procs - 1:
            end_index = len(data)   
        current_list = data[start_index: end_index]
        data_slices.append(current_list)
        
    result_queue = multiprocessing.Queue()
    processes = []
    for slice in data_slices:
        p = multiprocessing.Process(target = partial_sum, args = (slice, result_queue))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join() 
        
    total_sum = 0
    for _ in range(num_procs):
        total_sum += result_queue.get() 
    
    return total_sum

def sum_serial(data: list[int]) -> None:
    """
    Takes list of ints and a Queue. Puts the sum of the list into the Queue
    """
    # move to parallel programming, we no longer return values. we put them in a queue
    s = 0
    for elem in data:
        s += elem
    return s
    
def partial_sum(data_slice: list[int], result_queue: multiprocessing.Queue) -> None:
    """
    Takes list of ints and a Queue. Puts the sum of the list into the Queue
    """
    # move to parallel programming, we no longer return values. we put them in a queue
    val = sum(data_slice)
    result_queue.put(val)
       
if __name__ == "__main__":
    main()
