from django import forms
from .models import Article

class articleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        content = data.get('content')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title",f"{title} is already taken")
        return data
    

# class articleFormOld(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()

#     def clean_title(self):
#         cleaned_data = self.cleaned_data
#         print("cleaned_data",cleaned_data)
#         title = cleaned_data.get("title")
#         if title.lower().strip() == "the blacklist":
#             raise forms.ValidationError("This title is taken")
#         return title
        