from rest_framework.response import Response
from rest_framework.views import APIView

from football.models import FootballField, Config, ImageForFootballField
from .serializers import FootballFieldSerializer, ConfigSerializer, ImageSerializer


class GetConfigView(APIView):
    def get(self, *args, **kwargs):
        return Response(Config.get_cfg())


class FootballFieldView(APIView):
    def get(self, *args, **kwargs):
        football_fields = FootballField.objects.all()
        serialized_data = FootballFieldSerializer(football_fields, many=True)
        return Response(serialized_data.data)


class ImageView(APIView):
    def get(self, *args, **kwargs):
        images = ImageForFootballField.objects.all()
        serialized_data = ImageSerializer(images, many=True)
        return Response(serialized_data.data)


class FilterAreaAPI(APIView):
    """Фильтр по локации поля"""
    def get(self, *args, **kwargs):
        filter_data = FootballField.objects.filter(address=kwargs["area"])
        serialized_data = FootballFieldSerializer(filter_data, many=True)
        return Response(serialized_data.data)


class FilterSizeAPI(APIView):
    """Фильтр по размеру поля"""
    def get(self, *args, **kwargs):
        filter_data = FootballField.objects.filter(size=kwargs["size"])
        serialized_data = FootballFieldSerializer(filter_data, many=True)
        return Response(serialized_data.data)
