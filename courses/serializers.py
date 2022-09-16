from rest_framework import serializers
from courses.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'imgpath')


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'value')


class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True,
                                                     queryset=Category.objects.all(), source='category')

    class Meta:
        model = Course
        fields = (
            'name', 'description', 'logo', 'category', 'contacts', 'category_id', 'branches')

    def create(self, validated_data):
        contacts = validated_data.pop('contacts')
        branches = validated_data.pop('branches')
        course = Course.objects.create(**validated_data)
        for contact in contacts:
            Contact.objects.create(course=course, **contact)
        for branch in branches:
            Branch.objects.create(course=course, **branch)
        return course
