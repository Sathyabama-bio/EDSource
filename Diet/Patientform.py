from django import forms


class Patient(forms.Form):
    fname = forms.CharField(label="First Name",widget=forms.TextInput)
    mname = forms.CharField(label="Middle Name",required=False, widget=forms.TextInput)
    lname = forms.CharField(label="Last Name",widget=forms.TextInput)
    email = forms.EmailField(label="Email",widget=forms.TextInput)
    CHOICES = [('M','Male'), ('F','Female')]
    sex = forms.CharField(label="Sex",widget=forms.RadioSelect(attrs={'class' : 'radio-inline'},choices=CHOICES))
    dob = forms.DateField(label='Date Of Birth',widget=forms.SelectDateWidget)
    height = forms.FloatField(label='Height',widget=forms.NumberInput)
    weight = forms.FloatField(label='Weight',widget=forms.NumberInput)
    phonenumber = forms.IntegerField(label='Phone',widget=forms.NumberInput)

class PatientHistory(forms.Form):
    CHOICES = [('S', 'Yes'), ('N', 'No')]
    diabetes = forms.CharField(label="Have you ever been diagnosed with Diabetes?",widget=forms.RadioSelect(choices=CHOICES))
    diabetes_long = forms.CharField(label="If Yes, how long have you been diagnosed with Diabetes?",required=False,widget=forms.TextInput)
    HbA1c = forms.FloatField(label="HbA1C",required=False,widget=forms.TextInput)
    fasting = forms.FloatField(label="Fasting",required=False,widget=forms.TextInput)
    pp = forms.FloatField(label="PP",required=False,widget=forms.TextInput)
    familyhistory = forms.CharField(label="Do you have a history of Diabetes in your family?",widget=forms.RadioSelect(choices=CHOICES))
    hypertension = forms.CharField(label="Have you ever been diagnosed with Obesity?",required=False,widget=forms.RadioSelect(choices=CHOICES))
    hypertension_long = forms.CharField(label="If Yes, how long have you been diagnosed with Obesity?",required=False,widget=forms.TextInput)
    obesity = forms.CharField(label="Have you ever been diagnosed with Hypertension?",widget=forms.RadioSelect(choices=CHOICES))
    obesity_long = forms.CharField(label="If Yes, how long have you been diagnosed with Hypertension?",required=False,widget=forms.TextInput)
    pcod = forms.CharField(label="Have you ever been diagnosed with PCOD/PCOS?",widget=forms.RadioSelect(choices=CHOICES))
    pcod_long = forms.CharField(label="If Yes, how long have you been diagnosed with PCOD/PCOS?",required=False,widget=forms.TextInput)
    thyroid = forms.CharField(label="Have you ever been diagnosed with Thyroid problems?",widget=forms.RadioSelect(choices=CHOICES))
    thyroid_long = forms.CharField(label="If Yes, how long have you been diagnosed with Thyroid problems?",required=False,widget=forms.TextInput)
    heartdisease = forms.CharField(label="Have you ever been diagnosed with Heart disease?",widget=forms.RadioSelect(choices=CHOICES))
    heartdisease_long = forms.CharField(label="If Yes, how long have you been diagnosed with Heart disease?",required=False,widget=forms.TextInput)
    liverdisease = forms.CharField(label="Have you ever been diagnosed with Liver disease?",widget=forms.RadioSelect(choices=CHOICES))
    liverdisease_long = forms.CharField(label="If Yes, how long have you been diagnosed with Liver disease?",required=False,widget=forms.TextInput)
    kidney = forms.CharField(label="Have you ever been diagnosed with Liver disease?",widget=forms.RadioSelect(choices=CHOICES))
    kidney_long = forms.CharField(label="If Yes, how long have you been diagnosed with Kidney disease?",required=False,widget=forms.TextInput)
    currentmed = forms.CharField(label="Your current Medication:",required=False,widget=forms.TextInput)
    CHOICES = [('V', 'Veg'), ('N', 'Non-Veg')]
    foodhabit = forms.CharField(label="Your Food habit:",widget=forms.RadioSelect(choices=CHOICES))
