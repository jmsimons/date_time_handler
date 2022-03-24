import unittest
from date_time_handler import DateTimeHandler


class TestDateTimeHandler(unittest.TestCase):
    ''' implicitly tests that each callable method returns the correct type and value under every programmed case '''

    def setUp(self):
        self.start_time = (2000, 1, 1, 0, 0, 0) # January 1, 2000 00:00:00

    def test_timestring(self):
        self.assertEqual()