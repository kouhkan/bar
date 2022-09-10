from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.applicant.v1.applicant_logics import create_applicant
from apps.applicant.models import Applicant


class ApplicantLogicTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(email="test@gmail.com", level="ADMIN")

    def tearDown(self) -> None:
        self.user.delete()

    def test_create_applicant(self) -> None:
        applicant = create_applicant(self.user, "applicant 1", "content 1", "test place")
        self.assertIsInstance(applicant, Applicant)
