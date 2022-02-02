# -*- coding: utf-8 -*-

from odoo import models, fields, api
# from odoo.addons.sale_stock.models.sale_order import SaleOrder as GSSalesCustom

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('company_id')
    def _onchange_company_id(self):
        self.warehouse_id = False