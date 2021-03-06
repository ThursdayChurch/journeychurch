from django.db import models
from django.db.models import Q
from django.utils import timezone

class PublicEntryManager(models.Manager):
    """
    Manager class that overrides the objects field on class Entry.
    This returns the public entries instead of all entries.
    """

    def get_queryset(self):
        return super(PublicEntryManager, self).get_queryset().filter(
            # public entries: entry date <= now, expiration date > now, status is open
            Q(expiration_date__gt=timezone.now()) | Q(expiration_date__isnull=True),
            entry_date__lte=timezone.now(),
            status='open',
        )

class Entry(models.Model):
    """
    Abstract class used to define fields for all entries
    """

    # default uses PublicEntryManager to retrieve only public entries
    objects = PublicEntryManager()

    # All objects
    all_objects = models.Manager()

    # ID - automatically generated

    # Title of entry
    title = models.CharField(max_length=100, unique=True, null=True)

    # Slug for entry
    slug = models.SlugField(max_length=200, unique=True, null=True)

    # Date created
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    # Date updated
    updated_date = models.DateTimeField(auto_now=True, null=True)

    # Entry Date (used for scheduling)
    entry_date = models.DateTimeField(null=True)

    # Entry Date (used for scheduling)
    expiration_date = models.DateTimeField(blank=True, null=True)

    # Status of entry - open or closed
    STATUSES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
    )

    status = models.CharField(max_length=6, choices=STATUSES, default='open')

    # Representation in admin
    def __str__(self):
        return self.title

    # Check if the entry is published based on the entry date and expiration date
    def is_published(self, date):

        # Both are empty
        if self.entry_date is None and self.expiration_date is None:
            return True

        # Entry Date is empty
        elif self.entry_date is None:
            return date <= self.expiration_date

        # Expiration Date is empty
        elif self.expiration_date is None:
            return date >= self.entry_date

        # Both are specified
        else:
            return date >= self.entry_date and date <= self.expiration_date

    # Check if entry is visible to users
    def is_public(self, date):
        if self.status is 'open' and self.is_published(date=date):
            return True
        return False


    class Meta:

        # Specifies that class is abstract and to add these fields to each model that extends it
        abstract = True
