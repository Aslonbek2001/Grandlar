# choices.py
from django.utils.translation import gettext_lazy as _


class PrivilegeCategory:
    CHOICES = [
        ('undefined', _('Undefined')),
        ('student', _('Student')),
        ('employee', _('Employee')),
        ('admin', _('Admin')),
    ]


class EducationDirection:
    CHOICES = [
        ('undefined', _('Undefined')),
        ('science', _('Science')),
        ('engineering', _('Engineering')),
        ('arts', _('Arts')),
        ('business', _('Business')),
        ('medicine', _('Medicine')),
    ]


class EducationLevel:
    CHOICES = [
        ('undefined', _('Undefined')),
        ('high_school', _('High School')),
        ('bachelors', _('Bachelors')),
        ('masters', _('Masters')),
        ('doctorate', _('Doctorate')),
    ]

