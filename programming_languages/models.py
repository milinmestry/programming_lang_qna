from django.db import models

# Create your models here.
class ProgrammingLanguage(models.Model):
    """
        Programming Languages master table.
    """
    programming_lang = models.CharField(max_length=20)
    description = models.TextField(max_length=300, blank=True, null=True)
    icon_url = models.URLField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(blank=True)
    added_by = models.CharField(max_length=100, blank=True)
    added_on = models.DateTimeField(blank=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    deactivated_by = models.CharField(max_length=100, blank=True, null=True)
    deactivated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.programming_lang

    class Meta:
        db_table = 'programming_languages'
