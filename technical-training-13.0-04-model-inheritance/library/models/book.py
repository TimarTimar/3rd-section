# -*- coding: utf-8 -*-
from odoo import fields, models


class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')

    author_ids = fields.Many2many("library.partner", string="Authors")
    edition_date = fields.Date()
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one('library.publisher', string='Publisher')
    cbook_ids = fields.One2many('library.cbook', 'name', string="Each uniqe book")

    #rental_ids = fields.One2many('library.rental', 'book_id', string='Rentals')


class cbook(models.Model):
    _name = 'library.cbook'
    _description = 'piece of books'

    _inherits = {
        'library.book': 'name',
    }

    book_reference = fields.Char(string='Reference number', required="True")

    book_id = fields.Many2one('library.book', ondelete="cascade")
