import math
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def part_integral(f, a, step, start, end):
    acc = 0
    for i in range(start, end):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, pool):
    acc = 0
    step = (b - a) / n_iter

    batch_size = n_iter // n_jobs

    with pool(max_workers=n_jobs) as executor:
        futures = []
        for i in range(n_jobs):
            start = i * batch_size
            end = min((i + 1) * batch_size, n_iter)
            future = executor.submit(part_integral, f, a, step, start, end)
            futures.append(future)
        for future in futures:
            acc += future.result()

    return acc


def main():
    cpu_num = multiprocessing.cpu_count()
    min_n_jobs = 1
    max_n_jobs = cpu_num * 2
    f = open('artifacts/2.txt', 'w')
    f.write("-" * 30 + "time with ThreadPoolExecutor" + "-" * 30 + "\n")
    for n_jobs in range(min_n_jobs, max_n_jobs + 1):
        start_time = time.perf_counter()
        ans = integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, pool=ThreadPoolExecutor)
        thread_time = time.perf_counter() - start_time
        f.write("n_jobs=" + str(n_jobs) + ": " + str(thread_time) + "\n")

    f.write("-" * 30 + "time with ProcessPoolExecutor" + "-" * 30 + "\n")
    for n_jobs in range(min_n_jobs, max_n_jobs + 1):
        start_time = time.perf_counter()
        ans = integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, pool=ProcessPoolExecutor)
        thread_time = time.perf_counter() - start_time
        f.write("n_jobs=" + str(n_jobs) + ": " + str(thread_time) + "\n")


if __name__ == "__main__":
    main()
