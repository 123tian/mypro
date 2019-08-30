
from rest_framework import serializers

from .models import Publisher
class PublisherSerializer(serializers.ModelSerializer):
    # operator = serializers.SerializerMethodField(source='operator.username')
    operator = serializers.ReadOnlyField(source='operator.username')
    class Meta:
        model= Publisher
        fields = "__all__"
        # model = Publisher#我们要使用的模型类
        # fields = [
        #     'id',
        #     'name',
        #     'address'
        # ]
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    # address = serializers.CharField()
    #
    #
    # def create(self, validated_data):
    #     """新建数据到数据库"""
    #     return Publisher.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     #instance要修改的模型类
    #     instance.name = validated_data.get('name',instance.name)
    #
    #     instance.address = validated_data.get('address',instance.address)
    #     instance.save()
    #     return instance
