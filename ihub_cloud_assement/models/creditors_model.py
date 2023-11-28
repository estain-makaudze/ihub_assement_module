from odoo import fields, models, api , _
from odoo.exceptions import  ValidationError

class creditors_database(models.Model):
    """this manages all creditors in the erp"""
    _name = "creditors.model"
    _inherit =["mail.thread","mail.activity.mixin"]
    _description = "Creditor Record"
    _order="id desc"
    _rec_name="name"

    invoice_lines = fields.One2many('growers_invoices.model', 'creditors_id', string="Invoice ID",)

    name = fields.Char(required=True ,string="Name")
    creditor_no = fields.Char(string="Creditor No", readonly=True, required=True, copy=False, default=lambda self: _('New'))
    creditor_ref = fields.Char(string="Creditor Ref")
    creditor_acc_no = fields.Char(string="Creditor Account No")
    creditor_name = fields.Char(string="Creditor Name")
    creditor_add_1 = fields.Char(string="Creditor Address 1")
    creditor_add_2 = fields.Char(string="Creditor Address 2")
    creditor_add_3 = fields.Char(string="Creditor Address 3")
    creditor_type= fields.Char(string="Creditor Type")
    business_type= fields.Char(string="Business Type")
    creditor_old_no= fields.Char(string="Creditor Old No")
    creditor_address_from_timb= fields.Boolean(string="Creditor Address from TIMB")
    cellphone_no= fields.Char(string="Cellphone #")
    season = fields.Selection(
        default='2023',
        string='Grower Type',
        selection=[
            ('2023', '2023'),
            ('2024', '2024')])

    @api.model
    def create(self, vals):
        # AUTO CREDITORS NUMBER SEQUENCING
        if vals.get('creditor_no', _('New')) == _('New'):
            vals['creditor_no'] = self.env['ir.sequence'].next_by_code('creditor_no.seq') or _('New')
        res = super(creditors_database, self).create(vals)
        return res

class growers_invoices(models.Model):
    """this manages all growers invoices with one2many with creditors model relationship"""
    _name = "growers_invoices.model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Growers Invoice Record"
    _order = "id desc"
    _rec_name = "grower_name"

    creditors_id= fields.Many2one('creditors.model', string="Grower")
    grower_id= fields.Many2one('growers.model', string="Grower")
    grower_name= fields.Char(string="Grower Name", related='grower_id.name')
    number_of_bales= fields.Integer(string="Number of Bales")
    amount_charged= fields.Monetary(string="Amount Charged")
    currency_id=fields.Many2one('res.currency')
    amount_paid=fields.Monetary(string="Amount Paid")
    #add created by

