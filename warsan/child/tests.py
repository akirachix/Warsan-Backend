from django.test import TestCase
from django.urls import reverse
from child.models import Child, Guardian
from faker import Faker

class ChildModelTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()

    def test_child_model_str_representation(self):
        guardian = Guardian.objects.create(
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            location=self.fake.city(),
            phone_number=self.fake.phone_number()
        )
        child = Child.objects.create(
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            date_of_birth=self.fake.date_of_birth(),
            gender=self.fake.random_element(elements=('M', 'F')),
            guardian=guardian,
        )
        expected_str = f"{child.first_name} {child.last_name} (Child of {guardian.first_name} {guardian.last_name})"
        self.assertEqual(str(child), expected_str)

class GuardianModelTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()

    def test_guardian_model_str_representation(self):
        guardian = Guardian.objects.create(
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            location=self.fake.city(),
            phone_number=self.fake.phone_number()
        )
        expected_str = f"{guardian.first_name} {guardian.last_name}"
        self.assertEqual(str(guardian), expected_str)



# Print the values assigned to the "gender" field
print(Child._meta.get_field('gender').default)
print(Child._meta.get_field('gender').null)
