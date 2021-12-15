# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Cliente(models.Model):
    _name = 'cliente.cliente'

    fechaRegistro = fields.Date(string="Fecha de Registro", required=True)
