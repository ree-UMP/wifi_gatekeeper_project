import unittest
from python_hotspot_controller.hotspot_control import get_connected_devices

class TestHotspotControl(unittest.TestCase):
    def test_get_connected_devices(self):
        devices = get_connected_devices()
        self.assertIsInstance(devices, list)

if __name__ == '__main__':
    unittest.main()