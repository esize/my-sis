"""
URL configuration for my_sis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import core.views as core
import academic_structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/people/', view=core.person_list),
    path('api/people/<int:pk>/', view=core.person_detail),
    # path('api/academic_units/', view=core.academic_unit_list),
    # path('api/academic_units/<int:pk>/', view=core.academic_unit_detail),
    # path('api/academic_levels/', view=core.views.academic_level_list),
    # path('api/academic_levels/<int:pk>/', view=core.views.academic_level_detail),
    # path('api/program_of_study_types/', view=core.views.program_of_study_type_list),
    # path('api/program_of_study_types/<int:pk>/', view=core.views.program_of_study_type_detail),
    # path('api/program_of_studies/', view=core.views.program_of_study_list),
    # path('api/program_of_studies/<int:pk>/', view=core.views.program_of_study_detail),
    # path('api/educational_credentials/', view=core.views.educational_credential_list),
    # path('api/educational_credentials/<int:pk>/', view=core.views.educational_credential_detail),
    # path('api/educational_credential_types/', view=core.views.educational_credential_type_list),
    # path('api/educational_credential_types/<int:pk>/', view=core.views.educational_credential_type_detail),
]
