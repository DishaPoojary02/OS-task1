import threading
import time


class SharedBuffer:
    def __init__(self):
        self.buffer_array = [None] * 5
        self.write_position = 0
        self.read_position = 0
        self.item_count = 0

        self.buffer_condition = threading.Condition()

    def add_item(self, item):
        with self.buffer_condition:
            while self.item_count == 5:
                print("Buffer is full. Producer is waiting.")
                self.buffer_condition.wait()

            self.buffer_array[self.write_position] = item
            self.write_position = (self.write_position + 1) % 5
            self.item_count += 1

            print("Producer added item", item)

            self.buffer_condition.notify()

    def remove_item(self):
        with self.buffer_condition:
            while self.item_count == 0:
                print("Buffer is empty. Consumer is waiting.")
                self.buffer_condition.wait()

            item = self.buffer_array[self.read_position]
            self.buffer_array[self.read_position] = None
            self.read_position = (self.read_position + 1) % 5
            self.item_count -= 1

            print("Consumer took item", item)

            self.buffer_condition.notify()


def producer_task(shared_buffer):
    for item in range(1, 11):
        shared_buffer.add_item(item)
        time.sleep(0.1)


def consumer_task(shared_buffer):
    for _ in range(10):
        shared_buffer.remove_item()
        time.sleep(0.15)


shared_buffer = SharedBuffer()

producer_thread = threading.Thread(
    target=producer_task,
    args=(shared_buffer,)
)

consumer_thread = threading.Thread(
    target=consumer_task,
    args=(shared_buffer,)
)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Program completed.")