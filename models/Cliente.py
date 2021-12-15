# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Cliente(models.Model):
    _name = 'gesre.cliente'
    _inherit = 'res.users'

    fechaRegistro = fields.Date.today(string="Fecha de Registro", required=True)
