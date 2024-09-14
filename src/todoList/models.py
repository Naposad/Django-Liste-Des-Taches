from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.contrib.auth import get_user_model

Auth = get_user_model()


class ToDo(models.Model):
    mytodo = models.ForeignKey(Auth, on_delete=models.CASCADE, related_name='author')
    name = models.TextField(max_length=400)
    date = models.DateTimeField(default=datetime.now, blank=True)
    date_end = models.DateTimeField(default=datetime.now, blank=True)
    completed = models.BooleanField(default=False)
    slug = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.name} ------------------ {self.completed}'

    def save(self, *args, **kwargs):
        # Déboguer les valeurs des dates
        #print(f"date: {self.date}, date_end: {self.date_end}")

        # Assurer que date_end et date ne sont pas None avant la comparaison
        if self.date_end and self.date and self.date_end < self.date:
            print("Condition remplie: date_end < date")
            self.completed = True

        # Générer un slug unique si non défini
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            num = 1

            # S'assurer que le slug est unique
            while ToDo.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{base_slug}-{num}'
                num += 1

            self.slug = unique_slug

        # Appeler la méthode save de la superclasse
        super().save(*args, **kwargs)
