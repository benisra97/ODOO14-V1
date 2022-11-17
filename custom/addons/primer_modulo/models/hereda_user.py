from odoo import fields, models

class forma_ini(models.Model):
        _inherit = 'res.users'

        iniciales_user= fields.Char(string="Iniciales")

