from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Sarlavha kamida 3 ta harf bo'lishi kerak!")
        if "uchar" in value.lower() and "gilam" not in value.lower():
            raise serializers.ValidationError("Agar 'uchar' so'zi bo'lsa, 'gilam' ham bo'lishi shart!")
        return value

  
    def create(self, validated_data):
         validated_data['title'] = validated_data['title'].capitalize()
         return Book.objects.create(**validated_data)

   
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

   
    def to_representation(self, instance):
        representation = super().to_representation(instance)                
        representation['author_display'] = f"Hurmatli muallif: {instance.author}"
        representation['is_short_story'] = len(instance.description) < 100
        return representation