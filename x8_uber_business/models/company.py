# -*- coding: utf-8 -*-
from openerp import models, fields, api

class x8_uber_company(models.Model):
	_inherit = 'res.company'

	cuenta_sftp = fields.Char(string="Cuenta SFTP")
	puerto_sftp = fields.Integer(string="Puerto SFTP")
	dominio = fields.Char(string="Dominio")
	folder_destino = fields.Char(string="Folder destino")