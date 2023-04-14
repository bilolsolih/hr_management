from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Event(BaseModel):
    title = models.CharField(verbose_name=_('Event title'), max_length=255)
    description = models.TextField(verbose_name=_('Event description/scenario'))
    starts_at = models.DateTimeField(verbose_name=_('Starts at'), default=timezone.now)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    @property
    def is_active(self):
        if self.starts_at >= timezone.now():
            return True
        else:
            return False

    def __str__(self):
        return f"Event {self.title}"


class Attendance(BaseModel):
    employee = models.ForeignKey(
        verbose_name=_('Employee'),
        to='employees.Employee',
        related_name='attendances',
        unique_for_date='date',
        on_delete=models.SET_NULL,
        null=True
    )
    first_name = models.CharField(verbose_name=_('First name'), max_length=255, blank=True)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=255, blank=True)
    position = models.CharField(verbose_name=_('Position'), max_length=255, blank=True)
    date = models.DateField(verbose_name=_('Date'), default=timezone.now)
    arrived_at = models.TimeField(verbose_name=_('Arrived at'), default=timezone.now)

    class Meta:
        verbose_name = _('Attendance record')
        verbose_name_plural = _('Attendance records')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.first_name = self.employee.first_name
        self.last_name = self.employee.last_name
        self.position = self.employee.position.title
        super(Attendance, self).save()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Attendance record for {self.full_name}"


class Inventory(BaseModel):
    title = models.CharField(verbose_name=_('Inventory title'), max_length=255)

    # items

    class Meta:
        verbose_name = _('Inventory')
        verbose_name_plural = _('Inventories')

    def __str__(self):
        return f"Inventory {self.title}"


class Item(BaseModel):
    inventory = models.ForeignKey(
        verbose_name=_('Inventory'),
        to='management.Inventory',
        related_name='items',
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(verbose_name=_('Item name'), max_length=255)
    amount = models.DecimalField(verbose_name=_('Amount'), max_digits=24, decimal_places=2, default=0)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    price_per_unit = models.DecimalField(verbose_name=_('Price per unit'), max_digits=24, decimal_places=2, default=0)

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')

    @property
    def total_price(self):
        return self.amount * self.price_per_unit

    def __str__(self):
        return f"Item {self.title} - {self.amount}"
