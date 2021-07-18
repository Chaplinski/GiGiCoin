import time
import hashlib
import json


class Block:
    def __init__(self):
        self.block_header = {}
        self.transaction_list = {}

    def create_block(self):
        block_data = self.get_block_data()
        self.create_block_header("abc123", 17, block_data)
        print("this is where a block will be created")

    def create_block_header(self, hash_of_previous_block_header, nonce, block_data):
        self.block_header['previous_block_header'] = hash_of_previous_block_header
        self.block_header['timestamp'] = time.time()
        self.block_header['nonce'] = nonce
        self.block_header['hash_of_block_data'] = hashlib.sha256(json.dumps(block_data).encode('utf-8'))

    def get_block_data(self):
        block_data = self.get_transaction_list()
        return block_data

    def get_transaction_list(self):
        # get the transaction list from the queue and store it as a dictionary
        # self.transaction_list = transaction_list
        return self.transaction_list


b = Block()
b.create_block()
