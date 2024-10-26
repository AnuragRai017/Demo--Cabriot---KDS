from django.views.generic import TemplateView
from django.utils import timezone
from datetime import datetime
from django.conf import settings
from .models import DailyDisplay, DisplayItem, DisplaySection

'''
Explanation
Imports:

Import necessary modules and classes from Django and other libraries.
DisplayHomeView:

Inherits from TemplateView.
Uses get_context_data to add custom data to the context.
Fetches all sections and the current meal period.
Tries to get the DailyDisplay for the current date and meal period.
If found, fetches DisplayItem objects for each section and updates the context.
If not found, adds an error message to the context.
get_current_meal_period determines the current meal period based on the time of day.
DisplayView:

Similar to DisplayHomeView, but focuses on a specific section.
Uses get_context_data to add custom data to the context.
Fetches the current meal period and date.
Tries to get the DailyDisplay and DisplaySection for the current date, meal period, and section name.
If found, fetches DisplayItem objects for the section and updates the context.
If not found, adds an error message to the context.
get_current_meal_period is the same as in DisplayHomeView.
This code is designed to dynamically fetch and display information based on the current date, time, and section, providing a flexible way to manage and display meal period information.
'''

# DisplayHomeView is a class-based view that inherits from Django's TemplateView
class DisplayHomeView(TemplateView):
    template_name = 'displays/display_home.html'  # Template to render

    # Override the get_context_data method to add custom context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get the default context data
        
        # Get all available sections from the database
        sections = DisplaySection.objects.all()
        
        # Get the current meal period and date
        meal_period = self.get_current_meal_period()
        current_date = timezone.localtime().date()
        
        try:
            # Try to get the DailyDisplay object for the current date and meal period
            daily_display = DailyDisplay.objects.get(
                date=current_date,
                meal_period=meal_period
            )
            
            # Create a dictionary to hold items for each section
            section_items = {}
            for section in sections:
                # Get display items for each section
                items = DisplayItem.objects.filter(
                    daily_display=daily_display,
                    section=section
                )
                section_items[section] = items
            
            # Update the context with sections, items, meal period, and current date
            context.update({
                'sections': sections,
                'section_items': section_items,
                'meal_period': daily_display.get_meal_period_display(),
                'current_date': current_date,
            })
            
        except DailyDisplay.DoesNotExist:
            # If no DailyDisplay is found, add an error message to the context
            context['error'] = 'No display configured for the current time'
        
        return context

    # Method to determine the current meal period based on the time of day
    def get_current_meal_period(self):
        now = timezone.localtime().time()  # Get the current local time
        breakfast_start = datetime.strptime(settings.DISPLAY_SETTINGS['BREAKFAST_START'], '%H:%M').time()
        lunch_end = datetime.strptime(settings.DISPLAY_SETTINGS['LUNCH_END'], '%H:%M').time()
        dinner_end = datetime.strptime(settings.DISPLAY_SETTINGS['DINNER_END'], '%H:%M').time()
        
        # Determine the meal period based on the current time
        if breakfast_start <= now <= lunch_end:
            return 'BL'  # Breakfast/Lunch
        elif lunch_end < now <= dinner_end:
            return 'D'  # Dinner
        return 'BL'  # Default to Breakfast/Lunch

# DisplayView is another class-based view that inherits from Django's TemplateView
class DisplayView(TemplateView):
    template_name = 'displays/section_display.html'  # Template to render

    # Method to determine the current meal period (same as in DisplayHomeView)
    def get_current_meal_period(self):
        now = timezone.localtime().time()  # Get the current local time
        breakfast_start = datetime.strptime(settings.DISPLAY_SETTINGS['BREAKFAST_START'], '%H:%M').time()
        lunch_end = datetime.strptime(settings.DISPLAY_SETTINGS['LUNCH_END'], '%H:%M').time()
        dinner_end = datetime.strptime(settings.DISPLAY_SETTINGS['DINNER_END'], '%H:%M').time()
        
        # Determine the meal period based on the current time
        if breakfast_start <= now <= lunch_end:
            return 'BL'  # Breakfast/Lunch
        elif lunch_end < now <= dinner_end:
            return 'D'  # Dinner
        return 'BL'  # Default to Breakfast/Lunch
    
    # Override the get_context_data method to add custom context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get the default context data
        section_name = kwargs.get('section')  # Get the section name from the URL parameters
        
        # Get the current date and meal period
        current_date = timezone.localtime().date()
        meal_period = self.get_current_meal_period()
        
        try:
            # Try to get the DailyDisplay object for the current date and meal period
            daily_display = DailyDisplay.objects.get(
                date=current_date,
                meal_period=meal_period
            )
            
            # Get the DisplaySection object for the specified section name
            section = DisplaySection.objects.get(name=section_name)
            # Get display items for the specified section
            display_items = DisplayItem.objects.filter(
                daily_display=daily_display,
                section=section
            )
            
            # Update the context with display items, section, and meal period
            context['display_items'] = display_items
            context['section'] = section
            context['meal_period'] = daily_display.get_meal_period_display()
            
        except (DailyDisplay.DoesNotExist, DisplaySection.DoesNotExist):
            # If no DailyDisplay or DisplaySection is found, add an error message to the context
            context['error'] = 'No display configured for this section and time'
        
        return context