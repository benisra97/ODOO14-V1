from odoo import models, fields

class ProyectoStig(models.Model):
        _inherit = 'sale.order.line'


        clickcolor = fields.Integer(string='Click Color')
        clicknegro=fields.Integer(string='Click Negro')
        exccolor=fields.Integer(string='Excedente Color')
        excnegro= fields.Integer(string='Excedente Negro')

class ProyectoStig2(models.Model):
        _inherit = 'sale.order'
        terminos=fields.Selection([('serv','Servicio'),('rent','Renta'),('vent','Venta')], default='rent')
        vig_contrato = fields.Integer(string='Meses de vigencia')
        vendedor_ini = fields.Char(string="Iniciales del vendedor")

