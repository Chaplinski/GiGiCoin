from transaction import Transaction
import sys


class Queue:
    def __init__(self):
        self.queue = []
        if len(sys.argv) > 1:
            if sys.argv[1] == "add":
                if len(sys.argv) > 4:
                    self.add_transaction_message_to_queue(sys.argv[2], sys.argv[3], sys.argv[4])
                    print(len(self.queue))
                else:
                    print("You are missing one or more parameters")
            elif sys.argv[1] == "next":
                self.add_transaction_message_to_queue("rtf345", "abd298", 4)
                print(self.remove_first_message())
            elif sys.argv[1] == "print":
                self.add_transaction_message_to_queue("rtf345", "abd298", 4)
                self.add_transaction_message_to_queue("hre529", "abd298", 4)
                self.add_transaction_message_to_queue("bbg027", "abd298", 4)
                self.print_queue()

    def add_transaction_message_to_queue(self, source_wallet, destination_wallet, num_coins):
        self.queue.append(Transaction(source_wallet, destination_wallet, num_coins).message)

    def remove_first_message(self):
        return self.queue.pop(0)

    def print_queue(self):
        i = 0
        print("Printing queue:")
        for message in self.queue:
            print("Message " + str(i) + ": " + str(message))
            i += 1

    def retrieve_all_messages(self):
        return self.queue


this_queue = Queue()