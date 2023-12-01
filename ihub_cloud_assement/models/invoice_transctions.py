from odoo import fields, models, api , _
from odoo.exceptions import  ValidationError

class invoice_transtions(models.Model):
    """this manages all invoice transtions in the erp"""
    _name = "invoice_transtions.model"
    _inherit =["mail.thread","mail.activity.mixin"]
    _description = "Invoice Transaction Record"
    _order="id desc"
    _rec_name="creditor_name"

    invoice_lines = fields.One2many('growers_invoices.model', 'invoice_transtions_id', string="Invoice ID",)
    creditors_no = fields.Many2one('creditors.model', string="Creditor No.")
    sale_date = fields.Datetime(string="Sale Date")
    invoice_total = fields.Monetary(string="Invoice Total" , compute='_compute_total')
    currency_id = fields.Many2one('res.currency' ,string="Currency Id")
    creditor_name = fields.Char(related="creditors_no.creditor_name", string="Transport Name")
    creditor_id= fields.Char(related="creditors_no.creditor_no", string="Transport Name")
    season = fields.Selection(
        default='2023',
        string='Season',
        selection=[
            ('2023', '2023'),
            ('2024', '2024')])

    def _compute_total(self):
        # computes total in invoice lines and write to invoice_total
        invoice_total=0
        for record in self:
            for rec in record.invoice_lines:
                invoice_total=invoice_total+rec.amount_charged
            record.invoice_total=invoice_total
