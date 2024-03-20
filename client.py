import random
import asyncio
import websockets
import json
import string
from plane import Plane

def generate_flight_code() -> str:
    """
    Generate a random flight code in the format 'XX1234', where 'XX' are two random uppercase letters
    and '1234' are four random digits.

    Returns:
        str: Randomly generated flight code.

    Example:
        >>> generate_flight_code()
        'AB5678'
    """
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    numbers = ''.join(random.choices(string.digits, k=4))
    flight_code = f"{letters}{numbers}"
    return flight_code




async def send_planes() -> None:
    """Generate and send plane data via WebSocket.

    This function establishes a WebSocket connection to a specified URI and
    continuously sends randomly generated plane data (flight code and request
    type) at random intervals. The random number generator is seeded with a
    fixed value (42) to ensure reproducibility.

    Note:
        The flight code is generated as a random str LLNNNN where L is a random letter and N is a random number.
        The request type is randomly chosen from the options 'landing',
        'takeoff', or 'emergency'.

    URI:
        The URI to establish the WebSocket connection is set to
        'ws://localhost:7890'.

    Raises:
        ConnectionRefusedError: If the connection to the WebSocket server fails.

    """
    random.seed(42)
    uri = "ws://localhost:7890"

    async with websockets.connect(uri) as websocket:
        while True:
            await asyncio.sleep(random.uniform(0.6, 1))
            request_type = random.choice(["landing", "takeoff", "emergency"])
            flight_code = generate_flight_code()
            plane = Plane(flight_code, request_type)

            plane_data = {
                "flight_code": plane.flight_code,
                "type": plane.plane_type
            }
            await websocket.send(json.dumps(plane_data))
            print(f"Sending {plane}")


if __name__ == '__main__':
    asyncio.run(send_planes())
