# -*- coding: utf-8 -*-
from odoo import http

# class DrsProductViews(http.Controller):
#     @http.route('/drs_module/drs_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/drs_module/drs_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('drs_module.listing', {
#             'root': '/drs_module/drs_module',
#             'objects': http.request.env['drs_module.drs_module'].search([]),
#         })

#     @http.route('/drs_module/drs_module/objects/<model("drs_module.drs_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('drs_module.object', {
#             'object': obj
#         })