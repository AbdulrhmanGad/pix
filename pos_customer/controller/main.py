# -*- coding: utf-8 -*-
import logging


_logger = logging.getLogger(__name__)
from odoo import http
from odoo.http import request
from odoo.addons.point_of_sale.controllers.main import PosController


class PosGender(PosController):
    @http.route(['/pos/ticket/validate'], type='http', auth="public", website=True, sitemap=False)
    def show_ticket_validation_screen(self, access_token='', **kwargs):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        res = super(PosGender, self).show_ticket_validation_screen(access_token, **kwargs)
        res.update({'genders': request.env['partner.gender'].sudo().search([]),})
        return res
