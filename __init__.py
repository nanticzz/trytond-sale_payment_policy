#This file is part sale_payment_policy module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.pool import Pool
from .sale import *

def register():
    Pool.register(
        SalePaymentPolicy,
        SaleShop,
        Sale,
        module='sale_payment_policy', type_='model')
