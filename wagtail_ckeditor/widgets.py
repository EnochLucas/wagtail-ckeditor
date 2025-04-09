import json
from django.templatetags.static import static
from django.forms import widgets
from django.utils.safestring import mark_safe
from wagtail.admin.panels import FieldPanel  # Use FieldPanel for rich text panels
from wagtail.rich_text import expand_db_html

# A simple cleaning function; update as needed.
def clean_editor_html(value):
    return value

from wagtail_ckeditor import settings as ck_settings


class CKEditor(widgets.Textarea):
    """
    A CKEditor widget for Wagtail using CKEditor 5.
    This version does not extend WidgetWithScript,
    so it manually appends a <script type="module"> tag.
    """
    
    def get_panel(self):
        # In your page model, you would wrap this field in a FieldPanel.
        return FieldPanel

    def render(self, name, value, attrs=None, renderer=None):
        # Render the textarea as usual.
        if value is None:
            translated_value = None
        else:
            translated_value = expand_db_html(value)
        html = super().render(name, translated_value, attrs, renderer=renderer)
        # Append the JS initialization code after the textarea.
        editor_id = attrs.get("id", "")
        js_init = self.render_js_init(editor_id, name, value)
        return mark_safe(html + js_init)

    def render_js_init(self, editor_id, name, value):
        """Generates the script tag to initialize CKEditor."""
        json_config = ck_settings.JSON_CONFIG
        import_list = ck_settings.CKEDITOR_PLUGIN_IMPORTS
        plugin_references = ck_settings.CKEDITOR_PLUGIN_REFERENCES
        static_url = static(ck_settings.CKEDITOR_JS)


        return f"""
        <script type="module">
            import {{ {', '.join(import_list)} }} from '{static_url}';
            
            const editorConfig = {{
                ...{json_config},
                plugins: [ {', '.join(plugin_references)} ]
            }};

            ClassicEditor
                .create(document.querySelector('#{editor_id}'), editorConfig)
                .catch(error => {{
                    console.error("CKEditor init failed:", error);
                }});
        </script>
        """

    def value_from_datadict(self, data, files, name):
        original_value = super().value_from_datadict(data, files, name)
        if original_value is None:
            return None
        return clean_editor_html(original_value)




