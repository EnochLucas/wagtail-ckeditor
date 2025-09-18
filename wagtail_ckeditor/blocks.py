from django import forms
from wagtail.blocks import FieldBlock
from wagtail.fields import RichTextField
from wagtail_ckeditor.widgets import CKEditor


class CKEditorBlock(FieldBlock):
    """
    StreamField block that uses our CKEditor widget under the hood.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.field = forms.CharField(widget=CKEditor)

    class Meta:
        icon = "doc-full"
