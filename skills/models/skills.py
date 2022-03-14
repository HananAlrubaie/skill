import base64
import logging
import json

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError, AccessError , Warning
from odoo.modules.module import get_module_resource


class Skillslist(models.Model):

    _name = 'skills.list'
    _description = ''

    with open('/home/hanan/erp1/coretamkeenerp/custom/skills/data/skills.json') as f:
        FIELD_TYPES = list()
        for key in f:
            key = key.replace("\"", "")
            key = key.replace(",", "")
            FIELD_TYPES.append((key,key))
        FIELD_TYPES.pop(0)
        FIELD_TYPES.pop(2633)

    Skills = fields.Selection(selection=FIELD_TYPES, string='Employee Skills')


class Employeeskill(models.Model):

    _inherit = 'hr.employee'

    empskill = fields.Many2one('skills.list','Employee skills')














