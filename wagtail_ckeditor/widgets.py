import json
from django.templatetags.static import static
from django.forms import widgets
from django.utils.safestring import mark_safe
from wagtail.admin.panels import FieldPanel  # Use FieldPanel for rich text panels
from wagtail.rich_text import expand_db_html


from wagtail_ckeditor import settings as ck_settings


# A simple cleaning function; update as needed.
def clean_editor_html(value):
    return value


class CKEditor(widgets.Textarea):
    """
    A CKEditor widget for Wagtail using CKEditor 5.
    Uses Django Media to pull in assets, and tags each textarea
    with .ckeditor5 so our JS can initialize them all in one place.
    """

    class Media:
        css = {
            "all": (
                static(
                    ck_settings.CKEDITOR_CSS
                ),  # e.g. 'ckeditor5/ckeditor5/ckeditor5.css'
            )
        }
        # js = (
        #     static(ck_settings.CKEDITOR_JS),  # e.g. 'ckeditor5/ckeditor5/ckeditor5.js'
        #     static("wagtail-ckeditor.js"),
        # )

    def get_panel(self):
        return FieldPanel

    def render(self, name, value, attrs=None, renderer=None):
        # Ensure attrs exists and has our class
        attrs = attrs or {}
        existing = attrs.get("class", "")
        attrs["class"] = (existing + " ckeditor5").strip()

        # Expand any stored DB HTML
        translated_value = expand_db_html(value) if value is not None else None

        # Render the <textarea> with our updated attrs
        return super().render(name, translated_value, attrs=attrs, renderer=renderer)

    def value_from_datadict(self, data, files, name):
        val = super().value_from_datadict(data, files, name)
        return clean_editor_html(val) if val is not None else None
