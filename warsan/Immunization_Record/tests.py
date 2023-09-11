from django.test import TestCase
from .models import Immunization_Record
from datetime import datetime, timedelta
from django.utils import timezone

# class ImmunizationRecordModelTest(TestCase):
#     def setUp(self):
#         self.data = {
#              "date_of_administaration": "2023-09-05T06:00:00+00:00",  # Note the "+00:00" for UTC
#             "next_date_of_administration": "2023-09-06T18:00:00+00:00",  # Note the "+00:00" for UTC
# }


#         self.immunization_record = Immunization_Record(
#             date_of_administaration=timezone.make_aware(datetime.fromisoformat(self.data["date_of_administaration"])),
#             next_date_of_administration=timezone.make_aware(datetime.fromisoformat(self.data["next_date_of_administration"]))
#         )
#         self.immunization_record.save()

#     def tearDown(self):
#         # Clean up any data created during the test
#         Immunization_Record.objects.all().delete()

#     def test_immunization_record_creation(self):
#         """
#         Test if Immunization_Record instance was created successfully.
#         """
#         self.assertEqual(self.immunization_record.pk, 1)
#         self.assertEqual(
#             self.immunization_record.date_of_administaration.date(),
#             datetime.fromisoformat(self.data["date_of_administaration"]).date()
#         )
#         self.assertEqual(
#             self.immunization_record.next_date_of_administration.date(),
#             datetime.fromisoformat(self.data["next_date_of_administration"]).date()
#         )

#     def test_immunization_record_str(self):
#         """
#         Test the __str__ method of Immunization_Record model.
#         """
#         expected_str = f"Immunization Record #{self.immunization_record.pk}"
#         self.assertEqual(str(self.immunization_record), expected_str)

#     def test_immunization_record_fields(self):
#         """
#         Test individual fields of Immunization_Record.
#         """
#         immunization_record = Immunization_Record.objects.get(pk=1)
#         self.assertEqual(immunization_record.date_of_administaration, self.immunization_record.date_of_administaration)
#         self.assertEqual(immunization_record.next_date_of_administration, self.immunization_record.next_date_of_administration)

#     def test_immunization_record_update(self):
#         """
#         Test updating the fields of an Immunization_Record instance.
#         """
#         new_date = timezone.now() + timedelta(days=60)
#         self.immunization_record.next_date_of_administration = new_date
#         self.immunization_record.save()
#         updated_record = Immunization_Record.objects.get(pk=1)
#         self.assertEqual(updated_record.next_date_of_administration, new_date)
