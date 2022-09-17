from django.test import TestCase
from .utils import create_category
from courses import serializers, models


class TestCourseSerializer(TestCase):
    def test_custom_create(self):
        category = create_category()
        course_dictionary = {
            "name": "Random course name",
            "description": "Random text",
            "logo": "random logo",
            "category_id": 1,
            "branches": [
                {
                    "longitude": "random",
                    "latitude": "random",
                    "address": "random address"
                }
            ],
            "contacts": [
                {
                    "name": 1,
                    "value": "random"
                }
            ]
        }
        serializer = serializers.CourseSerializer(data=course_dictionary)
        self.assertTrue(serializer.is_valid())
        serializer.save()

        exists = models.Course.objects.get(id=1)
        self.assertIsNotNone(exists)