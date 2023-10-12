from odoo import fields, models,_

class Libro(models.Model):
    _name="libro"

    nombre = fields.Char()
    autor = fields.Char()
    isbn = fields.Char()
    fechapublicacion = fields.Date()

    