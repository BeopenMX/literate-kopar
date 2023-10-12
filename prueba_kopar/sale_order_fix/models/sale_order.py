from odoo import fields, models,_

class SaleOrder(models.Model):
    _inherit="sale.order"

    state = fields.Selection(
        selection_add=[('verificacióncalidad', 'Verificación de Calidad')]
    )
    
    def action_confirm(self):
        res = super().action_confirm()
        self.update({
            "state": "verificacióncalidad"
        })
        return res

    def action_button_comprobacion_calidad(self):
        self.update({
            "state": "done"
        })
        