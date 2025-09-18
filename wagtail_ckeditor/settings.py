from django.conf import settings
import json

from django.conf import settings

CKEDITOR_JS = getattr(
    settings, "WAGTAIL_CKEDITOR_JS", "ckeditor5/ckeditor5/ckeditor5.js"
)
CKEDITOR_CSS = getattr(
    settings, "WAGTAIL_CKEDITOR_CSS", "ckeditor5/ckeditor5/ckeditor5.css"
)

CKEDITOR_PLUGIN_IMPORTS = getattr(
    settings,
    "WAGTAIL_CKEDITOR_PLUGIN_IMPORTS",
    [
        "ClassicEditor",
        "Alignment",
        "Autoformat",
        "BlockQuote",
        "Bold",
        "CloudServices",
        "Code",
        "CodeBlock",
        "Essentials",
        "Font",
        "Heading",
        "Highlight",
        "Image",
        "ImageCaption",
        "ImageStyle",
        "ImageToolbar",
        "ImageUpload",
        "Indent",
        "Italic",
        "Link",
        "List",
        "MediaEmbed",
        "Paragraph",
        "PasteFromOffice",
        "Table",
        "TableToolbar",
        "TextTransformation",
        "Underline",
    ],
)

CKEDITOR_PLUGIN_REFERENCES = getattr(
    settings,
    "WAGTAIL_CKEDITOR_PLUGIN_REFERENCES",
    [
        "Alignment",
        "Autoformat",
        "BlockQuote",
        "Bold",
        "Code",
        "CodeBlock",
        "Essentials",
        "Font",
        "Heading",
        "Highlight",
        "Image",
        "ImageCaption",
        "ImageStyle",
        "ImageToolbar",
        "ImageUpload",
        "Indent",
        "Italic",
        "Link",
        "List",
        "MediaEmbed",
        "Paragraph",
        "PasteFromOffice",
        "Table",
        "TableToolbar",
        "TextTransformation",
        "Underline",
    ],
)

CKEDITOR_CONFIG = getattr(
    settings,
    "WAGTAIL_CKEDITOR_CONFIG",
    {
        "licenseKey": "GPL",
        "toolbar": [
            "undo",
            "redo",
            "|",
            "heading",
            "|",
            "bold",
            "italic",
            "underline",
            "highlight",
            "|",
            "fontSize",
            "fontFamily",
            "fontColor",
            "fontBackgroundColor",
            "|",
            "alignment",
            "outdent",
            "indent",
            "|",
            "numberedList",
            "bulletedList",
            "|",
            "link",
            "blockQuote",
            "insertTable",
            "mediaEmbed",
            "code",
            "codeBlock",
            "|",
            "imageUpload",
        ],
        "fontSize": {
            "options": [8, 10, 12, 14, 16, 18, 20, 22, 24, 30, 36, 48, 72, "default"],
            "supportAllValues": True,
        },
        "fontFamily": {
            "options": [
                "default",
                "Arial, Helvetica, sans-serif",
                "Courier New, Courier, monospace",
                "Georgia, serif",
                "Lucida Sans Unicode, Lucida Grande, sans-serif",
                "Tahoma, Geneva, sans-serif",
                "Times New Roman, Times, serif",
                "Trebuchet MS, Helvetica, sans-serif",
                "Verdana, Geneva, sans-serif",
            ],
            "supportAllValues": True,
        },
    },
)


JSON_CONFIG = json.dumps(CKEDITOR_CONFIG)
