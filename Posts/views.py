from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import PostCreateForm
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator

def redirectTo(url):
    return HttpResponseRedirect(reverse(url))

def _create_post(form, u):
    data = form.cleaned_data
    instance = Post.objects.create(user=u)

    instance.title = data['title']
    instance.price = data['price']
    instance.is_for_sale = data['is_for_sale']

    instance.rooms = data['rooms']
    instance.floor = data['floor']
    instance.address = data['address']

    instance.description = data['description']
    instance.city = data['city']

    instance.timestamp = timezone.now()

    instance.image_1 = data['image_1']
    instance.image_2 = data['image_2']
    instance.image_3 = data['image_3']

    instance.save()
    return instance

def create(request):
    c_user = request.user
    if not c_user.is_authenticated:
        return redirectTo('login:login')

    if request.method == 'GET':
        post_form = PostCreateForm()
        ctx = {
            'user': request.user,
            'f': post_form
        }
        return render(request, 'posts/create.html', context=ctx)
    else:
        post_form = PostCreateForm(request.POST, request.FILES)
        if post_form.is_valid():
            p = _create_post(post_form, c_user)
            return HttpResponseRedirect(reverse('post:detail', args=[p.id]))
        return HttpResponse('Error in form')

def posts(request):
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    p = Paginator(Post.objects.all(), 10)

    if page <= 0 or page > p.num_pages:
        page = 1

    posts = p.page(page)

    return render(request, 'posts/posts.html', {'posts': posts, 'user': request.user})

def detail_post(request, p_id):
    post = get_object_or_404(Post, id = p_id)
    ctx = {
        'post': post,
        'user': request.user
    }
    return render(request, 'posts/view.html', context=ctx)