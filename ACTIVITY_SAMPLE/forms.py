from django import forms
class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               "placeholder": "fullname"}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
               "placeholder": "Email"} ))


    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control',
               "placeholder": "Message"}))


    def clean(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("Please enter a Gmail address")
        return email
    #this will check if gmail is contained in email, if not will make u enter a gmail address