from courses.models import Course, Branch, Contact, Category


def create_category(name="Checking", imgpath="also checking"):
    return Category.objects.create(name=name, imgpath=imgpath)


def create_course(name="only a test", description="yes, this is only a test", logo="Check", category=None):
    return Course.objects.create(name=name, description=description, logo=logo, category=category)


def create_branch(latitude="yeah, another one", longitude="and another one", address="another one", course=None):
    return Branch.objects.create(latitude=latitude, longitude=longitude, address=address, course=course)


def create_contact(name=1, value="Any value", course=None):
    return Contact.objects.create(name=name, value=value, course=course)
