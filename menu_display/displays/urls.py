# displays/urls.py (App-level URLs)
from django.urls import path
from .views import DisplayView, DisplayHomeView

app_name = 'displays'

urlpatterns = [
    # Home view showing all sections
    path('', DisplayHomeView.as_view(), name='home'),
    
    # Individual section displays
    path('vegetable/', DisplayView.as_view(), {'section': 'vegetable'}, name='vegetable_display'),
    path('main/', DisplayView.as_view(), {'section': 'main'}, name='main_display'),
    path('bread/', DisplayView.as_view(), {'section': 'bread'}, name='bread_display'),
    
    # Generic section display (alternative to individual paths)
    path('<str:section>/', DisplayView.as_view(), name='section_display'),
]