import time
from fibonacci.fibonacci import fibonacci_normal, fibonacci_memoized
import memory_profiler

def test_function(func, inputs, trials=10):
    results = []
    for input in inputs:
      for _ in range(trials):
        mem_usage_before = memory_profiler.memory_usage()  # get memory usage at beginning 
        start_time = time.process_time()  # get start time
        result = func(input)
        cpu_time_used = time.process_time() - start_time  # calculate cpu time usage
        mem_usage_after = memory_profiler.memory_usage()  # get usage of memo after execution
        mem_used = mem_usage_after[0] - mem_usage_before[0]  # get memo usage
        duration = cpu_time_used
        results.append((input, result, duration, mem_used))
    return results


# def run_tests():
#     functions = {
#         "fibonacci_normal": fibonacci_normal,
#         "fibonacci_memoized": fibonacci_memoized
#     }
#     input_sizes = [100, 500, 1000]
#     for name, func in functions.items():
#         print(f"Testing {name}")
#         results = test_function(func, input_sizes)
#         for input_size, result, duration, mem_used in results:
#             print(f"Input: {input_size}, CPU Time: {duration:.6f}s, Memory Used: {mem_used:.6f} MiB")

def run_tests():
    functions = {
        "fibonacci_normal": fibonacci_normal,
        "fibonacci_memoized": fibonacci_memoized
    }
    input_sizes = [100, 500, 1000]
    filepath = '/home/jwmps/JWMPSExperiment/test_results.txt'
    with open(filepath, 'a') as file:  
        file.write("Test Results:\n")  
        for name, func in functions.items():
            file.write(f"Testing {name}\n")  
            results = test_function(func, input_sizes)
            for input_size, result, duration, mem_used in results:
                result_line = f"Input: {input_size}, CPU Time: {duration:.6f}s, Memory Used: {mem_used:.6f} MiB\n"
                file.write(result_line)  
                print(result_line)  

if __name__ == "__main__":
    run_tests()
