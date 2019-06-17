from django.shortcuts import render
from .models import MovieModel,TVModel,CartoonModel,ZongyiModel,Category
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    new_movies=MovieModel.objects.all().order_by('-time')[:12]
    new_tvs = TVModel.objects.all().order_by('-time')[:12]
    new_cartoons = CartoonModel.objects.all().order_by('-time')[:12]
    new_zongyis = ZongyiModel.objects.all().order_by('-time')[:12]
    category=Category.objects.get(category=1)
    category.count+=1
    category.save()
    context={
        'new_movies':new_movies,
        'new_tvs':new_tvs,
        'new_cartoons':new_cartoons,
        'new_zongyis':new_zongyis
    }
    return render(request,'index.html',context)

def search(request):
    if request.method=='POST':
        content=request.POST.get('content')
        movie=MovieModel.objects.filter(title__contains=content)
        for m in movie:
            m.video='movie'
            m.save()
        tv = TVModel.objects.filter(title__contains=content)
        for m in tv:
            m.video='tv'
            m.save()
        zongyi = ZongyiModel.objects.filter(title__contains=content)
        for m in zongyi:
            m.video='zongyi'
            m.save()
        cartoon = CartoonModel.objects.filter(title__contains=content)
        for m in cartoon:
            m.video='cartoon'
            m.save()
        video=[]
        video.extend(movie)
        video.extend(tv)
        video.extend(zongyi)
        video.extend(cartoon)
        if content:
            if video:
                context={
                    'movie_list':video,
                    'content':content
                }
                return render(request,'search.html',context)
            else:
                return render(request,'search.html')
        return render(request, 'search.html')

def list(request,type,type2='all',country='all',year='all',page_num=1):
    if type=='movie':
        if type2!='all':
            if country=='all':
                if year=='all':
                    all_movies = MovieModel.objects.filter(type=type2).order_by('-time')
                else:
                    all_movies = MovieModel.objects.filter(type=type2,year=year).order_by('-time')
            else:
                if year=='all':
                    all_movies = MovieModel.objects.filter(type=type2, country=country).order_by('-time')
                else:
                    all_movies = MovieModel.objects.filter(type=type2, country=country,year=year).order_by('-time')
        else:#type2==all
            if country=='all':
                if year=='all':
                    all_movies = MovieModel.objects.all().order_by('-time')
                else:
                    all_movies = MovieModel.objects.filter(year=year).order_by('-time')
            else:
                if year == 'all':
                    all_movies = MovieModel.objects.filter(country=country).order_by('-time')
                else:
                    all_movies = MovieModel.objects.filter(country=country,year=year).order_by('-time')
    if type=='tv':
        if type2!='all':
            if country=='all':
                if year=='all':
                    all_movies = TVModel.objects.filter(type=type2).order_by('-time')
                else:
                    all_movies = TVModel.objects.filter(type=type2,year=year).order_by('-time')
            else:
                if year=='all':
                    all_movies = TVModel.objects.filter(type=type2, country=country).order_by('-time')
                else:
                    all_movies = TVModel.objects.filter(type=type2, country=country,year=year).order_by('-time')
        else:#type2==all
            if country=='all':
                if year=='all':
                    all_movies = TVModel.objects.all().order_by('-time')
                else:
                    all_movies = TVModel.objects.filter(year=year).order_by('-time')
            else:
                if year == 'all':
                    all_movies = TVModel.objects.filter(country=country).order_by('-time')
                else:
                    all_movies = TVModel.objects.filter(country=country,year=year).order_by('-time')
    if type=='zongyi':
        if type2!='all':
            if country=='all':
                if year=='all':
                    all_movies = ZongyiModel.objects.filter(type=type2).order_by('-time')
                else:
                    all_movies = ZongyiModel.objects.filter(type=type2,year=year).order_by('-time')
            else:
                if year=='all':
                    all_movies = ZongyiModel.objects.filter(type=type2, country=country).order_by('-time')
                else:
                    all_movies = ZongyiModel.objects.filter(type=type2, country=country,year=year).order_by('-time')
        else:#type2==all
            if country=='all':
                if year=='all':
                    all_movies = ZongyiModel.objects.all().order_by('-time')
                else:
                    all_movies = ZongyiModel.objects.filter(year=year).order_by('-time')
            else:
                if year == 'all':
                    all_movies = ZongyiModel.objects.filter(country=country).order_by('-time')
                else:
                    all_movies = ZongyiModel.objects.filter(country=country,year=year).order_by('-time')

    if type=='cartoon':
        if type2!='all':
            if country=='all':
                if year=='all':
                    all_movies = CartoonModel.objects.filter(type=type2).order_by('-time')
                else:
                    all_movies = CartoonModel.objects.filter(type=type2,year=year).order_by('-time')
            else:
                if year=='all':
                    all_movies = CartoonModel.objects.filter(type=type2, country=country).order_by('-time')
                else:
                    all_movies = CartoonModel.objects.filter(type=type2, country=country,year=year).order_by('-time')
        else:#type2==all
            if country=='all':
                if year=='all':
                    all_movies = CartoonModel.objects.all().order_by('-time')
                else:
                    all_movies = CartoonModel.objects.filter(year=year).order_by('-time')
            else:
                if year == 'all':
                    all_movies = CartoonModel.objects.filter(country=country).order_by('-time')
                else:
                    all_movies = CartoonModel.objects.filter(country=country,year=year).order_by('-time')

    paginator=Paginator(all_movies,36)
    page=paginator.page(page_num)

    context={
        'type':type,
        'type2':type2,
        'country':country,
        'year':year,
        'all_movies':all_movies,
        'page':page,
        'page_num':page_num,
    }
    return render(request,'list.html',context)

