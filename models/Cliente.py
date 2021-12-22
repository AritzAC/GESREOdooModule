# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models

class Cliente(models.Model):
    _inherit = 'res.users'

    #Atributos
    #fechaRegistro = fields.Date.today(string="Fecha de Registro", required=True)
    #Relacion 1 a Muchos con Incidencia
    #incidencia = fields.One2Many('gesre.incidencia', 'cliente', string="Incidencia")
    