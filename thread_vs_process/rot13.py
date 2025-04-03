import time
from multiprocessing import Process, Queue, Event
from codecs import encode

def sender(sender_queue, getter_queue, exit_event):
    while not exit_event.is_set():
        try:
            message = sender_queue.get()
            message_lower = message.lower()
            time.sleep(5)
            getter_queue.put(message_lower)
        except (KeyboardInterrupt, SystemExit):
            exit_event.set()

def getter(getter_queue, main_queue, exit_event):
    while not exit_event.is_set():
        try:
            message = getter_queue.get()
            encode_message = encode(message,'rot13')
            curr_time = time.strftime("[%H:%M:%S] ", time.gmtime())
            print(curr_time + "encoded message: " + encode_message)
            main_queue.put(encode_message)
        except (KeyboardInterrupt, SystemExit):
            exit_event.set()



def main():
    sender_queue = Queue()
    getter_queue = Queue()
    main_queue = Queue()

    exit_event = Event()

    A = Process(target=sender, args=(sender_queue, getter_queue, exit_event))
    B = Process(target=getter, args=(getter_queue, main_queue, exit_event))

    A.start()
    B.start()

    try:
        while True:
            input_str = input()
            curr_time = time.strftime("[%H:%M:%S] ", time.gmtime())
            print(curr_time + "message: "+ input_str)
            sender_queue.put(input_str)
    except KeyboardInterrupt:
        curr_time = time.strftime("[%H:%M:%S] ", time.gmtime())
        exit_event.set()
        print(curr_time + "exit")

        A.join()
        B.join()

        if A.is_alive():
            A.terminate()
        if B.is_alive():
            B.terminate()


if __name__ == "__main__":
    main()