# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class Trabajador(models.Model):
    _inherit = 'res.users'
    
    #Atributos
    precioHora = fields.Float(digits=(4, 2))
    fechaContrato = fields.Date(string="Fecha Contrato", required="true")
    
    #Relaciones
    #recoge = fields.One2Many('gesre.recoge', 'trabajador', string='Recoge')
    #pieza = fields.One2Many('gesre.pieza', 'trabajador', string='Pieza')