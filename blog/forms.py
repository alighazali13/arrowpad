from django import forms
from django.forms import widgets
from .models import *


class blog_form(forms.ModelForm):
    class Meta:
        model = blog
        fields = [
            'title',
            'url',
            'brief',
            'content',
            'poster',

        ]
        widgets = {
            'title': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' تحلیل شخصیت ترور؛ بازی GTA V ', 'type':'text'  }),
            'url': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' gtav_trevor ', 'type':'text'  }),
            'brief': forms.Textarea(attrs={ 'class':'form-control', 'placeholder': ' یکی از این شخصیت‌ها، شخصیت ترور فیلیپس است که جزو محبوب‌ترین شخصیت‌های GTA V است و حرف‌های زیادی برای گفتن دارد. ', 'type':'text', 'cols':'40', 'rows':'20'  }),
            'content': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' توضیحات منحصر به فرد ', 'type':'text'  }),
            'poster': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' پوستر ', 'type':'file', 'data-default-file':'/statics/dashboard/assets/img/2849110.png', 'data-max-file-size':'2M' }),
        }

class blogMeta_form(forms.ModelForm):
    class Meta:
        model = blogMeta
        fields = [
            'metaTitle',
            'metaTags',
            'metaDescription',
            'metaKeywords',

        ]
        widgets = {
            'metaTitle': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' تحلیل شخصیت ترور؛ بازی GTA V ', 'type':'text'  }),
            'metaTags': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' میکروسکوپ-ترور-جی تی ای وی ', 'type':'text'  }),
            'metaDescription': forms.Textarea(attrs={ 'class':'form-control', 'placeholder': ' یک مقاله دیگه که براتون ترور از بازی جی نی ای وی رو بردیم زیر میکروسکوپ اروپد و براتون اون رو شرح  دادیم ', 'type':'text', 'cols':'40', 'rows':'10'  }),
            'metaKeywords': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' میکروسکوپ-ترور-جی تی ای وی ', 'type':'text'  }),
            
        }

class blogSlides_form(forms.ModelForm):
    class Meta:
        model = blogSlides
        fields = [
            'image',
        ]
        widgets = {
            'image': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' پوستر ', 'type':'file', 'data-default-file':'/statics/dashboard/assets/img/2849110.png', 'data-max-file-size':'2M'}),
        }



class blogVideo_form(forms.ModelForm):
    class Meta:
        model = blogVideos
        fields = [
            'url',

        ]
        widgets = {
            'url': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' https://www.aparat.com/video/video/embed/videohash/wsjc298/vt/frame ', 'type':'text'  }),
        }

