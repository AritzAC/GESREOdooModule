# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Trabajador(models.Model):
    _name = 'gesre.trabajador'
    _inherit = 'res.users'
    
    #Atributos
    precioHora = fields.Float(digits=(4,2))
    fechaContrato = fields.Date.today()
    
    #Relaciones
    recoge = fields.One2Many('gesre.recoge', 'trabajador', string='Recoge')
    
    piezas = fields.One2Many('gesre.pieza', 'trabajador', string='Piezas')