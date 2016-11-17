from django.shortcuts import render, redirect
from .models import Person, Interest

def index(request):
    return render(request, 'people/index.html')

def people(request):
    people = Person.objects.all()
    context = {'people': people}
    interests = Interest.objects.all()
    for interest in interests:
        print(interest.name)
    return render(request, 'people/people.html', context)

def show(request, id):
    person = Person.objects.filter(id=id)
    if person:
        interests = Interest.objects.filter(person=person)
        print interests
        context = {'person': person[0], 'interests': interests}
        return render(request, 'people/show.html', context)
    return redirect('people')

def formSubmit(request):
    people = Person.objects.filter(name=request.POST['name'])
    if people:
        person = people[0]
    else:
        person = Person.objects.create(name=request.POST['name'])

    interests = Interest.objects.filter(name=request.POST['interest'])
    if interests:
        interest = interests[0]
    else:
        interest = Interest.objects.create(name=request.POST['interest'])

    interest.person.add(person)

    return redirect('/people')

# Create your views here.
