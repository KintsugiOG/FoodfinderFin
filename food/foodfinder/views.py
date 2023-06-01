from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'foodfinder/index.html')


def catalog(request):
    return render(request, 'foodfinder/catalog.html')


def recipes(request):
    return render(request, 'foodfinder/recipes.html')


def logout(request):
    return render(request, 'foodfinder/recipes.html')


def plov(request):
    return render(request, 'foodfinder/dishes/plov.html')


def chcr(request):
    return render(request, 'foodfinder/dishes/chickencurry.html')


def cesar(request):
    return render(request, 'foodfinder/dishes/cesar.html')


def shrimppasta(request):
    return render(request, 'foodfinder/dishes/shrimppasta.html')


def shrimprice(request):
    return render(request, 'foodfinder/dishes/shrimprice.html')


def kartofragu(request):
    return render(request, 'foodfinder/dishes/kartofragu.html')


def draniki(request):
    return render(request, 'foodfinder/dishes/draniki.html')


def dereven(request):
    return render(request, 'foodfinder/dishes/dereven.html')


def pastapesto(request):
    return render(request, 'foodfinder/dishes/pastapesto.html')


def bolognese(request):
    return render(request, 'foodfinder/dishes/bolognese.html')


def olivier(request):
    return render(request, 'foodfinder/dishes/olivier.html')


def mimosa(request):
    return render(request, 'foodfinder/dishes/mimosa.html')


def chikenpineapple(request):
    return render(request, 'foodfinder/dishes/chikenpineapple.html')


def chinese(request):
    return render(request, 'foodfinder/dishes/chinese.html')


def goulash(request):
    return render(request, 'foodfinder/dishes/goulash.html')


def rukkbeef(request):
    return render(request, 'foodfinder/dishes/rukkbeef.html')


def chakhokhbili(request):
    return render(request, 'foodfinder/dishes/chakhokhbili.html')


def risotto(request):
    return render(request, 'foodfinder/dishes/risotto.html')


def shawarma(request):
    return render(request, 'foodfinder/dishes/shawarma.html')


def zapekanka(request):
    return render(request, 'foodfinder/dishes/zapekanka.html')

def lasagna(request):
    return render(request, 'foodfinder/dishes/lasagna.html')

def wok(request):
    return render(request, 'foodfinder/dishes/wok.html')


def greek(request):
    return render(request, 'foodfinder/dishes/greek.html')


def mozzarukk(request):
    return render(request, 'foodfinder/dishes/mozzarukk.html')

def stuffedpep(request):
    return render(request, 'foodfinder/dishes/stuffedpep.html')


def chicksoup(request):
    return render(request, 'foodfinder/dishes/chicksoup.html')

def pizzamar(request):
    return render(request, 'foodfinder/dishes/pizzamar.html')

def shrimproll(request):
    return render(request, 'foodfinder/dishes/shrimproll.html')


def frenchsoup(request):
    return render(request, 'foodfinder/dishes/frenchsoup.html')


def beefstroganoff(request):
    return render(request, 'foodfinder/dishes/beefstroganoff.html')