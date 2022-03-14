import base64
import logging
import json

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError, AccessError , Warning
from odoo.modules.module import get_module_resource


class EmployeeSkills(models.Model):

    _name = "emp.skills"
    _description = ''

    # with open('/home/hanan/erp1/coretamkeenerp/custom/empSkills/data/skillslist.json') as f:
    #     FIELD_TYPES = list()
    #     for key in f:
    #         key = key.replace("\"", "")
    #         key = key.replace(",", "")
    #         FIELD_TYPES.append((key,key))
    #     FIELD_TYPES.pop(0)
    #     FIELD_TYPES.pop(2633)

    # skills = fields.Selection(selection=FIELD_TYPES, string='Employee Skills')
    proficiency = fields.Selection([('Intermediate','Intermediate'),('Advanced','Advanced'),('Expert','Expert')], string='Proficiency level')
    certification = fields.Selection([('active','active'),('expired','expired'),('pending','pending'),('suspended','suspended'),('temporary','temporary')] ,string='Certification Status ')
    employees = fields.Many2one('hr.employee', 'Employee Name')
    skills = fields.Many2one('skills.list','Skills')
    empskill = fields.Char(string="Employee skills")

    @api.onchange('skills')
    def onchange_skills(self):
        if self.skills.Skills:
            self.skills = self.Skills


class Employeeskill(models.Model):

    _inherit = 'hr.employee'

    # empskill = fields.Many2one('emp.skills','Employee skills')
    skills = fields.Many2one('skills.list', 'Skills')
    empskill = fields.Char(string="Employee skills")


    @api.onchange('skillS')
    def onchange_email(self):
        if self.employees.skills:
            self.empskill = self.employees.skills







