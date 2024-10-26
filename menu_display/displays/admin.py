# displays/admin.py
from django.contrib import admin
from .models import (
    MenuItem, Ingredient, DisplaySection, 
    QuantityType, DailyDisplay, DisplayItem
)


''' 
Explanation
Imports:

Import necessary modules and classes from Django's admin module and the models defined in the models.py file.
DisplayItemInline:

Defines an inline admin class for the DisplayItem model.
model = DisplayItem: Specifies that this inline is for the DisplayItem model.
extra = 1: Specifies that one extra empty form should be displayed in the inline.
DailyDisplayAdmin:

Defines an admin class for the DailyDisplay model.
@admin.register(DailyDisplay): Registers the DailyDisplay model with this admin class.
list_display = ['date', 'meal_period']: Specifies the columns to display in the admin list view for DailyDisplay.
list_filter = ['date', 'meal_period']: Specifies the filters to display in the admin list view for DailyDisplay.
inlines = [DisplayItemInline]: Specifies that DisplayItemInline should be displayed within the DailyDisplay admin.
Registering Models:

admin.site.register(MenuItem): Registers the MenuItem model with the admin site.
admin.site.register(Ingredient): Registers the Ingredient model with the admin site.
admin.site.register(DisplaySection): Registers the DisplaySection model with the admin site.
admin.site.register(QuantityType): Registers the QuantityType model with the admin site.
admin.site.register(DisplayItem): Registers the DisplayItem model with the admin site.
Summary
This code configures the Django admin interface for the models defined in the models.py file. It includes:

An inline admin class for DisplayItem to be used within the DailyDisplay admin.
An admin class for DailyDisplay that includes list display columns, list filters, and the DisplayItemInline.
Registration of the MenuItem, Ingredient, DisplaySection, QuantityType, and DisplayItem models with the admin site.
This setup allows for a more user-friendly and efficient management of the models through the Django admin interface.
'''


# Inline admin class for DisplayItem
class DisplayItemInline(admin.TabularInline):
    model = DisplayItem  # Specifies the model to be used in the inline
    extra = 1  # Specifies the number of extra forms to display in the inline

# Admin class for DailyDisplay
@admin.register(DailyDisplay)
class DailyDisplayAdmin(admin.ModelAdmin):
    list_display = ['date', 'meal_period']  # Columns to display in the admin list view
    list_filter = ['date', 'meal_period']  # Filters to display in the admin list view
    inlines = [DisplayItemInline]  # Inline model to display within the DailyDisplay admin

# Register the remaining models with the admin site
admin.site.register(MenuItem)
admin.site.register(Ingredient)
admin.site.register(DisplaySection)
admin.site.register(QuantityType)
admin.site.register(DisplayItem)
