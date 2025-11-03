from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=255)
    active = models.BooleanField(verbose_name=_("active"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")