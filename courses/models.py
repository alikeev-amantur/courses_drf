from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    imgpath = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    logo = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE)

    def __str__(self):
        return self.address


class Contact(models.Model):
    PHONE = 1
    FACEBOOK = 2
    EMAIL = 3
    CHOICES = [
        (1, 'Phone'),
        (2, 'Facebook'),
        (3, 'Email'),
    ]

    name = models.IntegerField(choices=CHOICES)
    value = models.CharField(max_length=50)
    course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE)

    def __str__(self):
        return self.value
