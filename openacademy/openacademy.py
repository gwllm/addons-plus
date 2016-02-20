# -*- coding: utf-8 -*-

from openerp import models,fields

class openacademy_course(models.Model):
    _name = 'openacademy.course'
    _description = 'Esta es la descripcion del curso'
    
    name= fields.Char('Name')
    description= fields.Text("Description")

class openacademy_session(models.Model):
    _name = 'openacademy.session'
    
    start_date = fields.Date('Start Date')
    seats = fields.Integer('Number of seats')
    duration = fields.Float('duration')

class openacademy_attendee(models.Model):
    _name = 'openacademy.attendee'
