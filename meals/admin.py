
# Register your models here.
from django.contrib import admin
from meals.models import Meal, Dish, MealDish

class MealDishInline(admin.TabularInline):
    model = MealDish
    extra = 1

class MealAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['meal_name']}),
        (None,               {'fields': ['owner']}),
        (None,               {'fields': ['meal_desc']}),
        (None,               {'fields': ['meal_type']}),
        (None,               {'fields': ['photo']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = (MealDishInline,)
    list_filter = ['pub_date']
    search_fields = ['meal_name']

admin.site.register(Meal, MealAdmin)

admin.site.register(Dish)