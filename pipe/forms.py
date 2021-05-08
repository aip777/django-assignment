from django import forms
from .models import Pipe, Coating, Contents
# external admin form start

class AddPipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPipeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pipe
        fields = ('pipe_od','pipe_od_unit','pipe_wt', 'pipe_wt_unit',
                  'pipe_density', 'pipe_density_unit', 'corrosion_allowance','corrosion_allowance_unit'
                  )



class EditPipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditPipeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pipe
        fields = ('pipe_od','pipe_od_unit','pipe_wt', 'pipe_wt_unit',
                  'pipe_density', 'pipe_density_unit', 'corrosion_allowance','corrosion_allowance_unit'
                  )


class AddCoatingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddCoatingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Coating
        fields = ('coating_no','description', 'thickness',
                  'density'
                  )



class AddContentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddContentsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Contents
        fields = ('installation_empty','installation_empty_content',
                   'flooded','flooded_content','hydrotest','hydrotest_content','description'
                  )
