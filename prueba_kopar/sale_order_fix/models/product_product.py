from odoo import fields, models,_,api

class ProductProduct(models.Model):
    _inherit="product.product"

    new_cost_usd = fields.Monetary(
        compute='_compute_new_cost_usd'
    )

    @api.depends('standard_price')
    def _compute_new_cost_usd(self):
        if self.standard_price != 0.0:
            mx_currency_rate= self.env['res.currency'].search([
                ('name','=','MXN'),
            ]).rate
            self.new_cost_usd = mx_currency_rate * self.standard_price
        self.new_cost_usd =0.0