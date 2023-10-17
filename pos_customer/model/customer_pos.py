from odoo import fields, models


class PosCustomer(models.Model):
    _inherit = 'res.partner'

    customerid = fields.Char(string='Customer ID', store=True, readonly=False, required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('ذكر', 'ذكر'), ('أنثى', 'أنثى')], string='Gender')

    class PosSession(models.Model):
        _inherit = "pos.session"
        def _loader_params_res_partner(self):
            result = super()._loader_params_res_partner()
            result['search_params']['fields'].extend(['customerid', 'gender'])
            return result

def _pos_ui_models_to_load(self, params):
    return self.env['res.partner'].search_read(**params['search_params'])