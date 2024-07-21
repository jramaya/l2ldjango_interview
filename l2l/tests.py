from django.test import TestCase
from datetime import datetime
from l2l.templatetags.l2l_extras import l2l_dt

# Create your tests here.

class TestDateFilter(TestCase):
    def test_formatting_from_datetime(self):
        testing_date = datetime(2020,1,1,12,1,1)
        l2ldt_date = l2l_dt(testing_date)
        self.assertEqual(l2ldt_date,(
            '2020-01-01 12:01:01'))

    def test_formatting_from_string(self):
        testing_str = '2020-01-01T12:01:01'
        l2ldt_date = l2l_dt(testing_str)
        self.assertEqual(l2ldt_date,(
            '2020-01-01 12:01:01'))

    def test_formatting_from_object(self):
        testing_object = dict() 
        l2ldt_result = l2l_dt(testing_object)
        self.assertEqual(l2ldt_result, testing_object) 
