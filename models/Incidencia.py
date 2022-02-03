# -*- coding: utf-8 -*-
from odoo import api
from odoo import exceptions
from odoo import fields
from odoo import models
 

class Incidencia(models.Model):
    _name = 'gesre.incidencia'
    
    id = fields.Integer(string="id")
    estrellas = fields.Integer(string="Estrellas", domain="[('Estrellas','>',0)]")
    horas = fields.Integer(string="Horas", domain="[('Horas','>',0)]")
    precio = fields.Float(string="Precio", domain="[('Precio','>',0)]")
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
    
    #Validacion
    @api.constrains('estrellas')
    def _check_estrellasNum(self):
        if self.estrellas > 5:
            raise exceptions.ValidationError("las Estrellas no pueden ser mas de 5")
    #Validacion
    @api.onchange('horas')
    def _check_horasNum(self):
        if self.horas > 99:
            return {'warning':{
                'title': "Incorrect 'Estrellas' value",
                'message': "el numero de horas no puede pasar de 99",
            },
            }
     #Validacion
    @api.constrains('horas')
    def _check_HorasNum_Save(self):
       if self.horas > 99:
            raise exceptions.ValidationError( "el numero de horas no puede pasar de 99")

            
