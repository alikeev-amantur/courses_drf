from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from courses.serializers import CourseSerializer
from .utils import create_category, create_course
from courses.models import Course

COURSES_URL = reverse("courses_list")


class TestCourseViews(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_get_course(self):
        category = create_category()
        course1 = create_course(category=category)
        course2 = create_course(category=category)
        response = self.client.get(COURSES_URL)

        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_course(self):
        category = create_category()
        payload = {
            "name": "English courses",
            "description": "random stuff",
            "logo": "Other random stuff",
            "category_id": 1,
            "branches": [
                {
                    "longitude": "random longitude",
                    "latitude": "random latitude",
                    "address": "random address"
                }
            ],
            "contacts": [
                {
                    "name": 1,
                    "value": 123
                }
            ]
        }

        response = self.client.post(COURSES_URL, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        exists = Course.objects.filter(name=response.data["name"]).exists()
        self.assertTrue(exists)

    def test_course_detail_get(self):
        category = create_category()
        courses = create_course(category=category)
        response = self.client.get(
            courses.get_url()
        )
        serializer = CourseSerializer(courses)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_course_detail_delete(self):
        category = create_category(name="Intended course")
        courses = create_course(category=category)
        response = self.client.delete(
            courses.get_url()
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        exists = Course.objects.filter(name="Intended course")
        self.assertFalse(exists)
