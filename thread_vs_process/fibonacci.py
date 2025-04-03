import time
from threading import Thread
from multiprocessing import Process


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = 40 # we calculate the n-th fibonacci number
    m = 10 # repeat fibonacci numbers calculation m times

    # threading time
    start_time = time.perf_counter()
    threads = []
    for i in range(m):
        t = Thread(target=fibonacci, args=(n,))
        threads.append(t)
        t.start()
    for i in range(m):
        threads[i].join()
    threading_time = time.perf_counter() - start_time

    with open('artifacts/1.txt', 'a') as f:
        f.write("threading time = " + str(threading_time) + "\n")

    # synchronous launch
    start_time = time.perf_counter()
    for i in range(m):
        fibonacci(n)
    synchron_time = time.perf_counter() - start_time
    with open('artifacts/1.txt', 'a') as f:
        f.write("synchron time = " + str(synchron_time) + "\n")

    # multiprocessing time
    start_time = time.perf_counter()
    processes = []
    for i in range(m):
        p = Process(target=fibonacci, args=(n,))
        processes.append(p)
        p.start()
    for i in range(m):
        processes[i].join()
    multiprocessing_time = time.perf_counter() - start_time

    with open('artifacts/1.txt', 'a') as f:
        f.write("multiprocessing time = " + str(multiprocessing_time) + "\n")



if __name__ == "__main__":
    main()