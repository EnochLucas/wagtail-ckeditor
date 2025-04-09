from django.templatetags.static import static
from django.utils.html import format_html
from wagtail import hooks
from wagtail.admin.rich_text.converters.editor_html import WhitelistRule
from wagtail.whitelist import allow_without_attributes, attribute_rule
from wagtail_ckeditor import settings as ckeditor_settings

@hooks.register('insert_editor_js')
def ckeditorjs():
    return format_html(
        '<link rel="stylesheet" href="{css_src}">'
        '<link rel="stylesheet" href="{custom_css}">'
        '<script type="module" src="{js_src}"></script>',
        css_src = static(ckeditor_settings.CKEDITOR_CSS),
        custom_css = static('wagtail_ckeditor/custom.css'),
        js_src = static(ckeditor_settings.CKEDITOR_JS),
    )

@hooks.register('register_rich_text_features')
def ckeditor_feature(features):
    """
    Register a rich text feature for CKEditor that whitelists the
    desired elements and attributes.
    """
    # Register a feature named 'ckeditor'
    features.register_converter_rule('editorhtml', 'ckeditor', [
        WhitelistRule('s', allow_without_attributes),
        WhitelistRule('u', allow_without_attributes),
        WhitelistRule('span', attribute_rule({'style': True, 'class': True})),
        WhitelistRule('p', attribute_rule({'style': True, 'class': True})),
        WhitelistRule('div', attribute_rule({'style': True, 'class': True})),
        WhitelistRule('q', allow_without_attributes),
        WhitelistRule('ins', allow_without_attributes),
        WhitelistRule('pre', allow_without_attributes),
        WhitelistRule('address', allow_without_attributes),
        WhitelistRule('table', attribute_rule({'align': True, 'border': True, 'cellpadding': True, 'style': True})),
        WhitelistRule('caption', allow_without_attributes),
        WhitelistRule('thead', allow_without_attributes),
        WhitelistRule('tr', allow_without_attributes),
        WhitelistRule('tbody', allow_without_attributes),
        WhitelistRule('td', attribute_rule({'style': True, 'class': True})),
        WhitelistRule('hr', allow_without_attributes),
        WhitelistRule('img', attribute_rule({'alt': True, 'src': True, 'style': True, 'width': True, 'height': True})),
    ])

    # Add the feature to the default set
    features.default_features.append('ckeditor')