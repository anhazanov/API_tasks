from django.views import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import BaseUtils, ApiUtils


class UkrainePage(View, BaseUtils):
    context = {}

    def get(self, request):
        return render(request, 'backend_api/ukraine.html', context=self.context)

    def post(self, request):
        # write API token
        if request.POST.get('API_token'):
            self.write_api_token('api_token_ukraine', request.POST.get('API_token'))

        if request.POST.get('free_domains'):
            params = {
                'by': 'desc',
                'sort': 'trust'
            }
            headers = {'Content-Type': 'application/json',
                       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)",
                       'Authorization': 'Bearer ' + self.read_api_token().get("api_token_ukraine")}
            response = ApiUtils.send_post_request('https://adm.tools/action/domain/expired/load',
                                                  params=params, headers=headers)
            print(response['response'].get('list')[0])

        return render(request, 'backend_api/ukraine.html', context=self.context)


class BodisPage(View, BaseUtils):
    context = {}

    def get(self, request):
        return render(request, 'backend_api/bodis.html', context=self.context)

    def post(self, request):
        if request.POST.get('API_token_bodis'):
            self.write_api_token('api_token_bodis', request.POST.get('API_token_bodis'))

        return render(request, 'backend_api/bodis.html', context=self.context)


def headers_ukraine(username: str):
    return {'Content-Type': 'application/json',
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)",
            'Authorization': 'Bearer ' + BaseUtils.read_api_token(username).api_ukraine}


class UkraineFreeDomains(APIView):
    def get(self, request):
        url = 'https://adm.tools/action/domain/expired/load/'
        params = {
            'by': 'desc',
            'sort': 'trust'
        }
        response = ApiUtils.send_post_request(url=url, params=params, headers=headers_ukraine(request.user.username))
        output = [
            {
                'name': output.get('name'),
                'id': output.get('id'),
                'expired_dtime': output.get('expired_dtime'),
                'trust': output.get('trust')
            } for output in response['response'].get('list')
        ]
        return Response(output)


class UkraineCheckDomain(APIView):
    # def get(self, request):
    #     print(request.GET.get('domain'))
    #     url = 'https://adm.tools/action/domain/check/'
    #     params = {'domain': request.GET.get('domain')}
    #     response = ApiUtils.send_post_request(url=url, params=params, headers=headers_ukraine(request.user.username))
    #     print(response)
    #     return Response("Домен свободен" if response and response.get('result') else 'Домен занят')

    def post(self, request):
        print(request.data)
        print(request.POST)
        url = 'https://adm.tools/action/domain/check/'
        params = {'domain': request.data.get('domain')}
        response = ApiUtils.send_post_request(url=url, params=params, headers=headers_ukraine(request.user.username))
        return Response("Домен свободен" if response and response.get('result') else 'Домен занят')


class UkraineRegistrDomain(APIView):
    def get(self, request):
        return Response({})

    def post(self, request):
        url = 'https://adm.tools/action/domain/register/'
        params = {'domain': request.data['registr'].get('domain'),
                  'period': request.data['registr'].get('period', 1)}
        response = ApiUtils.send_post_request(url=url, params=params, headers=headers_ukraine(request.user.username))
        if response.get('result'):
            return Response({
                'domain': response['response']['domain'].get('name'),
                'price': f"{response['response']['invoice'].get('sum')} {response['response']['invoice'].get('currency')}"
            })
        else:
            return Response({'domain': request.data['registr'].get('domain'), 'price': ""})


class UkraineGetInvoices(APIView):
    def get(self, request):
        url = 'https://adm.tools/action/billing/get_invoices/'
        response = ApiUtils.send_get_request(url=url, headers=headers_ukraine(request.user.username))
        return Response(response['response'].get('list') if response.get('result') else [])


class UkraineCancelInvoice(APIView):
    def get(self, request):
        return Response({})

    def post(self, request):
        url = 'https://adm.tools/action/billing/invoice_cancel/'
        params = {'invoice_id': request.data.get('id')}
        response = ApiUtils.send_post_request(url=url, params=params, headers=headers_ukraine(request.user.username))
        return Response(response.get('result'))


class UkraineInvoicePayBalance(APIView):
    def post(self, request):
        url = 'https://adm.tools/action/billing/invoice_pay_from_balance/'
        params = {'invoice_id': int(request.data.get('id')),
                  "token": " "}
        # 'token': 'Bearer ' + BaseUtils.read_api_token().get("api_token_ukraine")}
        response = ApiUtils.send_post_request(url=url, params=params, headers=headers_ukraine(request.user.username))
        print(response)
        return Response(response)


def headers_bodis(username: str):
    return {'Content-Type': 'application/json',
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)",
            'Authorization': 'Bearer ' + BaseUtils.read_api_token(username).api_bodis}


class BodisAddDomains(APIView):
    def post(self, request):
        print(request)
        url = 'https://api.bodis.com/v2/domains'
        if '.com' in request.data[0]:
            return Response(True)
        else:
            return Response(False)
