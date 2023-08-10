from django import forms

from apps.drink.models import Drink


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = '__all__'


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = None
        exclude = ['tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_class()

    def __set_class(self):
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control m-b-25',
                'placeholder': field.label,
            })

        self.fields['image'].widget = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
