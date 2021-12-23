# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class Trabajador(models.Model):
    _name = 'gesre.trabajador'
    _inherit = 'res.users'
    
    #Atributos
    precioHora = fields.Float(digits=(4, 2))
    fechaContrato = fields.Date(string="Fecha Contrato", required="true")
    
    #Relaciones
    recoge = fields.One2many('gesre.recoge', 'trabajador', string='Recoge')
    pieza = fields.One2many('gesre.pieza', 'trabajador', string='Pieza')