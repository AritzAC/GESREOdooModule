# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

#Author: Daniel Brizuela
class Pieza(models.Model):
    _name = 'gesre.pieza'

    #Atributos
    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripcion", required=True)
    stock = fields.Integer(string="Stock", required=True)
    
    #Relacion 1 a Muchos con Incidencia
    incidencia = fields.One2Many('gesre.incidencia', 'pieza', string="Incidencia")
    #Relacion Muchos a 1 con Trabajador
    trabajador = fields.Many2One('gesre.trabajador', string="Trabajador")
