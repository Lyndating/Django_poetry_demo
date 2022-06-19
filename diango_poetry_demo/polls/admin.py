from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# register Question model

# remove register() call for Choice model
# Choice objects are edited on the Question admin page.


# class ChoiceInline(admin.StackedInline): display all fields in lines
class ChoiceInline(admin.TabularInline):  # displaying tabular way
    model = Choice
    extra = 3  # by default provide fields for 3 choices


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
