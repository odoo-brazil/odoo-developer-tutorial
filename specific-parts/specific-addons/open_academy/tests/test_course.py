# -*- coding: utf-8 -*-

import datetime
from dateutil.relativedelta import relativedelta

from openerp import exceptions, fields
from openerp.tools import mute_logger
import openerp.tests.common as common

class TestOpenAcademy(common.TransactionCase):

    def setUp(self):
        super(TestOpenAcademy, self).setUp()

    def test_exercise_01(self):
        course_model = self.env['openacademy.course']
        python_course = course_model.create({
            'name': 'Python Course',
            'description': 'Google Python Class',
        })

    def test_exercise_02(self):
        course_model = self.env['openacademy.course']
        domain = [
            ('name', '=', 'Course 0'),
            ('name', '=', 'Course 1'),
            ('name', '=', 'Course 2'),
        ]
        courses = course_model.search(domain)
        self.assertEquals(len(courses), 3,
            "Os cursos inseridos via xml de dados não estão corretos")

    # def test_exercise_08(self):
    #     sesison_model = self.env['openacademy.session']
    #     python_session = sesison_model.create({
    #         'name': 'Python 2016/2',
    #         'start_date': datetime.datetime.now(),
    #         'duration': 2,
    #         'seats': 10,
    #     })
    #
    # def test_exercise_09(self):
    #     course_model = self.env['openacademy.course']
    #     self.res_partner_model = self.env['res.partner']
    #     self.partner = self.browse_ref('base.res_partner_2')
    #     elm_course = course_model.create({
    #         'name': 'ELM Course',
    #         'description': 'Chega de dor de cabeça no front end',
    #         'responsible_id': self.partner.id,
    #     })
    #     self.res_partner_model = self.env['res.partner']
    #     self.elm_instructor = self.browse_ref('base.res_partner_3')
    #     sesison_model = self.env['openacademy.session']
    #     elm_session = sesison_model.create({
    #         'name': 'ELM 2016/2',
    #         'start_date': datetime.datetime.now(),
    #         'duration': 2,
    #         'seats': 10,
    #         'instructor_id': self.elm_instructor.id,
    #         'course_id': elm_course.id,
    #     })
    #
    # def test_exercise_10(self):
    #     course_model = self.env['openacademy.course']
    #     self.res_partner_model = self.env['res.partner']
    #     self.partner = self.browse_ref('base.res_partner_2')
    #     elm_course = course_model.create({
    #         'name': 'ELM Course',
    #         'description': 'Chega de dor de cabeça no front end',
    #         'responsible_id': self.partner.id,
    #     })
    #     self.res_partner_model = self.env['res.partner']
    #     self.elm_instructor = self.browse_ref('base.res_partner_3')
    #     sesison_model = self.env['openacademy.session']
    #     elm_session_1 = sesison_model.create({
    #         'name': 'ELM 2016/1',
    #         'start_date': datetime.datetime.now(),
    #         'duration': 2,
    #         'seats': 10,
    #         'instructor_id': self.elm_instructor.id,
    #         'course_id': elm_course.id,
    #     })
    #     elm_session_2 = sesison_model.create({
    #         'name': 'ELM 2016/2',
    #         'start_date': datetime.datetime.now(),
    #         'duration': 2,
    #         'seats': 10,
    #         'instructor_id': self.elm_instructor.id,
    #         'course_id': elm_course.id,
    #     })
    #     self.assertEquals(len(elm_course.session_ids), 2,
    #         "A quantidade de sessões do curso de EML esta incorreta")
    #
    # def test_exercise_11(self):
    #     sesison_model = self.env['openacademy.session']
    #     attendees = self.browse_ref(
    #         'base.res_partner_2') | self.browse_ref('base.res_partner_3')
    #     python_session = sesison_model.create({
    #         'name': 'Python 2016/2',
    #         'start_date': datetime.datetime.now(),
    #         'duration': 2,
    #         'seats': 10,
    #         'attendee_ids': (6, 0, [attendees])
    #     })
    #     # TODO
    #
    # def test_exercise_12(self):
    #     partner = self.browse_ref('base.res_partner_2')
    #     partner.write(
    #         {'instructor': True}
    #     )
    #
    # def test_exercise_15(self):
    #     # taken_seats
    #     self.assertTrue(False, " ")
    #
    # def test_exercise_16(self):
    #     # default values
    #     self.assertTrue(False, " ")
    #
    # def test_exercise_17(self):
    #     # on change
    #     self.assertTrue(False, " ")
    #
    # def test_exercise_18(self):
    #     # constraint python
    #     self.assertTrue(False, " ")
    #
    # def test_exercise_20(self):
    #     # constraint SQL
    #     self.assertTrue(False, " ")
    #
    # def test_exercise_21(self):
    #     # duplicate
    #     self.assertTrue(False, " ")
    #
    # def test_exercise_28(self):
    #     # workflow
    #     self.assertTrue(False, " ")
    #
    # def test_exercise_30(self):
    #     # automated transitions
    #     self.assertTrue(False, " ")
    #
    # def test_exercise_31(self):
    #     # Server action
    #     self.assertTrue(False, " ")
    #
    # def test_exercise_32(self):
    #     # Access control
    #     self.assertTrue(False, " ")
    #
    # def test_exercise_35(self):
    #     # Wizard
    #     self.assertTrue(False, " ")




