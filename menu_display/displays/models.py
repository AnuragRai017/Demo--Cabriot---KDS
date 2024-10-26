# displays/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

'''
Explanation
Imports:

Import necessary modules and classes from Django and other libraries.
MenuItem Model:

Represents a menu item with fields for title, name, and image.
__str__ method returns a string representation of the menu item.
Ingredient Model:

Represents an ingredient with fields for title, name, and image.
__str__ method returns a string representation of the ingredient.
DisplaySection Model:

Represents a display section with a name (choice field) and an optional description.
__str__ method returns the display name of the section.
QuantityType Model:

Represents a quantity type with a unit (choice field).
__str__ method returns the display name of the unit.
DailyDisplay Model:

Represents a daily display with a date and meal period (choice field).
__str__ method returns a string representation of the daily display.
clean method ensures no duplicate meal periods for the same date.
DisplayItem Model:

Represents a display item with foreign keys to DailyDisplay, DisplaySection, MenuItem, Ingredient, and QuantityType.
clean method ensures either a menu item or ingredient is specified, but not both.
__str__ method returns a string representation of the display item.
This code defines the models for a menu display system, including menu items, ingredients, display sections, quantity types, daily displays, and display items. The models include validation logic to ensure data integrity and provide string representations for easy identification.
'''

# Model representing a menu item
class MenuItem(models.Model):
    title = models.CharField(max_length=100)  # Title of the menu item
    name = models.CharField(max_length=100)  # Name of the menu item
    image = models.ImageField(upload_to='menu_items/')  # Image of the menu item
    
    def __str__(self):
        return f"{self.title} - {self.name}"  # String representation of the menu item

# Model representing an ingredient
class Ingredient(models.Model):
    title = models.CharField(max_length=100)  # Title of the ingredient
    name = models.CharField(max_length=100)  # Name of the ingredient
    image = models.ImageField(upload_to='ingredients/')  # Image of the ingredient
    
    def __str__(self):
        return f"{self.title} - {self.name}"  # String representation of the ingredient

# Model representing a display section
class DisplaySection(models.Model):
    SECTION_TYPES = (
        ('vegetable', 'Vegetable Section'),
        ('main', 'Main Section'),
        ('bread', 'Bread Section'),
    )
    
    name = models.CharField(max_length=50, choices=SECTION_TYPES)  # Name of the section with choices
    description = models.TextField(blank=True)  # Description of the section (optional)
    
    def __str__(self):
        return self.get_name_display()  # String representation of the section

# Model representing a quantity type
class QuantityType(models.Model):
    UNIT_CHOICES = (
        ('g', 'Grams'),
        ('kg', 'Kilograms'),
        ('num', 'Numbers'),
    )
    
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES)  # Unit of measurement with choices
    
    def __str__(self):
        return self.get_unit_display()  # String representation of the unit

# Model representing a daily display
class DailyDisplay(models.Model):
    MEAL_PERIODS = (
        ('BL', 'Breakfast/Lunch'),
        ('D', 'Dinner'),
    )
    
    date = models.DateField()  # Date of the display
    meal_period = models.CharField(max_length=2, choices=MEAL_PERIODS)  # Meal period with choices
    
    def __str__(self):
        return f"{self.date} - {self.get_meal_period_display()}"  # String representation of the daily display
    
    def clean(self):
        # Ensure no duplicate meal periods for the same date
        if DailyDisplay.objects.filter(date=self.date, meal_period=self.meal_period).exists():
            raise ValidationError('A display for this date and meal period already exists.')

# Model representing a display item
class DisplayItem(models.Model):
    daily_display = models.ForeignKey(DailyDisplay, on_delete=models.CASCADE)  # Foreign key to DailyDisplay
    section = models.ForeignKey(DisplaySection, on_delete=models.CASCADE)  # Foreign key to DisplaySection
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True, blank=True)  # Foreign key to MenuItem (optional)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True, blank=True)  # Foreign key to Ingredient (optional)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # Quantity of the item
    quantity_type = models.ForeignKey(QuantityType, on_delete=models.CASCADE)  # Foreign key to QuantityType
    
    def clean(self):
        # Ensure either a menu item or ingredient is specified, but not both
        if not (self.menu_item or self.ingredient):
            raise ValidationError('Either a menu item or ingredient must be specified.')
        if self.menu_item and self.ingredient:
            raise ValidationError('Cannot specify both menu item and ingredient.')

    def __str__(self):
        item = self.menu_item or self.ingredient  # Get the item (menu item or ingredient)
        return f"{self.daily_display} - {self.section} - {item}"  # String representation of the display item
