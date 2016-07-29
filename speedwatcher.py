#!/usr/bin/env python
import MySQLdb
import MySQLdb.cursors
from math import ceil
from calendar import monthrange
from datetime import datetime, timedelta

class SpeedWatcher(object):
    def __init__(self, date_start, date_end):
        self.F = '%Y-%m-%d %H:%M:%S'
        self.data = None
        self.date_start = None
        self.date_end = None

        self.set_date_start(date_start)
        self.set_date_end(date_end)
        self.fetch_data(self.date_start, self.date_end)

    def array_nones_to_zeros(self, array):
        """ If None is found in array, replace with zero, return array """
        new_array = [0 if number is None else number for number in array]
        return new_array

    def avg(self, array):
        """ Get average from array, first clean using array_nones_to_zeros(), return float """
        array = self.array_nones_to_zeros(array)
        average = float(sum(array))/len(array) if len(array) > 0 else float('nan')
        return average

    def format_date(self, date):
        """ Use F to strip time from string """
        return datetime.strptime(date, self.F)

    def get_start_of_period(self, period_type, date):
        """ From a date, get lowest datetime in period and return as datetime object """
        _year = date.year
        _month = date.month
        _day = date.day
        _hour = date.hour

        period_date = None

        if period_type == 'hour':
            _min = 0
            period_date = datetime(_year, _month, _day, _hour, _min)

        elif period_type == 'day':
            _hour = 0
            period_date = datetime(_year, _month, _day, _hour)

        elif period_type == 'month':
            _day = 1
            period_date = datetime(_year, _month, _day)

        elif period_type == 'week':
            _year = date.isocalendar()[0]
            _week = date.isocalendar()[1]
            _day = 1
            date_str = '{}-W{}-{}'.format(_year, _week, _day)
            period_date = datetime.strptime(date_str, "%Y-W%W-%w")

        return period_date

    def get_next_period(self, period_type, date):
        """ From a date, get date from next period and return as datetime object """
        period_next = None

        if period_type == 'hour':
            period_next = date + timedelta(hours=1)

        elif period_type == 'day':
            period_next = date + timedelta(days=1)

        elif period_type == 'week':
            period_next = date + timedelta(weeks=1)

        elif period_type == 'month':
            period_next = datetime(date.year, date.month + 1, 1)

        return period_next

    def range_by(self, period_type, start_date, end_date):
        """ Create range from a start and end date based on hourly, daily, weekly, or monthly periods """
        start_date = self.get_start_of_period(period_type, start_date)
        end_date = self.get_start_of_period(period_type, end_date)
        next_end_date = self.get_next_period(period_type, end_date)

        while start_date < next_end_date:
            yield start_date
            start_date = self.get_next_period(period_type, start_date)

    def set_date_start(self, date):
        """ Start date setter """
        self.date_start = self.format_date(date)

    def set_date_end(self, date):
        """ End date setter """
        self.date_end = self.format_date(date)

    def fetch_data(self, date_start = None, date_end = None):
        """ Fetch data from server using a start and end date as parameters and return as tuple """
        if date_start is None:
            date_start = self.date_start

        if date_end is None:
            date_end = self.date_end

        # connect to database
        db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='SpeedWatcher', cursorclass=MySQLdb.cursors.DictCursor)
        cr = db.cursor()
        sql = "SELECT * FROM entry WHERE entry_date_created >= %s AND entry_date_created <= %s"

        cr.execute(sql, (date_start, date_end))
        self.data = cr.fetchall()
        db.close

    def get_data(self, data_type='speed_down', period_type='hour'):
        """ Parse data and return summary based on period """
        data_summary = []
        for period in self.range_by(period_type, self.date_start, self.date_end):
            next_period = self.get_next_period(period_type, period)

            data = []
            data_date = None
            first_entry = True
            for entry in self.data:

                if period <= entry['entry_date_created'] < next_period:
                    data.append(entry['entry_{}'.format(data_type)])

                    if first_entry == True:
                        first_entry = False
                        data_date = entry['entry_date_created']

            data_date = data_date if data_date else period

            data_date = data_date.strftime("%Y-%m-%d %H:%M:%S")
            data_average = round(self.avg(data), 2)

            data_summary.append({ 'time': data_date, 'data': data_average })

        return data_summary
