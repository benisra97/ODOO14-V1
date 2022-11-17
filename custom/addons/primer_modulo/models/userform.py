from odoo import fields, models

class Userform(models.Model):
        _inherit = 'res.partner'

        iniciales_= fields.Char(string="Iniciales")

