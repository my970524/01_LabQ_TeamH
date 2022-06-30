from dataclasses import fields

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import SewerPipe, Rainfall, GuName


class SewerPipeModelSerializer(ModelSerializer):
    '''
    Assignee : 민지
    데이터 출력 예시와 동일하게 고유번호, 측정 수위 필드만 출력
    '''
    class Meta:
        model = SewerPipe
        fields = ['idn', 'mea_wal']

class RainfallModelSerializer(ModelSerializer):
    '''
    Assignee : 민지
    데이터 출력 예시와 동일하게 강우량계명, 10분우량 필드만 출력
    '''
    class Meta:
        model = Rainfall
        fields = ['raingauge_name', 'rainfall10']


class GuNameModelSerializer(ModelSerializer):
    rainfall_data = serializers.SerializerMethodField()
    rainfall_set = RainfallModelSerializer(many=True)
    sewerpipe_set = SewerPipeModelSerializer(many=True)

    def get_rainfall_data(self, obj):
        rainfalls = obj.rainfall_set
        datetime = self.context["datetime"]

        return {
            "last_review": RainfallModelSerializer(rainfalls.filter()).data,
        }

    class Meta:
        model = GuName
        fields = ["gubn", "name", "rainfall_set", "sewerpipe_set"]