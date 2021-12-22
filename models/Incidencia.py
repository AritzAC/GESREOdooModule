# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models

class Incidencia(models.Model):
    _name = 'gesre.incidencia'
    
    estrellas = fields.Integer(String="Estrellas", required="false")
    horas = fields.Integer(String="Horas", required="false")
    precio = fields.Double(String="Precio", required="false")
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
    #recoge = fields.One2Many('gesre.recoge', 'incidencia', string="Recoge")
    #Relacion Mucho a 1 con Pieza
    #pieza = fields.Many2One('gesre.pieza', string="Pieza")
    #Relacion Mucho a 1 con Cliente
    #cliente = fields.Many2One('gesre.cliente', string="Cliente") 