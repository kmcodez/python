# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for thread
#                   multiprocessing = better for cpu tasks (heavy cpu usages)
#                   multithreading = better for  bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


# def main():
#     print(cpu_count())
#     start_time = time.perf_counter()
#     a = Process(target=counter, args=(125000000,))
#     b = Process(target=counter, args=(125000000,))
#     c = Process(target=counter, args=(125000000,))
#     d = Process(target=counter, args=(125000000,))
#     e = Process(target=counter, args=(125000000,))
#     f = Process(target=counter, args=(125000000,))
#     g = Process(target=counter, args=(125000000,))
#     h = Process(target=counter, args=(125000000,))

#     a.start()
#     b.start()
#     c.start()
#     d.start()
#     e.start()
#     f.start()
#     g.start()
#     h.start()

#     a.join()
#     b.join()
#     c.join()
#     d.join()
#     e.join()
#     f.join()
#     g.join()
#     h.join()

#     end_time = time.perf_counter()
#     print('finished in ' + str(end_time - start_time) + ' seconds')


def main():
    start_time = time.perf_counter()
    print(cpu_count())
    cpuList = [Process(target=counter, args=(round(1000000000 / 10),)) for i in range(1, 10)]
    for cpu in cpuList:
        cpu.start()
        cpu.join()

    # a = Process(target=counter, args=(10000000000,))
    # a.start()
    # a.join()

    end_time = time.perf_counter()
    print('finished in ' + str(end_time - start_time) + ' seconds')


if __name__ == '__main__':
    main()