def detail(request,type,id):
    video=''

    if type=='movie':
        movie=MovieModel.objects.filter(id=id)
        if movie:
            movie=movie[0]
            video=movie
            url_list = []
            xiangguanvideo=MovieModel.objects.filter(type=video.type).order_by('-time')[:12]
    if type=='tv':
        movie = TVModel.objects.filter(id=id)
        if movie:
            movie = movie[0]
            video = movie
            url_list=eval(video.url_lists)
            xiangguanvideo = TVModel.objects.filter(type=video.type).order_by('-time')[:12]
    if type=='zongyi':
        movie = ZongyiModel.objects.filter(id=id)
        if movie:
            movie = movie[0]
            video = movie
            url_list=eval(video.url_lists)
            xiangguanvideo = ZongyiModel.objects.filter(type=video.type).order_by('-time')[:12]
    if type=='cartoon':
        movie = CartoonModel.objects.filter(id=id)
        if movie:
            movie = movie[0]
            video = movie
            url_list=eval(video.url_lists)
            xiangguanvideo = CartoonModel.objects.filter(type=video.type).order_by('-time')[:12]
    context={
        'type':type,
        'video':video,
        'xiangguanvideo':xiangguanvideo,
        'url_lists':url_list,

    }
    return render(request,'detail.html',context)

def video(request,type,id):
    if request.method=='POST':
        url=request.POST.get('url','')
        if type == 'tv':
            movie = TVModel.objects.filter(id=id)
            if movie:
                movie = movie[0]
                video = movie
                url_list = eval(video.url_lists)
                xiangguanvideo = TVModel.objects.filter(type=video.type).order_by('-time')[:10]
        if type == 'zongyi':
            movie = ZongyiModel.objects.filter(id=id)
            if movie:
                movie = movie[0]
                video = movie
                url_list = eval(video.url_lists)
                xiangguanvideo = ZongyiModel.objects.filter(type=video.type).order_by('-time')[:10]
        if type == 'cartoon':
            movie = CartoonModel.objects.filter(id=id)
            if movie:
                movie = movie[0]
                video = movie
                url_list = eval(video.url_lists)
                xiangguanvideo = CartoonModel.objects.filter(type=video.type).order_by('-time')[:10]
        context = {
            'type': type,
            'video': video,
            'xiangguanvideo': xiangguanvideo,
            'url':url,
            'url_lists':url_list
        }
        return render(request, 'video.html', context)
    video = ''
    if type == 'movie':
        movie = MovieModel.objects.filter(id=id)
        if movie:
            movie = movie[0]
            video = movie
            url_list=[]
            xiangguanvideo = MovieModel.objects.filter(type=video.type).order_by('-time')[:10]
    if type == 'tv':
        movie = TVModel.objects.filter(id=id)
        if movie:
            movie = movie[0]
            video = movie
            url_list = eval(video.url_lists)
            xiangguanvideo = TVModel.objects.filter(type=video.type).order_by('-time')[:10]
    if type == 'zongyi':
        movie = ZongyiModel.objects.filter(id=id)
        if movie:
            movie = movie[0]
            video = movie
            url_list = eval(video.url_lists)
            xiangguanvideo = ZongyiModel.objects.filter(type=video.type).order_by('-time')[:10]

    if type == 'cartoon':
        movie = CartoonModel.objects.filter(id=id)
        if movie:
            movie = movie[0]
            video = movie
            url_list = eval(video.url_lists)
            xiangguanvideo = CartoonModel.objects.filter(type=video.type).order_by('-time')[:10]

    context = {
        'type': type,
        'video': video,
        'url_lists': url_list,
        'xiangguanvideo': xiangguanvideo
    }

    return render(request,'video.html',context)

