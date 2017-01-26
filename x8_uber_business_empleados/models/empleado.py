# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class x8_uber_empleado(models.Model):

	_inherit = ['hr.employee']

	can_use_uber = fields.Boolean(string="Puede usar Uber", default=False)
	
	@api.model
	def create(self, vals):
		employee = super(x8_uber_empleado, self).create(vals)
		self.sincroniza()
		return employee

	@api.multi
	def write(self, vals):
		employee = super(x8_uber_empleado, self).write(vals)
		self.sincroniza()
		return employee

	@api.model
	def sincroniza(self):
		usuarios = self.env['hr.employee'].search([('can_use_uber','=', True)])
		for usuario in usuarios:
			_logger.info(usuario.name)
			_logger.info(usuario.work_email)
			_logger.info(usuario.id)