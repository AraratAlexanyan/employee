from django.db import models


class Job(models.Model):
    DEADLINE_CHOICES = (
        ('7 days', 7),
        ('14 days', 14),
        ('30 days', 30)
    )

    SEEKER_LEVEL = (
        ('Internship', 'Internship'),
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior')
    )

    JOB_TYPE = (
        ('full', 'Full Time'),
        ('remote', 'Remote'),
        ('contract', 'Contract'),
        ('part', 'Part time')
    )

    job_title = models.CharField(max_length=64, verbose_name="Job")
    job_description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    dead_line = models.DateTimeField(choices=DEADLINE_CHOICES, max_length=64)
    seeker_level = models.CharField(choices=SEEKER_LEVEL, default='Undefined', max_length=64)
    category = models.CharField(max_length=64, blank=True, null=True, default='Undefined')
    term = models.CharField(choices=JOB_TYPE, default='Permanent', max_length=64)

    def __str__(self):
        return self.job_title
