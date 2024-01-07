from rest_framework import serializers

from electronics_network.models import Company, Contact, Product


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('debt',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CompanyDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    provider = CompanySerializer(many=True, read_only=True)
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Company
