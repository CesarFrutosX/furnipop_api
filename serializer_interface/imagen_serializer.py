from rest_framework import serializers

from furnipop_api.models import Imagen

class ImagenSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    url = serializers.SerializerMethodField()

    def get_url(self, instance : Imagen):
        return ""+self.hostName+instance.src.url

    class Meta:
        model = Imagen
        fields = '__all__'