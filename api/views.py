import csv
import codecs
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Deal


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(
        operation_description='Upload a file',
        manual_parameters=[
            openapi.Parameter(
                name='deals',
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                required=True,
                description='File containing deal history',
            ),
        ],
        responses={
            200: openapi.Response(description='File processed successfully'),
            400: openapi.Response(description='Error occurred during file processing'),
        }
    )

    def post(self, request, format=None):
        file_obj = request.FILES.get('deals')

        try:
            # Чтение файла CSV с указанием кодировки
            reader = csv.reader(codecs.iterdecode(file_obj, 'utf-8'))
            next(reader)  # Пропустить заголовок
            
            # Создание экземпляров модели на основе данных из файла
            for row in reader:
                customer = row[0]
                item = row[1]
                total = float(row[2])
                quantity = int(row[3])
                date = row[4]
                
                deal = Deal.objects.create(
                    customer=customer,
                    item=item,
                    total=total,
                    quantity=quantity,
                    date=date
                )
            
            return Response(status=200, data={'status': 'OK'})
        except Exception as e:
            return Response(status=400, data={'status': 'Error', 'desc': str(e)})


class ProcessedDataView(APIView):
    def get(self, request, format=None):
        # Получение данных для обработки
        deals = Deal.objects.all()

        # Вычисление суммы потраченных средств для каждого клиента
        spent_money_by_customer = {}
        for deal in deals:
            if deal.customer not in spent_money_by_customer:
                spent_money_by_customer[deal.customer] = 0
            spent_money_by_customer[deal.customer] += deal.total

        # Сортировка клиентов по сумме потраченных средств
        sorted_customers = sorted(spent_money_by_customer.items(), key=lambda x: x[1], reverse=True)

        top_customers = sorted_customers[:5]

        gems = set()
        for customer, _ in top_customers:
            customer_deals = deals.filter(customer=customer)
            for deal in customer_deals:
                if deals.filter(item=deal.item).count() >= 2:
                    gems.add(deal.item)

        response_data = []
        for customer, spent_money in top_customers:
            customer_gems = [gem for gem in gems if deals.filter(customer=customer, item=gem).exists()]
            response_data.append({
                'username': customer,
                'spent_money': spent_money,
                'gems': customer_gems
            })

        return Response({'response': response_data})
