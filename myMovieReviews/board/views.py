from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from django.urls import reverse


# Create your views here.

def board_create(request):
    if request.method == 'POST':
        # board = Board.objects.create(
        #     title2 = request.POST['title'],
        #     releaseYear = request.POST['releaseYear'],
        #     genre = request.POST['genre'],
        #     rating = request.POST['rating'],
        #     producer =request.POST['producer'],
        #     actors = request.POST['actors'],
        #     runningTime  = request.POST['runningTime'],
        #     review = request.POST['review'],
        # )
        title = request.POST.get('title')
        releaseYear = request.POST.get('releaseYear')
        genre = request.POST.get('genre')
        rating = request.POST.get('rating')
        producer = request.POST.get('producer')
        actors = request.POST.get('actors')
        runningTime = request.POST.get('runningTime')
        review = request.POST.get('review')

        print(f"제목: {title}, 개봉년도: {releaseYear}, 장르: {genre}")
        board = Board.objects.create(
            title=title,
            releaseYear=releaseYear,
            genre=genre,
            rating=rating,
            producer=producer,
            actors=actors,
            runningTime=runningTime,
            review=review,
        )
        return redirect(reverse('board:board_list'))
    return render(request, 'board/create.html')

def board_list(request):
    boards = Board.objects.all()
    context = {'boards' : boards}
    return render(request, 'board/list.html', context)


def board_update(request, pk):
    board = get_object_or_404(Board, id=pk)  
    if request.method == "POST":
            title2 = request.POST['title']
            releaseYear2 = request.POST['releaseYear']
            genre2 = request.POST['genre']
            rating2 = request.POST['rating']
            producer2 =request.POST['producer']
            actors2 = request.POST['actors']
            runningTime2  = request.POST['runningTime']
            review2 = request.POST['review']

            board.title =title2
            board.releaseYear =releaseYear2
            board.genre =genre2
            board.rating =rating2
            board.producer =producer2
            board.actors =actors2
            board.runningTime = runningTime2
            board.review = review2

            board.save()
            return redirect('board:board_detail', pk=board.pk)
    # context={
    #         'title' : title2,
    #         'releaseYear' : releaseYear2,
    #         'genre' : genre2,
    #         'rating' : rating2,
    #         'producer' : producer2,
    #         'actors' : actors2,
    #         'runningTime' : runningTime2,
    #         'review' : review2,
    # }
    # boards = Board.objects.all()
    return render(request, 'board/update.html',{'board':board})


def board_detail(request,pk):
    boards = Board.objects.get(id=pk)
    context = {
        'board' : boards,
    }     
    return render(request, 'board/detail.html', context)


def board_delete(request,pk):
    board = Board.objects.get(id=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('board:board_list')
    return redirect('board:board_list')