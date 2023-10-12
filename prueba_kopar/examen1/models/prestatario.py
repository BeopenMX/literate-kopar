from odoo import fields, models,_

class Prestatario(models.Model):
    _name="prestatario"

    nombre = fields.Char()
    email = fields.Char()
    teléfono = fields.Char()
