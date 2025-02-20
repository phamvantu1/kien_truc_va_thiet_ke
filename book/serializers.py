from bson import ObjectId
from rest_framework import serializers
from .models import Book  # Import model của bạn

class BookSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)  # Chuyển ObjectId thành string

    class Meta:
        model = Book
        fields = '__all__'  # Hoặc chỉ định các trường cụ thể

    def to_representation(self, instance):
        """Chuyển ObjectId về string để tránh lỗi"""
        rep = super().to_representation(instance)
        rep['_id'] = str(instance._id) if isinstance(instance._id, ObjectId) else instance._id
        return rep
