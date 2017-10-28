
import datetime
import json
from decimal import Decimal
from unittest import TestCase

from json_default import default


class DefaultTestCase(TestCase):
    def encode(self, obj):
        return json.dumps(obj, default=default)

    def test_simple(self):
        self.assertEqual(self.encode({'a': 1}), '{"a": 1}')

    def test_datetime(self):
        d = datetime.datetime(2017, 6, 8, 12, 23, 1, 1231)
        self.assertEqual(self.encode({'when': d}), '{"when": "2017-06-08T12:23:01"}')

    def test_datetime_tz(self):
        d = datetime.datetime(2017, 6, 8, 12, 23, 1, 1231, tzinfo=datetime.timezone.utc)
        self.assertEqual(self.encode({'when': d}), '{"when": "2017-06-08T12:23:01Z"}')

    def test_date(self):
        d = datetime.date(2016, 6, 8)
        self.assertEqual(self.encode({'when': d}), '{"when": "2016-06-08"}')

    def test_time(self):
        d = datetime.time(17, 53, 39)
        self.assertEqual(self.encode({'when': d}), '{"when": "17:53:39"}')

    def test_decimal(self):
        self.assertEqual(self.encode({'value': Decimal('123.45')}), '{"value": "123.45"}')
