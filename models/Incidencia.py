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
   