from django.urls import path

from .views import *


urlpatterns = [
    path('ukraine', UkrainePage.as_view(), name='ukraine'),
    path('bodis', BodisPage.as_view(), name='bodis'),

    path('api/free_domains/', UkraineFreeDomains.as_view(), name='ukraine_free_domains'),
    path('api/check_domain/', UkraineCheckDomain.as_view(), name='check_domain'),
    path('api/registr_domain/', UkraineRegistrDomain.as_view(), name='registr_domain'),
    path('api/get_invoices/', UkraineGetInvoices.as_view(), name='get_invoices'),
    path('api/cancel_invoices/', UkraineCancelInvoice.as_view(), name='cancel_invoices'),
    path('api/pay_invoice_balance/', UkraineInvoicePayBalance.as_view(), name='pay_invoice_balance'),
    path('api/add_domains_bodis', BodisAddDomains.as_view(), name='add_domains_bodis')
]