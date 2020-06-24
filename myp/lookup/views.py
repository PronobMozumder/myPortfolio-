from django.shortcuts import render
from. models import myinfo, education, experience, awards, services


def index(request):
    myin = myinfo.objects.get()
    eduList = education.objects.all()
    expList = experience.objects.all()
    awardsList = awards.objects.all()
    servicesList = services.objects.all()
    # myinfo.name = 'Pronob'
    # myinfo.age = 20
    # myin = myinfo()

    return render(request, 'index.html', {
        'info': myin, 
        'education': eduList, 
        'experience': expList, 
        'awards':awardsList,
        'services':servicesList,
        })


def test(request):
    # myin = myinfo.objects.all().first()
    myin = myinfo.objects.get(id=1)
    # print("string", myin.name)

    return render(request, 'test.html', {'t': myin})
