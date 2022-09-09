from django.db.models import QuerySet
from django.utils import timezone


class SoftDeleteQueryset(QuerySet):
    def delete(self):
        return self.update(is_deleted=True, deleted_at=timezone.now())

