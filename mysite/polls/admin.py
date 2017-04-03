from django.contrib import admin

# Register your models here.
from .models import Choice, Question

#class ChoiceInLine(admin.StackedInline):
class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question_text']
	fieldsets = [
		(None, 					{'fields': ['question_text']}),
		('Date information', 	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInLine]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']#filter sidebar that allows user to filter list by the pub_date field.
	search_fields = ['question_text'] #search box to search for words in specified field (question_text)

#admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)