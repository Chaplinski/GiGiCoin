# GiGiCoin

<h3>block.py</h3>

To create a new block

`python3 block.py create`

To return the hash of the previous block

`python3 block.py previous-header`

<h3>queue.py</h3>

To add a transaction message to the queue

`python3 queue.py add <source wallet> <destination wallet> <number of coins to send>`

The following example will send 7 coins from the source wallet abc123 to destination wallet def456:

`python3 queue.py add abc123 def456 7`

To retrieve the next message from the queue

`python3 queue.py next`

To print the entire queue

`python3 queue.py print`

<h3>vault.py</h3>

To check whether a hash exists on disk

`python3 vault.py find <hash> <difficulty>`

The following example will search for the hash 123abc with a difficulty of 4:

`python3 vault.py find 123abc 4`

<h3>blockchain.py</h3>

To get the hash from the previous block in the blockchain

`python3 blockchain.py previous-hash`

To get the entire blockchain

`python3 blockchain.py blockchain`
