# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from mypaginator import MyPaginator
from .models import BjjydyArticle, Kt
from .forms import BjjydyArticleForm, KtForm
from django.http import  HttpResponseRedirect
from  django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

# Create your views here.
#登录
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('infomanage:bjjydy'))
        else:
            dicts = {
                'login_error': '用户名或密码错误。',
            }
            return render(request, 'infomanage/login.html', dicts)
    else:
        return render(request, 'infomanage/login.html')

#注销
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('infomanage:login'))


# 登录主页面，北京教育（德育）主页面
@login_required
def bjjydy(request):
    if request.method == 'GET':
        bjjydy_article_list = BjjydyArticle.objects.filter()

        # 文章搜索
        year_and_issue = request.GET.get('year_and_issue')
        authors = request.GET.get('authors')
        school = request.GET.get('school')
        title = request.GET.get('title')
        section = request.GET.get('section')
        if year_and_issue:
            bjjydy_article_list = bjjydy_article_list.filter(year_and_issue__contains=year_and_issue)
        if authors:
            bjjydy_article_list = bjjydy_article_list.filter(authors__contains=authors)
        if school:
            bjjydy_article_list = bjjydy_article_list.filter(school__contains=school)
        if title:
            bjjydy_article_list = bjjydy_article_list.filter(title__contains=title)
        if section:
            bjjydy_article_list = bjjydy_article_list.filter(section__contains=section)

        # 显示文章列表
        #bjjydy_article_list = bjjydy_article_list.order_by('-year_and_issue')
        paginator = MyPaginator(bjjydy_article_list, 20, 1)
        page = request.GET.get('page')
        try:
            cur_bjjydy_article_list = paginator.page(page)
        except PageNotAnInteger:
            cur_bjjydy_article_list = paginator.page(1)
        except EmptyPage:
            cur_bjjydy_article_list = paginator.page(paginator.num_pages)

        article_form = BjjydyArticleForm()
        dicts = {
            'cur_bjjydy_article_list': cur_bjjydy_article_list,
            'article_form': article_form,
        }
        return render(request, 'infomanage/bjjydy.html', dicts)

    if request.method == 'POST':

        #文章添加
        article_form = BjjydyArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
        else:
            print(article_form.errors.as_json())
        return HttpResponseRedirect(reverse('infomanage:bjjydy'))
    
#文章删除
@login_required
def article_rem(request, article_id):
    #article = get_object_or_404(BjjydyArticle, pk=article_id)
    BjjydyArticle.objects.get(pk=article_id).delete()
    return HttpResponseRedirect(reverse('infomanage:bjjydy'))

#文章批量删除
@login_required
def article_batch_rem(request):
    ids = request.POST.getlist('article_check')
    idstring = ','.join(ids)
    BjjydyArticle.objects.extra(where=['id IN ('+ idstring +')']).delete()
    return HttpResponseRedirect(reverse('infomanage:bjjydy'))

#文章修改
@login_required
def article_change(request, article_id):
    article = get_object_or_404(BjjydyArticle, pk=article_id)
    if request.method == "GET":
        article_form = BjjydyArticleForm(instance=article)
        return render(request, 'infomanage/bjjydy_article_change.html', {'article_form': article_form,'article_id': article_id,})
    else:
        article_form = BjjydyArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
        else:
            print(article_form.errors.as_json())
        return HttpResponseRedirect(reverse('infomanage:bjjydy'))

#课题主页面
@login_required
def kt(request):
    if request.method == 'GET':
        kt_list = Kt.objects.all()

        # 课题搜索
        year = request.GET.get('year')
        kt_type = request.GET.get('kt_type')
        project_number = request.GET.get('project_number')
        applicant = request.GET.get('applicant')
        school = request.GET.get('school')
        kt_name = request.GET.get('kt_name')
        is_completed_or_not = request.GET.get('is_completed_or_not')

        if year:
            kt_list = kt_list.filter(year=year)
        if kt_type:
            kt_list = kt_list.filter(kt_type__contains=kt_type)
        if project_number:
            kt_list = kt_list.filter(project_number__contains=project_number)
        if applicant:
            kt_list = kt_list.filter(applicant__contains=applicant)
        if school:
            kt_list = kt_list.filter(school__contains=school)
        if kt_name:
            kt_list = kt_list.filter(kt_name__contains=kt_name)
        if is_completed_or_not:
            kt_list = kt_list.filter(is_completed_or_not=is_completed_or_not)

        # 显示课题列表
        paginator = MyPaginator(kt_list, 20, 1)
        page = request.GET.get('page')

        try:
            cur_kt_list = paginator.page(page)
        except PageNotAnInteger:
            cur_kt_list = paginator.page(1)
        except EmptyPage:
            cur_kt_list = paginator.page(paginator.num_pages)

        kt_form = KtForm()
        dicts = {
            'cur_kt_list': cur_kt_list,
            'kt_form': kt_form,
        }
        return render(request, 'infomanage/kt.html', dicts)

    if request.method == 'POST':

        # 课题添加
        kt_form = KtForm(request.POST)
        if kt_form.is_valid():
            kt_form.save()
        else:
            print(kt_form.errors.as_json())
        return HttpResponseRedirect(reverse('infomanage:kt'))

#课题删除
@login_required
def kt_rem(request, kt_id):
    kt = get_object_or_404(Kt, pk=kt_id)
    if kt:
        kt.delete()
    #BjjydyArticle.objects.get(pk=kt_id).delete()
    return HttpResponseRedirect(reverse('infomanage:kt'))

#课题批量删除
@login_required
def kt_batch_rem(request):
    ids = request.POST.getlist('kt_check')
    idstring = ','.join(ids)
    Kt.objects.extra(where=['id IN ('+ idstring +')']).delete()
    return HttpResponseRedirect(reverse('infomanage:kt'))

#课题修改
@login_required
def kt_change(request, kt_id):
    kt = get_object_or_404(Kt, pk=kt_id)
    if request.method == "GET":
        kt_form = KtForm(instance=kt)
        return render(request, 'infomanage/kt_change.html', {'kt_form': kt_form,'kt_id': kt_id,})
    else:
        kt_form = KtForm(request.POST, instance=kt)
        if kt_form.is_valid():
            kt_form.save()
        else:
            print(kt_form.errors.as_json())
        return HttpResponseRedirect(reverse('infomanage:kt'))