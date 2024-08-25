from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import os,re,sys
import  subprocess
from django.views.generic import TemplateView, ListView
from django.db.models import Q 
from .models import Topic,Entry
from .forms import TopicFrom,EntryForm,SearchEntry
from django import template
import re
# Create your views here.
@login_required
def index(request):
    """Домашняя страница приложения"""
    return render(request,'Posts/index.html')
@login_required
def topics(request):
    """Выводим темы"""
    topics = Topic.objects.order_by('date_added')#Запрос к БД отсорированный по дате
    context = {'topics': topics} #словарь , харнить данные по ключу  
    return render(request,'Posts/topics.html',context)
@login_required
def topic(request,topic_id):
    """Выводит одну тему и все её записи"""
    topic = Topic.objects.get(id=topic_id)#Получение темы 
    entries = topic.entry_set.order_by('-date_added')#отсортированный вывод
    context = {'topic' : topic,'entries': entries}
    return render(request,'Posts/topic.html',context)
@login_required
def new_topic(request):
    """Опеределяет новую тему"""
    if request.method != 'POST':
        #Данные не отправлялись , создается пустая форма
        form = TopicFrom()
    else:
        #Отправление данные POST,обработать данные
        form = TopicFrom(request.POST)#передаём данные
        if form.is_valid():#проверяет заполнены ли все обязательные поля
            topic = form.save(commit=False)
            topic.owner = request.user
            topic.save()
            #form.save()
            return HttpResponseRedirect(reverse('Posts:topics'))#Переадресация после сохранения данных
    context ={'form':form}
    return render(request,'Posts/new_topic.html',context)
@login_required
def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)#Получение темы 
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic =  topic
            new_entry.user = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('Posts:topic',args=[topic_id]))
    context = {'topic' : topic, 'form': form }
    return render(request,'Posts/new_entry.html',context)
@login_required
def edit_entry(request,entry_id):

    entry = Entry.objects.get(id=entry_id)#Получение записи 
    topic = entry.topic

    if request.method != 'POST':
        #Исходный запрос,форма заполняется текщими данными
        form = EntryForm(instance=entry)#Если не выполняется запрос POST ,то выводится существующая запись
    else:
        #Отправка данных ;обработка данныех
        form = EntryForm(instance=entry,data=request.POST)#При получение запроса POST вносится изменение в существующей записи 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Posts:topic',args=[topic.id]))
    context = {'entry':entry,'topic' : topic, 'form': form }
    return render(request,'Posts/edit_entry.html',context)
@login_required
def history(request):
    text = Entry.objects.order_by('-date_added')
    context = {'text': text}
    return render(request,'Posts/history.html',context)
@login_required
def info(request):
    return render(request,'Posts/info.html')


register = template.Library()


@register.filter

class SearchResultsView(ListView):
    
    model = Entry
    template_name = 'Posts/search.html'
    
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        
        
        #query = re.sub(query,"<font color='red'>{}</font>".format(query),query)
        object_list = Entry.objects.filter(Q(text__icontains=query)).order_by('-date_added')
        return  object_list
            
@login_required
def view_user_profile(request, user_pk):
    user = User.objects.get(pk=user_pk)
    form = UpdateForm(instance=user)
    return render(request, 'Posts/profile.html', {
        'form': form
    })
@login_required
def profiler(request, username):
        k = get_object_or_404(User, username=username)
        return render_to_response("Posts/profilе.html", locals(), context_instance=RequestContext(request))
@login_required
def p_test(request):
    return render(request,'Posts/test.html')

def upload_test(request,data):
    import os, cgi
    data = cgi.FieldStorage()
    upload = data['filename']
    filename = os.path.basename(upload.filename)
    with open(filename,'wb') as f:
        f.write(upload.file.read())
    return render(request,'Posts/upload_test.html')
    
