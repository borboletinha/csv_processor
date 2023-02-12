from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
import logging

from deals.serializers import FileSerializer, DealSerializer
from deals.utils import export_deals_in_db, handle_data_queryset

logging.basicConfig(level=logging.INFO)


class DealView(GenericViewSet):

    queryset = handle_data_queryset()

    def get_serializer_class(self):
        if self.action == 'list':
            return DealSerializer
        else:
            return FileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            file = request.FILES['deals']
            try:
                export_deals_in_db(file)
            except Exception as exception:
                return Response(
                    f'Status: Error, Desc: {exception} - в процессе обработки файла произошла ошибка', status=400)
            else:
                return Response({'Status: OK - файл был обработан без ошибок'}, status=201)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response({'response': serializer.data})
