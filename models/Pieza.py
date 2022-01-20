# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models
from odoo import exceptions

class Pieza(models.Model):
    _name = 'gesre.pieza'

    #Atributos
    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripcion", required=True)
    stock = fields.Integer(string="Stock", required=True)
    
    #Relacion 1 a Muchos con Incidencia
    incidencia = fields.One2many('gesre.incidencia', 'pieza', string="Incidencia")
    #Relacion Muchos a 1 con Trabajador
    trabajador = fields.Many2one('gesre.trabajador', string="Trabajador")
    
    #Validaciones
    @api.constrains('stock')
    def _verificar_stock_no_negativo(self):
        if self.stock < 0:
            raise exceptions.ValidationError("Stock no puede ser negativo")
