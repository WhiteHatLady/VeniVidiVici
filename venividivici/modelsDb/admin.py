from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# from django_markdown.admin import MarkdownModelAdmin
# from .fields import MarkdownFormField
# from .widgets import MarkdownWidget
# from .utils import editor_js_initialization
# from django.core.urlresolvers import reverse
# Register your models here.

#admin summernote implementation: https://djangocentral.com/integrating-summernote-in-django/

class SummerAdmin(SummernoteModelAdmin):
	# this is for all model's objects
	summernote_fields = '__all__'
	# summernote_fields = 'text'

admin.site.register(Rules, SummerAdmin)
admin.site.register(UserProfile)
admin.site.register(Group)
admin.site.register(Competition, SummerAdmin)
admin.site.register(Points)
# admin.site.register(Rules,  )
admin.site.register(Shop)
# admin.site.register(Hof)



