from django.db import models

from django.utils import timezone
from django.urls import reverse
# Create your models here.

# set week days
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

# return backward
class ToDoList(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse("list",args=[self.id])

    def __str__(self):
        return self.title

# return insert page
class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(default=one_week_hence)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]