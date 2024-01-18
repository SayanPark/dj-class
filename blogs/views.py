from django.db.models import Avg, Max, Min
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Product

# Create your views here.
all_post = [
    {'slug': 'python-programing',
     'title': 'Python',
     'author': 'Pouya Pormanesh',
     'image': 'Python.png',
     'date': date(1402, 1, 20),
     'short_description': 'Python is a high-level, general-purpose programming language.',
     'content': '''Python is a high-level, general-purpose programming language. 
                   Its design philosophy emphasizes code readability with the use of significant indentation.
                   Python is dynamically typed and garbage-collected.
                   It supports multiple programming paradigms, including structured, object-oriented and functional programming.'''
     },
    {'slug': 'c-programing',
     'title': 'C#',
     'author': 'Kim Gomini',
     'image': 'C_Sharp.png',
     'date': date(1401, 9, 25),
     'short_description': 'C# is a general-purpose high-level programming language supporting multiple paradigms.',
     'content': '''C# is a general-purpose high-level programming language supporting multiple paradigms.
                   C# encompasses static typing, strong typing, lexically scoped, imperative, declarative, functional, generic, object-oriented, and component-oriented programming disciplines.'''
     },
    {'slug': 'php-programing',
     'title': 'PHP',
     'author': 'Sayan Park',
     'image': 'PHP.png',
     'date': date(1399, 5, 7),
     'short_description': 'php is for developing websites',
     'content': '''PHP is a general-purpose scripting language geared towards web development.
                   It was originally created by Danish-Canadian programmer Rasmus Lerdorf in 1993 and released in 1995.
                   The PHP reference implementation is now produced by the PHP Group.'''
     }
]


def get_date(post):
    return post['date']


def index(request):
    # d = list(all_post)
    # context = {'a': d}
    # return render(request, 'blogs/index.html', context)
    post_sorted = sorted(all_post, key=get_date)
    leatests = post_sorted[-2:]
    return render(request, 'blogs/index.html', {'leatest_posts': leatests})


def posts(request):
    return render(request, 'blogs/all_posts.html', {'all_posts': all_post})


def single_post(request, slug):
    post = next(post for post in all_post if post['slug'] == slug)
    return render(request, 'blogs/post_details.html', {'post': post})


def list_of_products(request):
    all_products = Product.objects.all().order_by('-price')
    num = all_products.count()
    info = all_products.aggregate(Avg('price'), Max('price'), Min('price'))
    return render(request, 'blogs/product_list.html', {'all_products': all_products,
                                                                           'numbers': num,
                                                                           'info': info})


def details_of_product(request, slug):
    # try:
    #     pro = Product.objects.get(id=p_id)
    # except:
    #     raise Http404
    pro = get_object_or_404(Product, slug=slug)
    return render(request, 'blogs/product_details.html', {'pro': pro})
