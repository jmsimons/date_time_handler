import unittest, datetime, time
from pytz import timezone
from date_time_handler.main import load_tz, DateTimeHandler


class TestDateTimeHandler(unittest.TestCase):
    ''' implicitly tests that each callable method returns the correct type and value under every programmed case '''

    @classmethod
    def setUpClass(self):
        print("****** Setting up test-class ******")
        self.tz_utc = "UTC"
        self.tz_pac = "US/Pacific"
        self.dt_fmt = DateTimeHandler()
        self.utc_fmt = DateTimeHandler(time_zone = self.tz_utc) # will start at start_tz or utc and convert to utc
        self.pac_fmt = DateTimeHandler(time_zone = self.tz_pac) # will start at start_tz or Pacific and convert to Pacific
        self.start_tuple = (2000, 1, 1, 0, 0, 0)
        self.start_time = datetime.datetime(*self.start_tuple, tzinfo = None) # January 1, 2000 00:00:00
        self.one_day = datetime.datetime(2000, 1, 2, 0, 0, 0, tzinfo = None) # January 8, 2000 00:00:00
        self.one_week = datetime.datetime(2000, 1, 8, 0, 0, 0, tzinfo = None) # January 8, 2000 00:00:00
        self.one_month = datetime.datetime(2000, 2, 1, 0, 0, 0, tzinfo = None) # Febuary 1, 2000 00:00:00
        self.three_months = datetime.datetime(2000, 4, 1, 0, 0, 0, tzinfo = None) # Febuary 1, 2000 00:00:00
        self.six_months = datetime.datetime(2000, 7, 1, 0, 0, 0, tzinfo = None) # July 1, 2000 00:00:00
        self.one_year = datetime.datetime(2001, 1, 1, 0, 0, 0, tzinfo = None) # January 1, 2001 00:00:00
    
    @classmethod
    def tearDownClass(self):
        print("")

    def test_load_tz(self):
        self.assertEqual(load_tz(self.tz_pac), timezone(self.tz_pac))
        self.assertEqual(load_tz("not_real_tz"), None) # returns none if tz string unreconcilable

    def test__get_time_obj(self):
        ''' tests _get_time_obj type detection and timezone conversion '''
        # TODO: resolve ol_offset_hours through pytz.timezone/datetime
        dl_offset_hours = 7

        # use utc_fmt to convert start_time from local time to utc and check for correct daylight time
        utc_timestamp = self.utc_fmt.timestamp(self.start_time.timestamp(), start_tz = self.tz_pac)
        self.assertEqual(utc_timestamp, int(self.start_time.timestamp() + (60 * 60 * dl_offset_hours)))
        
        # use pac_fmt to convert back to local time and check for correct daylight time
        self.assertEqual(self.pac_fmt.timestamp(utc_timestamp, start_tz = self.tz_utc), int(self.start_time.time_stamp()))

    def test_timestring(self):
        ''' tests that timestring returns a string of the correct value and format '''
        timestring = self.dt_fmt.timestring(self.start_time.timestamp())
        self.assertEqual(timestring, "2000/01/01 00:00:00")
    
    def test_timestamp(self):
        ''' tests that timestamp returns an integer of the correct value '''
        timestamp = self.dt_fmt.timestamp(self.start_time.timestamp())
        self.assertEqual(type(timestamp), int) # change to float if use-case requires more specificity
        self.assertEqual(timestamp, int(self.start_time.timestamp()))
    
    def test_timetuple(self):
        ''' tests that timetuple returns a tuple containing the correct values '''
        timetuple = self.dt_fmt.timetuple(self.start_time.timestamp())
        self.assertEqual(timetuple, self.start_time.timetuple())
    
    def test_datestring(self):
        ''' tests that timestring returns a string of the correct value and format '''
        datestring = self.dt_fmt.datestring(self.start_time.timestamp())
        self.assertEqual(datestring, "2000/01/01")
    
    def test_datestamp(self):
        ''' tests that datestamp returns an integer of the correct value '''
        datestamp = self.dt_fmt.datestamp(self.start_time.timestamp())
        self.assertEqual(type(datestamp), int) # change to float if use-case requires more specificity
        self.assertEqual(datestamp, int(self.start_time.timestamp()))
    
    def test_datetuple(self):
        ''' tests that timestring returns a string of the correct value and format '''
        datetuple = self.dt_fmt.datetuple(self.start_time.timestamp())
        expected_time = self.start_time
        expected_time.replace(tzinfo = None)
        self.assertEqual(datetuple, expected_time.timetuple())
    
    def test_add_interval(self):
        ''' tests that add_interval returns an integer of the correct value and format for each programmed case '''
        one_day = self.dt_fmt.add_interval(self.start_time.timestamp(), "daily")
        one_week = self.dt_fmt.add_interval(self.start_time.timestamp(), "weekly")
        one_month = self.dt_fmt.add_interval(self.start_time.timestamp(), "monthly")
        three_months = self.dt_fmt.add_interval(self.start_time.timestamp(), "3 months")
        six_months = self.dt_fmt.add_interval(self.start_time.timestamp(), "6 months")
        one_year = self.dt_fmt.add_interval(self.start_time.timestamp(), "12 months")
        self.assertEqual(one_day, int(self.one_day.timestamp()))
        self.assertEqual(one_week, int(self.one_week.timestamp()))
        self.assertEqual(one_month, int(self.one_month.timestamp()))
        self.assertEqual(three_months, int(self.three_months.timestamp()))
        self.assertEqual(six_months, int(self.six_months.timestamp()))
        self.assertEqual(one_year, int(self.one_year.timestamp()))
