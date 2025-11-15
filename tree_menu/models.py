from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


class MenuItem(models.Model):
    menu = models.CharField(max_length=100, db_index=True,
        help_text="Which menu this item belongs to. Items in the same menu form a tree.")

    title = models.CharField(max_length=200,
                             help_text="The text that will appear for this menu item.")

    parent = models.ForeignKey('self', null=True, blank=True,
                               related_name='children',on_delete=models.CASCADE,
                               help_text="Optional parent menu item. Leave blank if this is a top-level item.")

    url = models.CharField(max_length=500, blank=True,
                           help_text="Direct URL for this menu item (like /about/). Leave blank if using a named URL.")

    named_url = models.CharField(max_length=200, blank=True,
                                 help_text="Django named URL (like 'home'). Used if no direct URL is provided.")

    named_url_kwargs = models.JSONField(null=True, blank=True,
                                        help_text="Optional parameters for the named URL, e.g., {\"id\": 5}.")

    order = models.PositiveIntegerField(default=0, help_text="Sort order. Items with lower numbers appear first.")

    open_in_new_tab = models.BooleanField(default=False, help_text="If checked, this menu item will open in a new browser tab.")

    image = models.URLField(blank=True, help_text="Optional image for this menu item. Will use a default placeholder if empty.")

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return f"{self.title} ({self.menu})"

    def clean(self):
        parent = self.parent
        while parent:
            if parent == self:
                raise ValidationError("Circular parent reference is not allowed.")
            parent = parent.parent

    def get_resolved_url(self):
        if self.url:
            return self.url
        if self.named_url:
            try:
                return reverse(self.named_url, kwargs=self.named_url_kwargs or {})
            except:
                return "/"
        return "/"