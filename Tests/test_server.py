import unittest
from unittest.mock import MagicMock
import asyncio
import websockets
import json
from server import Airport, process_planes

class TestAirport(unittest.TestCase):
    def test_add_request(self):
        airport = Airport()
        plane = MagicMock()
        plane.flight_code = "AB1234"
        plane.plane_type = "landing"
        airport.add_request(plane)
        # Assert that the plane is added to the queue with the correct priority
        self.assertEqual(len(airport.air_traffic_control_queue.heap), 1)
        self.assertEqual(airport.air_traffic_control_queue.heap[0][1], "AB1234")
        self.assertEqual(airport.air_traffic_control_queue.heap[0][2], 1)

    def test_give_action_permission(self):
        airport = Airport()
        # Add some mock planes to the queue
        airport.air_traffic_control_queue.enqueue("AB1234", 1)  # Landing
        airport.air_traffic_control_queue.enqueue("CD5678", 0)  # Takeoff
        airport.air_traffic_control_queue.enqueue("EF91011", 100)  # Emergency landing
        # Mock printing to stdout
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        airport.give_action_permission()
        airport.give_action_permission()
        airport.give_action_permission()
        # Assert that the correct messages are printed based on priorities
        self.assertIn("\033[92mCONTROL\033[0m: Flight \033[93mAB1234\033[0m has permission to land", captured_output.getvalue())
        self.assertIn("\033[92mCONTROL\033[0m: Flight \033[93mCD5678\033[0m has permission to takeoff", captured_output.getvalue())
        self.assertIn("\033[92mCONTROL\033[0m: Flight \033[93mEF91011\033[0m has permission to\033[91m emergency \033[0mland", captured_output.getvalue())

        # Reset stdout
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
