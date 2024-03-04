import random
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class CookieStand(models.Model):
    
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(blank=True)
    hourly_sales = models.JSONField(default=list, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('cookie_stands_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        # Check if it's a new instance or if any of the dependent values have changed
        if self._state.adding or self.has_changed():
            self.hourly_sales = [
                int(random.randint(self.minimum_customers_per_hour, self.maximum_customers_per_hour) * self.average_cookies_per_sale)
                for _ in range(12)
            ]
        super().save(*args, **kwargs)

    def has_changed(self):
        if not self.pk:
            return True
        # Fetch the original values from the database
        original = CookieStand.objects.get(pk=self.pk)
        # Check if any of the specified fields have changed
        if (original.minimum_customers_per_hour != self.minimum_customers_per_hour or
                original.maximum_customers_per_hour != self.maximum_customers_per_hour or
                original.average_cookies_per_sale != self.average_cookies_per_sale):
            return True
        return False
    