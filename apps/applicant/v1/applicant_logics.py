from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from apps.applicant.models import Applicant

User = get_user_model()


@atomic
def create_applicant(user_id: User, title: str, description: str, location: str) -> Applicant:
    applicant = Applicant()
    applicant.user_id = user_id
    applicant.title = title
    applicant.description = description
    applicant.location = location
    applicant.save()
    return applicant
