# -*- coding: utf-8 -*-
from odoo import fields, models, api
import time


class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', string='Customer')
    book_id = fields.Many2one('library.book', string='Book')

    rental_date = fields.Date(required=True)
    return_date = fields.Date(required=True)

    customer_address = fields.Text(related='customer_id.address')
    customer_email = fields.Char(related='customer_id.email')

    book_authors = fields.Many2many(related='book_id.author_ids')
    book_edition_date = fields.Date(related='book_id.edition_date')
    book_publisher = fields.Many2one(related='book_id.publisher_id')
    state = fields.Selection([('open', "Open"), ('closed', 'Closed'), ('late', 'Late')], default='open')
    date = fields.Date(default=fields.Date.today)

    """@api.depends('return_date')
    def _islate(self):
        for r in self:
            if r.date>=r.return_date:
                r.state='late'
            else:
                pass"""