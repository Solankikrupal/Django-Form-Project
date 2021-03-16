from django import forms
from django.core import validators
from FormApp.models import profile

#this commented code is code for the form if you didnt connect form to database so u can use the this code

"""def check_for_z(val):
    if val[0].lower() != 'z':
        raise forms.ValidationError('Ha HA GO HAve Z u ZazkAzz')
"""
"""class FormField(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    e_mail = forms.EmailField()
    feedback = forms.CharField(widget = forms.Textarea)
    botcheck = forms.CharField(required = False , widget = forms.HiddenInput , validators = [ validators.MaxLengthValidator(0)] )
    """
"""
    def bot_check_fun(self):

        botcatcher = self.cleaned_data['botcheck']
        if len(botcatcher) > 0 :
            raise forms.ValidationError('Ha Ha Jokes on You')
        return botcatcher
"""
class NewUser(forms.ModelForm):

    class Meta():

        model = profile
        fields = '__all__'
