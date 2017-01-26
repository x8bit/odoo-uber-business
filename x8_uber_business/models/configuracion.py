# -*- coding: utf-8 -*-
from openerp import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class x8_uber_settings(models.TransientModel):
	_inherit = 'account.config.settings'
	_name = 'x8.uber.config.settings'

	cuenta_sftp = fields.Char(string="Cuenta SFTP")
	puerto_sftp = fields.Integer(string="Puerto SFTP")
	dominio = fields.Char(string="Dominio")
	folder_destino = fields.Char(string="Folder destino")
	
	@api.model
	def get_default_company_values(self, fields):
		company = self.env.user.company_id
		_logger.info(company.id);
		_logger.info(company.name);
		
		return {
			'cuenta_sftp' : company.cuenta_sftp,
			'puerto_sftp' : company.puerto_sftp,
			'dominio' : company.dominio,
			'folder_destino' : company.folder_destino
		}
	
	@api.one
	def set_company_values(self):
		company = self.env.user.company_id
		company.cuenta_sftp = self.cuenta_sftp
		company.puerto_sftp = self.puerto_sftp
		company.dominio = self.dominio
		company.folder_destino = self.folder_destino
