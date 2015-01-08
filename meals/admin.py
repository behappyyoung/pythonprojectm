
# Register your models here.
from django.contrib import admin
from meals.models import Meal, Dish

##class DishInline(admin.TabularInline):
##    model = Dish
##    extra = 3

class MealAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['meal_title']}),
        (None,               {'fields': ['owner']}),
        (None,               {'fields': ['dish']}),
        (None,               {'fields': ['meal_desc']}),
        (None,               {'fields': ['meal_type']}),
        (None,               {'fields': ['photo']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    list_filter = ['pub_date']
    search_fields = ['meal_title']

admin.site.register(Meal, MealAdmin)

admin.site.register(Dish)