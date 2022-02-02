# -*- coding: utf-8 -*-
from odoo import api
from odoo import exceptions
from odoo import fields
from odoo import models

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
    #Numero negativo y longitud en Stock
    @api.constrains('stock')
    def _verificar_stock_no_negativo(self):
        if self.stock < 0:
            raise exceptions.ValidationError("Stock no puede ser negativo")
        if len(str(self.stock)) > 3:
            raise exceptions.ValidationError("Solo se admiten numeros de 3 dígitos en Stock")
    
    #Longitud en Nombre
    @api.onchange('nombre')
    def _limitar_longitud_campo_nombre(self):
        if len(self.nombre) > 25:
            return {
                'warning': {
                    'title': "Límite alcanzado",
                    'message': "Límite de 25 caracteres alcanzado en Nombre",
                },
            }
            
    @api.constrains('nombre')
    def _limitar_longitud_campo_nombre(self):
        if len(self.nombre) > 25:
            raise exceptions.ValidationError("Límite de 25 caracteres alcanzado en Nombre")
