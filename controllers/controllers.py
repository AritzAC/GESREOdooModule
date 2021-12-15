# -*- coding: utf-8 -*-
from odoo import http

# class Gesre(http.Controller):
#     @http.route('/gesre/gesre/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gesre/gesre/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gesre.listing', {
#             'root': '/gesre/gesre',
#             'objects': http.request.env['gesre.gesre'].search([]),
#         })

#     @http.route('/gesre/gesre/objects/<model("gesre.gesre"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gesre.object', {
#             'object': obj
#         })