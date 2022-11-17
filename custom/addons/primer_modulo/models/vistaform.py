from odoo import fields, models,api

class Vistaform(models.Model):
        _inherit = 'sale.order'

        entrega_tiempo = fields.Char(string="Tiempo de entrega")
        vendedor_ini = fields.Char(string="Iniciales del vendedor")
        estado_pago= fields.Selection([('not_paid','No pagado'),('yes_paid','Pagado')], default='not_paid')
        id_cotizacion = fields.Char(string="ID Cotizacion")

        def run_sql(self):
             self._cr.execute(""" select od.vendedor_ini,sum(ol.comision)
                                                  from public.sale_order od
                                                  inner join public.sale_order_line ol
                                                  on od.id = ol.order_id
                                                  where od.estado_pago='yes_paid'
                                                  and od.create_date BETWEEN (now() - INTERVAL '7 days') AND now()
                                                  group by od.vendedor_ini""")

             _res = self._cr.fetchall()
             return _res


