# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models

class Recoge(models.Model):
    _name = 'gesre.recoge'
    
    horasEstimadas = fields.Integer(string="Horas Estimadas", required="true")
    fechaRecogida = fields.Date(string="Fecha Recogida", required="true")

    #Relacion Muchos a 1 con Incidencias
    incidencia = fields.Many2one('gesre.incidencia', string="Incidencia")
    #Relacion Muchos a 1 con Trabajador
    trabajador = fields.Many2one('res.users', string="Trabajador")