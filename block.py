import time
import hashlib
import json
from queue import Queue

class Block:
    def __init__(self):
        self.block_header = {}
        self.block = {}

    def create_block(self):
        # TODO load blockchain and retrieve and pass previous block header

        block_data = self.get_block_data()
        self.create_block_header("abc123", 17, block_data)
        # print(self.block_header)
        self.block['block_header'] = self.block_header
        self.block['block_data'] = block_data
        return self.block

    def create_block_header(self, hash_of_previous_block_header, nonce, block_data):
        self.block_header['previous_block_header'] = hash_of_previous_block_header
        self.block_header['timestamp'] = time.time()
        self.block_header['nonce'] = nonce
        self.block_header['hash_of_block_data'] = hashlib.sha256(json.dumps(block_data).encode('utf-8')).hexdigest()

    def get_block_data(self):
        block_data = self.get_all_messages_from_queue()
        return block_data

    def get_all_messages_from_queue(self):
        queue = Queue()
        return queue.retrieve_all_messages()


# TODO confirm with blockchain that a wallet has num_coins before allowing transaction
