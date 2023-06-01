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
from odoo.exceptions import ValidationError

class pruebas(models.Model):
     _name = 'pruebas.pruebas'
     _description = 'probando'

     
     
     name = fields.Char(string='Nombre', required=True)
     age = fields.Integer(string='Edad', required=True)
     altura = fields.Float(string='Altura', required=True)
     voto = fields.Selection(selection=[('s','Si'),('n','No')], string="¿Vas a votar?", required=True)
     voto2 = fields.Boolean(string='Voto en blanco')
     voto3 = fields.Boolean(string='Prefiero no decirlo')
     voto4 = fields.Boolean(string='Candidato')

     @api.constrains('age')
     def _check_age(self):
        for record in self:
            if record.age <= 16:
                raise ValidationError('La edad debe ser mayor de 16 años.')

    
     @api.onchange('name')
     def action_test(self):
         self.name = "Facundo Alaniz"

     
           


class votacion(models.TransientModel):
    _name = 'pruebas.votacion'

    
    voto = fields.Selection(selection=[('c1','Candidato 1'),('c2','Candidato 2') , ('c3' , 'Candidato 3')], string="Candidatos", required=True)

    



#
# class votacion(models,Model):
 #   _name = 'pruebas.votacion'
  #  _description = 'Votacion' 




     
         





