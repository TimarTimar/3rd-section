# -*- coding: utf-8 -*-
from odoo import fields, models


class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', string='Customer')
    cbook_id = fields.Many2one('library.cbook', string='CBook')

    rental_date = fields.Date()
    return_date = fields.Date()

    customer_address = fields.Text(related='customer_id.address')
    customer_email = fields.Char(related='customer_id.email')

    book_authors = fields.Many2many(related='cbook_id.author_ids')
    book_edition_date = fields.Date(related='cbook_id.edition_date')
    book_publisher = fields.Many2one(related='cbook_id.publisher_id')
