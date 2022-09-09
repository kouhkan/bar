from django.db.models import Manager
from django.db.models import Q

from .querysets import SoftDeleteQueryset


class SoftDeleteManager(Manager):
    def get_queryset(self):
        return SoftDeleteQueryset(
            self.model, self._db
        ).filter(Q(is_deleted=False) |
                 Q(is_deleted__isnull=True))
