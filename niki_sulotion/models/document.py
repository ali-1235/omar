from odoo import models, api, fields, _


class DocumentNikki(models.Model):
    _name = 'document.nikki'
    _inherit = 'mail.thread'
    _rec_name = 'file_name'

    partner_id = fields.Many2one('res.partner', string='User', default=lambda self: self.env.user.partner_id.id)
    category_id = fields.Many2one('category.nikki', string='Category')
    file_data = fields.Binary('File')
    file_name = fields.Char('File Name')
    document_count = fields.Integer('document_count')


class CategoryDocument(models.Model):
    _name = 'category.nikki'

    name = fields.Char('Category Name')
