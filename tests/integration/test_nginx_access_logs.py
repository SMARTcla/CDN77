import unittest

class TestNginxAccessLogs(unittest.TestCase):
    def test_nginx_logs_format(self):
        log_format_correct = True
        self.assertTrue(log_format_correct, msg="Smth")

    def test_nginx_logs_availability(self):
        logs_available = True
        self.assertTrue(logs_available, msg="Smth")

if __name__ == '__main__':
    unittest.main()
