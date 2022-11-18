from odoo import fields, models, api

class Project(models.Model):
        _inherit = 'sale.order.line'

        new_field = fields.Char( string='Unidad')
        costo_unitario = fields.Integer(string="Costo U")
        porcentaje_comi= fields.Float(string="% Comision")
        discount_total = fields.Char(string="sd")
        tiempo_entrega = fields.Integer(string="Tiempo de entrega")

        #ini_id_mio=fields.Many2one('res.users')
       # ini_user=fields.Char(related="ini_id_mio.iniciales_user")

        total_sd = fields.Float(string="Total S/D", compute="compute_field", store=True)
        pu_cd = fields.Float(string="Precio unitario C/D", compute="compute_field", store=True)
        utilidad_ = fields.Float(string="Utilidad", compute="compute_field", store=True)
        comision = fields.Float(string="Comision", compute="compute_field", store=True)
        multi_pu = fields.Float(string="*")

        @api.depends('total_sd','pu_cd','utilidad_','comision','costo_unitario','porcentaje_comi','discount_total','multi_pu')
        def compute_field(self):
            for rec in self:
             rec.price_unit = rec.costo_unitario * rec.multi_pu
             rec.total_sd = rec.product_uom_qty * rec.price_unit
             rec.pu_cd = rec.price_unit-(rec.price_unit*(rec.discount/100))
             rec.utilidad_= (rec.pu_cd*rec.product_uom_qty)-(rec.costo_unitario*rec.product_uom_qty)
             rec.comision= rec.utilidad_*(rec.porcentaje_comi/100)

            self._cr.execute(""" select od.vendedor_ini,sum(ol.comision)
                                                  from public.sale_order od
                                                  inner join public.sale_order_line ol
                                                  on od.id = ol.order_id
                                                  where od.estado_pago='yes_paid'
                                                  and od.create_date BETWEEN (now() - INTERVAL '7 days') AND now()
                                                  group by od.vendedor_ini""")
            data = self._cr.dictfetchall()
            print(data)




