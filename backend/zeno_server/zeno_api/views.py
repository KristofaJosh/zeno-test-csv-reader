from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from .models import ZenoCsv
from .serializers import ZenoCsvSerializer, ZenoCsvUploadSerializer
import pandas as pd


# Create your views here.
class ZenoCsvViewSet(viewsets.ModelViewSet):
    serializer_class = ZenoCsvSerializer
    queryset = ZenoCsv.objects.all()


class ZenoFileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def put(self, request, *args, **kwargs):

        file_obj = request.data['file']

        csv_data = pd.read_csv(file_obj)
        dataframe = pd.DataFrame(csv_data, columns=['id', 'timestamp', 'temperature', 'duration'])

        for row in dataframe.itertuples():
            fields = {'idd': row.id, 'timestamp': row.timestamp, 'temperature': row.temperature, 'duration': row.duration}
            print(fields)
            data_serializer = ZenoCsvSerializer(data=fields)
            if data_serializer.is_valid():
                data_serializer.save()

                # return Response(data_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

