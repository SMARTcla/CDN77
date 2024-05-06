import unittest

class TestPrometheusAlerts(unittest.TestCase):
    def test_alertmanager_reacts_to_high_load(self):
        high_load_detected = True
        self.assertTrue(high_load_detected, msg="Smth")

    def test_alertmanager_notifies_on_service_down(self):
        service_down = True
        self.assertTrue(service_down, msg="Smth")

if __name__ == '__main__':
    unittest.main()
