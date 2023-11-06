"""
URL configuration for bootstrap_form project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.template.response import TemplateResponse
from django.urls import path
from django import forms
from django.forms.renderers import TemplatesSetting


class CustomFormRenderer(TemplatesSetting):
    field_template_name = "forms/field.html"


days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday"
}


class BootstrapForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    appointment_date = forms.ChoiceField(
        choices=days,
        widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
        template_name="forms/radio_field.html",
        help_text="Select which day you would like your appointment. We're only open Monday-Wednesday."
    )
    attachment = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
        help_text="Please provide any files you wish us to review prior to your appointment.",
    )


def index(request):
    form = BootstrapForm()
    context = {"form": form}
    return TemplateResponse(request, "index.html", context)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index)
]
