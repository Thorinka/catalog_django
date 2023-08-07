from django import forms

from catalog.models import Product, Version

BANNED_WORDS = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        for word in BANNED_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Такой продукт создать нельзя')

        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']

        for word in BANNED_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Такой продукт создать нельзя')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"

    # def clean_is_active(self):
    #     cleaned_data = self.cleaned_data['is_active']
    #     current_version = Version.objects.get(is_active=self.get('is_active'))
    #     if cleaned_data is True:
    #         if self.fields.items['is_active'] is True:
    #             raise forms.ValidationError('Одновременно может быть только одна активная версия')
    #
    #     return cleaned_data
