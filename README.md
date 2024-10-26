# Django Admin Configuration

This Django application configures the admin interface for managing various models related to a daily display system. Below is an overview of the configuration and how to set it up.

## Models

The following models are registered and managed through the Django admin interface:

- `MenuItem`
- `Ingredient`
- `DisplaySection`
- `QuantityType`
- `DisplayItem`
- `DailyDisplay`

## Admin Configuration

### DisplayItemInline

This inline class allows you to manage `DisplayItem` instances directly within the `DailyDisplay` admin interface.

```python
class DisplayItemInline(admin.TabularInline):
    model = DisplayItem
    extra = 1

DailyDisplayAdmin
This admin class customizes the admin interface for the DailyDisplay model.

@admin.register(DailyDisplay)
class DailyDisplayAdmin(admin.ModelAdmin):
    list_display = ['date', 'meal_period']
    list_filter = ['date', 'meal_period']
    inlines = [DisplayItemInline]

Registering Models
The following models are registered with the admin site:
admin.site.register(MenuItem)
admin.site.register(Ingredient)
admin.site.register(DisplaySection)
admin.site.register(QuantityType)
admin.site.register(DisplayItem)
```
## Setup
1. Ensure you have Django installed in your environment.
2. Add the models to your admin.py file as shown above.
3. Run python manage.py makemigrations and python manage.py migrate to apply any database changes.
4. Create a superuser using python manage.py createsuperuser to access the admin interface.
5. Run the development server using python manage.py runserver and navigate to /admin to manage your models.

### Summary

- **Do not hardcode credentials**: Always use secure methods to manage sensitive information.
- **Follow prompts**: When creating a superuser, follow the prompts in the terminal to enter the necessary information securely.
 
**manage.py createsuperuser to access the admin interface.**

Run the development server using python manage.py runserver and navigate to /admin to manage your models.

## Usage

- **You can just navigate to the Django admin interface.**
 
- **Manage DailyDisplay entries, including inline DisplayItem instances.**

- **Use the filters and list display options to navigate and manage your data easily.**
### License
This project is licensed under the MIT License.
This README provides a clear overview of the admin configuration, setup instructions, and usage guidelines.
