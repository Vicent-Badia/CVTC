from django.contrib import admin
from .models import Question
from .models import Choice

#add Choices to Questions form
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
#This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #filter by date:
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)