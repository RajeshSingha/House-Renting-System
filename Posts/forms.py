from django.forms import ModelForm
from .models import Post


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'price', 'is_for_sale', 'rooms', 'floor', 'address', 'city', 'description',
                  'image_1', 'image_2', 'image_3'
                  ]
