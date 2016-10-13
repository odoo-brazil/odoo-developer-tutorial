# -*- coding: utf-8 -*-

import datetime
from dateutil.relativedelta import relativedelta

from openerp import exceptions, fields
from openerp.tools import mute_logger
import openerp.tests.common as common

class TestCourse(common.TransactionCase):

    def test_exercise_01(self):

        self.assertEqual(
            False, True, 'Open Academy: Message')
