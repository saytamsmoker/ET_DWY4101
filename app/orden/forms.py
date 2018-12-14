from .models import Orden
from django import forms

class OrdenForm(forms.ModelForm):

    class Meta:
        model = Orden

        fields = [
            'folio',
            'fk_cli',
            'fk_tec',
            'fecha',
            'hr_in',
            'hr_tr',
            'fk_asc',
            'fails',
            'rep',
            'pi_ch',
            'nom_rec',
        ]
        labels = {
            'folio': 'N° Folio',
            'fk_cli': 'Cliente',
            'fk_tec': 'Tecnico',
            'fecha': 'Fecha',
            'hr_in': 'Hora inicio',
            'hr_tr': 'Hora Termino',
            'fk_asc': 'Ascensor',
            'fails': 'Fallas detectadas',
            'rep': 'Reparaciones efectuadas',
            'pi_ch': 'Piezas Cabmiadas',
            'nom_rec': 'Nombre quien recepciona',
        }
        wirdgets = {
            'folio': forms.TextInput(attrs={'class':'form-control','placeholder':'00000'}),
            'fk_cli': forms.Select(attrs={'class':'form-control'}),
            'fk_tec': forms.Select(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'hr_in': forms.TimeInput(attrs={'class':'form-control'}),
            'hr_tr': forms.TimeInput(attrs={'class':'form-control'}),
            'fk_asc': forms.Select(attrs={'class':'form-control'}),
            'fails': forms.TextInput(attrs={'class':'form-control'}),
            'rep': forms.TextInput(attrs={'class':'form-control'}),
            'pi_ch': forms.TextInput(attrs={'class':'form-control'}),
            'nom_rec': forms.TextInput(attrs={'class':'form-control'}),
        }