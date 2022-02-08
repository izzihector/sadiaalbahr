from odoo import models, fields, api
from num2words import num2words

class JournalItem(models.Model):
    _inherit = 'account.move.line'
    sequence_number = fields.Integer('Number')

class JournalEntry(models.Model):
    _inherit = 'account.move'

    def compute_amount_in_word2(self,amount):
        if self.env.user.lang == 'en_US':
            num_word = str(self.currency_id.amount_to_text(amount)) + ' only'
            return num_word
        elif self.env.user.lang == 'ar_001':
            num_word = num2words(amount, to='currency', lang=self.env.user.lang)
            num_word = str(num_word) + ' فقط'
            return num_word

    # def amount_text_arabic(self,amount):
    #     return amount_to_text_arabic(amount, self.company_id.currency_id.name)