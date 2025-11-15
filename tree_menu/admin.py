from django.contrib import admin
from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def clean_named_url_kwargs(self):
        data = self.cleaned_data.get('named_url_kwargs')
        if data in [None, ""]:
            return None
        if not isinstance(data, dict):
            raise forms.ValidationError("named_url_kwargs must be a dictionary.")
        return data


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm
    list_display = ('title', 'menu', 'parent', 'order', 'named_url', 'url', 'open_in_new_tab', 'image')
    list_filter = ('menu',)
    search_fields = ('title', 'url', 'named_url')
    ordering = ('menu', 'order', 'title')
    list_editable = ('order',)
    raw_id_fields = ('parent',)