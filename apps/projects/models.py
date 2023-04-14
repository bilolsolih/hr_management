from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Team(BaseModel):
    members = models.ManyToManyField(verbose_name=_('Members'), to='employees.Employee', related_name='teams')
    is_active = models.BooleanField(verbose_name=_('Is still active?'), default=True)

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    @property
    def team_title(self):
        return f"Team {self.id} working on {self.project.title} project"

    def __str__(self):
        return self.team_title

    # project


class Project(BaseModel):
    team = models.OneToOneField(
        verbose_name=_('Team'),
        to='projects.Team',
        related_name='project',
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(verbose_name=_('Project title'), max_length=255)
    description = models.TextField(verbose_name=_('Project description'))
    client = models.CharField(verbose_name=_('Client'), max_length=255)
    deadline = models.DateField(verbose_name=_('Deadline'), default=timezone.now)
    is_active = models.BooleanField(verbose_name=_('Is still active?'), default=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.title
