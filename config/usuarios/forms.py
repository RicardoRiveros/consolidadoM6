from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")


        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        # Guardar el usuario, creando un usuario con la contraseña correctamente cifrada
        usuario = super().save(commit=False)
        password = self.cleaned_data["password1"]
        usuario.set_password(password)

        if commit:
            usuario.save()
        return usuario

    

    
