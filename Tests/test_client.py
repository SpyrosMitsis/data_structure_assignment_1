import unittest 
from unittest.mock import patch, Mock
import asyncio
from client import generate_flight_code, send_planes

class TestGenerateFlightCode(unittest.TestCase):
    def test_generate_flight_code(self):
        flight_code = generate_flight_code()
        self.assertRegex(flight_code, r'^[A-Z]{2}\d{4}$')

@patch('client.websockets.connect')
@patch('client.asyncio.sleep')
class TestSendPlanes(unittest.TestCase):
    async def test_send_planes(self, mock_sleep, mock_websocket_connect):
        mock_websocket.send = Mock(return_value=asyncio.Future()) 
        mock_websocket_connect.return_value.__aenter__.return_value = mock_websocket

        # Ensure send_planes properly sends data
        await send_planes()

        # Assert that websocket connection is established
        mock_websocket_connect.assert_called_once_with('ws://localhost:7890')

        # Assert that websocket send is called with proper data
        mock_websocket.send.assert_called()
        
if __name__ == '__main__':
    unittest.main()
