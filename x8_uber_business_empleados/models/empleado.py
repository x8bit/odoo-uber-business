# -*- coding: utf-8 -*-
from openerp import models, fields, api, SUPERUSER_ID, _
from openerp.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class x8_uber_empleado(models.Model):

	_inherit = ['hr.employee']

	can_use_uber = fields.Boolean(string="Puede usar Uber", default=False)