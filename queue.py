from message import Message


class Queue:
    def __init__(self):
        self.queue = []

    def add_transation_message(self, source_wallet, destination_wallet, num_coins):
        self.queue.append(Message(source_wallet, destination_wallet, num_coins).message)

    def remove_first_message(self):
        return self.queue.pop(0)

    def print_queue(self):
        i = 0
        print("Printing queue:")
        for message in self.queue:
            print("Message " + str(i) + ": " + str(message))
            i += 1


this_queue = Queue()
# message1 = Message("zyx124", "abd298", 4)
this_queue.add_transation_message("zyx124", "abd298", 4)
this_queue.add_transation_message("rtf345", "abd298", 4)
this_queue.add_transation_message("hre529", "abd298", 4)
this_queue.add_transation_message("bbg027", "abd298", 4)
this_queue.print_queue()
print()
print("Removing message: " + str(this_queue.remove_first_message()))
print()
this_queue.print_queue()