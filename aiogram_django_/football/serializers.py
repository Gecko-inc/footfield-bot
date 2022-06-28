from rest_framework.serializers import ModelSerializer

from football.models import FootballField, Config, ImageForFootballField


class FootballFieldSerializer(ModelSerializer):
    class Meta:
        model = FootballField
        fields = "__all__"


class ConfigSerializer(ModelSerializer):
    class Meta:
        model = Config
        fields = "__all__"


class ImageSerializer(ModelSerializer):
    class Meta:
        model = ImageForFootballField
        fields = "__all__"
