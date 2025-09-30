from django import forms

class LoginForms(forms.Form):
        nome_login = forms.CharField(
                label='Nome de Login',
                required=True,
                max_length=100,
                widget=forms.TextInput(
                        attrs={
                                'class': 'form-control',
                                'placeholder': 'Ex.: João Silva',
                        }
                )
        )  
        senha = forms.CharField(
                label='Senha',
                max_length=100,
                required=True,
                widget=forms.PasswordInput(
                        attrs={
                                'class': 'form-control',
                                'placeholder': 'Digite sua senha',
                        }                        
                ),
        )

class CadastroForms(forms.Form):
        nome_login = forms.CharField(
                label='Nome de Login',
                required=True,
                max_length=100,
                widget=forms.TextInput(
                        attrs={
                                'class': 'form-control',
                                'placeholder': 'Ex.: João Silva',
                        }
                )
        )
        email = forms.EmailField(
                label='E-mail',
                required=True,
                max_length=100,
                widget=forms.EmailInput(
                        attrs={
                                'class': 'form-control',
                                'placeholder': 'jaoa@xpto.com',
                        }
                )
        )  
        senha1 = forms.CharField(
                label='Senha',
                max_length=100,
                required=True,
                widget=forms.PasswordInput(
                        attrs={
                                'class': 'form-control',
                                'placeholder': 'Senha',
                        }
                ),
        )
        senha2 = forms.CharField(
                label='Confirmação de Senha',
                max_length=100,
                required=True,
                widget=forms.PasswordInput(
                        attrs={
                                'class': 'form-control',
                                'placeholder': 'Comfirme a senha',
                        }
                ),
        )

        def clean_nome_login(self):
                nome = self.cleaned_data.get('nome_login')

                if nome:
                        nome = nome.strip()
                        if " " in nome:
                                raise forms.ValidationError('Não é possivel inserir espaços no campo usuário')
                        else:
                                return nome
                