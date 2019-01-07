# -*- coding: utf-8 -*-

from odoo import fields, models, api

class company(models.Model):
    _inherit = 'res.partner'

    supplier_code = fields.Char()
    name = fields.Char()
    name_local = fields.Char()
    short_name_en_us = fields.Char()
    short_name_local = fields.Char()
    company_currency = fields.Char()
    company_country = fields.Char()
    is_drs_company = fields.Boolean()
    is_supplier = fields.Boolean()
    official_registration_number = fields.Char()
    bank_name = fields.Char()
    bank_branch_name = fields.Char()
    bank_account_code = fields.Char()
    bank_account_name = fields.Char()


class product(models.Model):
    _inherit = "product.template"

    # BASIC INFORMATION

    refinfo_ids = fields.One2many('drs.refinfo', 'product_name')
    company_code = fields.Char()
    product_name_chi = fields.Char()
    product_category = fields.Char()
    brand_name_eng = fields.Char()
    brand_name_chi = fields.Char()
    drs_product_code = fields.Char()
    sup_product_code = fields.Char()
    mlt = fields.Integer()
    allergy_warning = fields.Boolean()
    product_material_percentage = fields.Char()
    product_link = fields.Char()

    # COMPLIANCE INFORMATION
    countryoforigin = fields.Char()
    medicaldevice = fields.Boolean()
    wireless = fields.Char()
    otherwireless = fields.Char()
    hscode = fields.Char()
    importexport = fields.Char()
    containmaterial = fields.Char()
    potentialhazards = fields.Char()


class refinfo(models.Model):
    _name = 'drs.refinfo'

    product_name = fields.Many2one('product.template')
    filename = fields.Char()
    link = fields.Char()
    type = fields.Char()
    appliedVariationProduct = fields.Char()
    applicableRegion = fields.Char()
    description = fields.Text()


class purchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_id')
    def onchange_product_list(self):
        return {'domain': {'product_id': [('sup_product_code', '=', self.partner_id.supplier_code)]}}
