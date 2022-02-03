# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models
from odoo import exceptions

class Trabajador(models.Model):
    _name = 'gesre.trabajador'
    _inherit = 'res.users'
    
    #Atributos
    precioHora = fields.Float(digits=(4, 2))
    fechaContrato = fields.Date(string="Fecha Contrato", required="true")
    
    #Relaciones
    recoge = fields.One2many('gesre.recoge', 'trabajador', string='Recoge')
    pieza = fields.One2many('gesre.pieza', 'trabajador', string='Pieza')
    
    @api.constrains('precioHora')
    def _validar_precioHora_positivo(self):
        if self.precioHora < 0:
            raise exceptions.ValidationError("El precio hora no puede ser negativo")
    
    @api.constrains('fechaContrato')
    def _validar_fecha_antes_hoy(self):
        
        if self.fechaContrato > fields.Date.today():
            raise exceptions.ValidationError("Fecha no puede ser despues de la actual")
        
    @api.onchange('precioHora')
    def _control_precioHora(self):
        if self.precioHora < 0:
            raise exceptions.ValidationError("El precio hora no puede ser negativo")