from django.forms import *

from core.arp.models import Category

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'form-control'
        
        self.fields['name'].widget.attrs['autofocus'] = True


    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs = {
                    'placeholder': 'Ingrese el nombre',
                }
            ),
            'desc': Textarea(
                attrs = {
                    'placeholder': 'Ingrese la descripcion',
                    'rows': 3,
                    'cols': 3
                }
            )
        }
