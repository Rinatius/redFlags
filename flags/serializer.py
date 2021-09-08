from rest_framework import serializers

from flags.models import Tender, Lot, Entity, Bid, Irregularity, Flag, Classifier


class TenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tender
        fields = '__all__'


class LotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lot
        fields = '__all__'


class EntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity
        fields = '__all__'


class BidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = '__all__'


class IrregularitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Irregularity
        fields = '__all__'


class FlagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flag
        fields = '__all__'


class ClassifierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classifier
        fields = '__all__'
