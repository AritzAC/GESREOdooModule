# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models

class Incidencia(models.Model):
    _name = 'gesre.incidencia'
    
    estrellas = fields.Integer(string="Estrellas")
    horas = fields.Integer(string="Horas")
    precio = fields.Float(string="Precio")
    tipoIncidencia = fields.Selection([('a', 'ELECTRICO'),
                                      ('b', 'FACHADA'),
                                      ('c', 'FONTANERIA'),
                                      ('d', 'GAS'),
                                      ('e', 'HUMEDAD'),
                                      ('f', 'CERRAJERO'),
                                      ('g', 'REVISION')], string="Tipo Incidencia", required="true")
    statusIncidencia = fields.Selection([('a', 'PENDIENTE'),
                                        ('b', 'PROCESO'),
                                        ('c', 'CERRADO')], string="Estado de Incidencia", required="true")                                  
   
    #Relacion 1 a Muchos con Recoge
    recoge = fields.One2many('gesre.recoge', 'incidencia', string="Recoge")
    #Relacion Mucho a 1 con Pieza
    pieza = fields.Many2one('gesre.pieza', string="Pieza")
    #Relacion Mucho a 1 con Cliente
    cliente = fields.Many2one('gesre.cliente', string="Cliente") 