from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Page

# Create your views here.

'''def index(request):
    #return HttpResponse('<p>welcome</p>')
    return render(request, 'base.html')'''

def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    #assert False
    return render(request, 'page/page.html', context)

