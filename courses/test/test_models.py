from django.test import TestCase
from courses.models import Course, Branch, Contact, Category
from .utils import create_course, create_category, create_branch, create_contact


class CoursesTest(TestCase):

    def test_category_creation(self):
        c = create_category()
        self.assertTrue(isinstance(c, Category))
        self.assertTrue(str(c), c.name)

    def test_courses_creation(self):
        w = create_course(category=create_category())
        self.assertTrue(isinstance(w, Course))
        self.assertEqual(str(w), w.name)

    def test_branch_creation(self):
        b = create_branch(course=create_course(category=create_category()))
        self.assertTrue(isinstance(b, Branch))
        self.assertEqual(str(b), b.address)

    def test_contact_creation(self):
        con = create_contact(course=create_course(category=create_category()))
        self.assertTrue(isinstance(con, Contact))
        self.assertEqual(str(con), con.value)
