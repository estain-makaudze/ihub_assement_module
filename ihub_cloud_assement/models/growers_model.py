from odoo import fields, models, api , _
from odoo.exceptions import  ValidationError

class growers_database(models.Model):
	"""this manages all growers into the systme"""
	_name = "growers.model"
	_inherit =["mail.thread","mail.activity.mixin"]
	_description = "Grower Database"
	_order="id desc"
	_rec_name="name"


	name = fields.Char(required=True ,string="Name")
	first_name = fields.Integer(string="First Name")
	surname= fields.Char(string="Surname")
	grower_no=fields.Char(string="Grower No",readonly=True,required=True,copy=False,default=lambda self: _('New'))
	selling_point= fields.Char(string="Selling Point")
	initials= fields.Char(string="Initials")
	national_id= fields.Char(string="National Id")
	telephone_landline= fields.Char(string="Telephone Landline")
	cellphone_number= fields.Char(string="Cellphone Number")
	grower_type = fields.Selection(
		default='g',
		string='Grower Type',
		selection=[
			('g', 'G'),
			('h', 'H')])
	farm_name= fields.Char(string="Farm Name")
	postal_address_1= fields.Char(string="Postal Address 1")
	postal_address_2= fields.Char(string="Postal Address 2")
	district= fields.Char(string="District")
	grower_area= fields.Char(string="Grower Area")
	grower_class= fields.Char(string="Grower Class")
	next_registration= fields.Char(string="Next Registration")
	season = fields.Selection(
		default='2023',
		string='Grower Type',
		selection=[
			('2023', '2023'),
			('2024', '2024')])
	email= fields.Char(string="Email")
	association = fields.Selection(
		default='self',
		string='Association',
		selection=[
			('self', 'SELF')])
	barn_type=fields.Char(string="Barn Type")
	date_amended=fields.Datetime(string="Date Amended")
	amend_type=fields.Char(string="Amend Type")
	contractor=fields.Char(string="Contractor")
	hectors=fields.Integer(string="Hectors")
	area_2=fields.Integer(string="Area_2")
	province = fields.Selection(
		default='mashonaland_central',
		string='Grower Type',
		selection=[
			('mashonaland_central', 'Mashonaland Central'),
			('mashonaland_east', 'Mashonaland East'),
			('mashonaland_west', 'Mashonaland West'),
			('manicaland', 'Manicaland'),
			('midlands', 'Midlands'),
			('masvingo', 'Masvingo'),
			('matabeleland_north', 'Matabeleland North'),
			('matabeleland_south', 'Matabeleland South')])
	landholding = fields.Char(string="landholding")
	obligations_fullfilled = fields.Char(string="Obligations Fullfilled")
	date_amended = fields.Char(string="Date Amended")

	@api.model
	def create(self,vals):
		# AUTO GROWER NUMBER SEQUENCING
		if vals.get('grower_no', _('New')) == _('New'):
			vals['grower_no']=self.env['ir.sequence'].next_by_code('grower_no.seq') or _('New')
		res= super(growers_database,self).create(vals)
		return res






