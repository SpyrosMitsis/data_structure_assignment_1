import asyncio
import websockets
import json
from priority_queue import PriorityQueue
from plane import Plane
from functools import partial

class Airport:
    """Class representing an airport's air traffic control system.

    Attributes:
        air_traffic_control_queue (PriorityQueue): A priority queue to manage incoming plane requests.
    """

    def __init__(self) -> None:
        """Initialize the Airport instance."""
        self.air_traffic_control_queue: PriorityQueue = PriorityQueue()

    def add_request(self, plane: Plane) -> None:
        """Add a plane request to the air traffic control queue.

        Args:
            plane (Plane): The plane object representing the request.
        """
        if plane.plane_type == "landing":
            self.air_traffic_control_queue.enqueue(plane.flight_code, 1)
        elif plane.plane_type == "takeoff":
            self.air_traffic_control_queue.enqueue(plane.flight_code, 0)
        elif plane.plane_type == "emergency":
            self.air_traffic_control_queue.enqueue(plane.flight_code, 100)
        else:
            raise ValueError("Invalid plane request type. Must be 'landing', 'takeoff', or 'emergency'.")
            

    def give_action_permission(self) -> None:
        """Process the next action for the airport.

        This method grants permission for the next plane in the queue to takeoff, land,
        or perform an emergency landing based on its priority.

        """
        if not self.air_traffic_control_queue.is_empty():
            _, plane, priority = self.air_traffic_control_queue.dequeue()
            if priority == 1:
                print(f"\033[92mCONTROL\033[0m: Flight \033[93m{plane}\033[0m has permission to land")
            elif priority == 100:
                print(f"\033[92mCONTROL\033[0m: Flight \033[93m{plane}\033[0m has permission to\033[91m emergency \033[0mland")
            elif priority == 0:
                print(f"\033[92mCONTROL\033[0m: Flight \033[93m{plane}\033[0m has permission to takeoff")
            else:
                raise ValueError("Invalid priority level encountered in air traffic control queue.")


async def simulate_airport(airport: Airport) -> None:
    """Simulate the operation of the airport's air traffic control system.

    This coroutine continuously checks for new actions to be performed by the airport
    and grants permissions accordingly.

    Args:
        airport (Airport): The airport instance representing the air traffic control system.

    """
    while True:
        await asyncio.sleep(1)  
        airport.give_action_permission()
        
async def process_planes(websocket: websockets.WebSocketServerProtocol, path: str, airport: Airport) -> None:
    """Process incoming plane requests received via WebSocket.

    This coroutine receives JSON-formatted messages representing plane requests
    and adds them to the airport's air traffic control queue.

    Args:
        websocket (websockets.WebSocketServerProtocol): The WebSocket connection.
        path (str): The URL path.
        airport (Airport): The airport instance representing the air traffic control system.

    """
    async for message in websocket: 
        plane_data = json.loads(message) 

        if plane_data["type"] == "takeoff":
            print(f"Flight \033[93m{plane_data['flight_code']}\033[0m requests takeoff")

        elif plane_data["type"] == "landing":
            print(f"Flight \033[93m{plane_data['flight_code']}\033[0m requests landing")

        elif plane_data["type"] == "emergency":
            print(f"Flight \033[93m{plane_data['flight_code']}\033[0m requests \033[91m{plane_data['type']}\033[0m landing")
        else:
            raise ValueError("Invalid plane request type received.")
            
        plane = Plane(plane_data["flight_code"], plane_data["type"])

        airport.add_request(plane)


if __name__ == '__main__':
    airport = Airport()
    
    process_planes_with_airport = partial(process_planes, airport=airport)
    start_server = websockets.serve(process_planes_with_airport, "localhost", 7890) 

    asyncio.get_event_loop().run_until_complete(asyncio.gather(
        start_server,
        simulate_airport(airport)
    ))
    asyncio.get_event_loop().run_forever()
