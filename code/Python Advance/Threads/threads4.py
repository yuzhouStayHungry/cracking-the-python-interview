import threading

num = 0
mutex = threading.Lock()


def plus_one():
    global num
    mutex.acquire()
    for i in range(1000000):
        num += 1
    mutex.release()


def minus_one():
    global num
    mutex.acquire()
    for i in range(1000000):
        num -= 1
    mutex.release()


def main():
    t1 = threading.Thread(target=plus_one)
    t2 = threading.Thread(target=minus_one)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(num)


if __name__ == '__main__':
    main()
