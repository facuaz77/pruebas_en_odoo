# -*- coding: utf-8 -*-




# class pruebas(models.Model):
#     _name = 'pruebas.pruebas'
#     _description = 'pruebas.pruebas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100



from odoo import models, fields, api

class pruebas(models.Model):
     _name = 'pruebas.pruebas'
     _description = 'probando'
     
     name = fields.Char(string='Nombre', required=True)
     age = fields.Integer(string='Edad', required=True)
     altura = fields.Float(string='Altura', required=True)
     voto = fields.Selection(selection=[('s','Si'),('n','No')], string="¿Vas a votar?", required=True)
     voto2 = fields.Boolean(string='Si')
     voto3 = fields.Boolean(string='No')


