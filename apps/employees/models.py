from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel


class Position(BaseModel):
    title = models.CharField(verbose_name=_('Position title'), max_length=255, unique=True)
    job_description = models.TextField()

    # employees

    class Meta:
        verbose_name = _('Position')
        verbose_name_plural = _('Positions')

    def __str__(self):
        return self.title


class Employee(BaseModel):
    position = models.ForeignKey(
        verbose_name=_('Position'),
        to='employees.Position',
        related_name='employees',
        on_delete=models.SET_NULL,
        null=True
    )
    first_name = models.CharField(verbose_name=_('First name'), max_length=255)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=255)
    phone_number = PhoneNumberField(verbose_name=_('Phone number'), region='UZ')
    salary = models.DecimalField(verbose_name=_('Salary'), max_digits=24, decimal_places=2, default=0)
    started_on = models.DateField(verbose_name=_('Started on'), default=timezone.now)
    ends_on = models.DateField(verbose_name=_('Ends on'), default=timezone.now)
    is_intern = models.BooleanField(verbose_name=_('Is an intern?'), default=False)

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def position_title(self):
        return self.position.title

    @property
    def attendance_records(self):
        records = self.attendances.all()
        print(records)
        return self.create_attendance_record(records)

    @staticmethod
    def create_attendance_record(records):
        response = dict()
        for record in records:
            response[f"{record.date.year}-{record.date.month}-{record.date.day}"] = 9 * 60 - (record.arrived_at.hour * 60 + record.arrived_at.minute)
            print(response)
        return response

    def __str__(self):
        return self.full_name
