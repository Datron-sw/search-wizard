from django import forms

class SearchQueryForm(forms.Form):
    search_engine = forms.ChoiceField(
        choices=[
            ('', 'tarayici seç'),
            ('google', 'Google'),
            ('yandex', 'Yandex'),
            ('brave', 'Brave'),
            ('edge', 'Microsoft Edge'),
        ],
        widget=forms.Select(attrs={'class':'form-select', 'aria-label':'Default select example'}),
        required=False,  
    )
    
    file_type = forms.ChoiceField(
        choices=[
            ('pdf', 'Pdf'),
            ('exe', 'Exe'),
            ('rar', 'Rar'),
            ('docx', 'Docx'),
        ],
        widget=forms.Select(attrs={'class':'form-select', 'size':'3', 'aria-label':'Size 3 select example'}),
        required=False  
    )
    
    search_type = forms.ChoiceField(
        choices=[
            ('book', 'Kitap'),
            ('article', 'Makale'),
            ('image', 'Görsel'),
            ('download', 'İndirme'),
        ],
        widget=forms.Select(attrs={'class':'form-select','size':'3', 'aria-label':'Size 3 select example'}),
        required=False  
    )
    
    search_input = forms.CharField(
        widget=forms.TextInput(attrs={'class':'girdi', 'placeholder':'Ne aramak istiyorsunuz ', 'autocomplete': 'off'}),
        required=False  
    )
    
    selected_site = forms.CharField(
        widget=forms.TextInput(attrs={'class':'girdi', 'placeholder':'https://www.example.com/', 'autocomplete': 'off'}),
        required=False  
    )
    selected_language = forms.ChoiceField(
        choices=[
            ('türkçe', 'Türkçe'),
            ('ingilizce', 'İngilizce'),
            ('fransizca', 'Fransizca'),
            ('almanca', 'Almanca')
        ],
        widget=forms.Select(attrs={'class':'form-select', 'aria-label':'Default select example'}),
        required=False,  
    )


    

