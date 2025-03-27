import json

from django.forms import widgets
from django.utils.safestring import mark_safe
from wagtail.utils.widgets import WidgetWithScript
from wagtail.admin.panels import FieldPanel  # Use FieldPanel as the default panel for rich text fields
from wagtail.rich_text import expand_db_html

# A simple cleaning function; you can extend this if needed.
def clean_editor_html(value):
    return value

from wagtail_ckeditor import settings


class CKEditor(WidgetWithScript, widgets.Textarea):

    def get_panel(self):
        # Return FieldPanel so that this widget can be used in a panel.
        return FieldPanel

    def render(self, name, value, attrs=None, renderer=None):
        # Remove the for_editor argument
        if value is None:
            translated_value = None
        else:
            translated_value = expand_db_html(value)
        return super().render(name, translated_value, attrs, renderer=renderer)

    def render_js_init(self, editor_id, name, value):
        return "CKEDITOR.replace( '%s', %s);" % (
            editor_id,
            mark_safe(json.dumps(settings.WAGTAIL_CKEDITOR_CONFIG))
        )

    def value_from_datadict(self, data, files, name):
        original_value = super().value_from_datadict(data, files, name)
        if original_value is None:
            return None
        return clean_editor_html(original_value)
