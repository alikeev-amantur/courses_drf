from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Course, Branch, Contact
from .serializers import CourseSerializer, BranchSerializer, ContactSerializer, CategorySerializer


class CourseAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailAPIView(APIView):
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response({"message": "item has been deleted"})
