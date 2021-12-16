# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class Recoge(models.Model):
    _name = 'gesre.recoge'
    
    horasEstimadas = fields.Integer(string="Horas Estimadas", required="true")
    fechaRecogida = fields.Date.today()
