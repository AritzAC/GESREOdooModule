# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Pieza(models.Model):
    _name = 'pieza.pieza'

    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripcion", required=True)
    stock = fields.Integer(string="Stock", required=True)
