# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, _, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    prepayment_ok = fields.Boolean(
        string=_('Advance Invoice'),
    )

    @api.multi
    def action_move_create(self):
        res = super(AccountInvoice, self).action_move_create()
        if self.type == 'out_invoice':
            for line in self.invoice_line_ids:
                product = line.product_id.id
                deposit = self.pool['ir.values'].get_default(
                    self._cr, self._uid, 'sale.config.settings',
                                         'deposit_product_id_setting') or False
                if product == deposit:
                    self.prepayment_ok = True
                else:
                    self.prepayment_ok = False

        return res
