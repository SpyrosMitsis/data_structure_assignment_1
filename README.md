# Airport Air Traffic Control Simulation

This repository contains Python code for simulating an airport's air traffic control system using asyncio, websockets, and priority queue data structure. The simulation includes two main components: the airport server and the plane client.


## Setup

To run the simulation both files need to be executed at the same time. 
Simply execute these two commands in two separate terminals

The client file sends plane requests:
```bash
python client.py
```

The server file receives plane requests and gives them permission to take action:
```bash
python server.py
```


## Running Unit Tests
To run the tests with vs code simply go the `Testing` badge in the activity bar.

To run the unit tests in the terminal simply use this command:

```bash
python -m unittest Tests\test_priority_queue.py Tests\test_client.py Tests\test_server.py     
```

## Demo

[demo.webm](https://github.com/SpyrosMitsis/data_structure_assigment_1/blob/main/demo.webm)
