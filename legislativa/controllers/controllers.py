# -*- coding: utf-8 -*-
# from odoo import http


# class Legislativa(http.Controller):
#     @http.route('/legislativa/legislativa', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/legislativa/legislativa/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('legislativa.listing', {
#             'root': '/legislativa/legislativa',
#             'objects': http.request.env['legislativa.legislativa'].search([]),
#         })

#     @http.route('/legislativa/legislativa/objects/<model("legislativa.legislativa"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('legislativa.object', {
#             'object': obj
#         })
