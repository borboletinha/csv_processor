from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    deals = serializers.FileField()


class DealSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200, source='customer')
    spent_money = serializers.IntegerField()
    gems = serializers.ListField(child=serializers.CharField(max_length=200))
