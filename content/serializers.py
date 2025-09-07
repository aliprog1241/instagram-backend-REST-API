from rest_framework import serializers





class TagSerializer(serializers.Serializer):
    title = serializers.CharField()
    id = serializers.IntegerField()

