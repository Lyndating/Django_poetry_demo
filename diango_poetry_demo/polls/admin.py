from django.contrib import admin

# Register your models here.
from .models import Question, Choice
# register Question model
admin.site.register(Question)
# register Choice model
admin.site.register(Choice)
