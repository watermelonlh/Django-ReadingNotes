# Create your views here.
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from django.http import HttpResponse

from reading_notes.models import Note, Reading, ReadingType
from reading_notes.utils import update_notes_from_github

def index(request):
    return render_to_response('reading_notes/index.html', {}, context_instance=RequestContext(request))

def readings(request):
    year = request.GET.get('year')
    month = int(request.GET.get('month')) + 1
    res = Note.objects.filter(create_date__year=year, create_date__month=month).distinct('reading')
    return HttpResponse(simplejson.dumps([{ "title" : unicode(a.reading), "reading_id" : a.reading_id } for a in res]), mimetype="application/json")

def detail(request, reading_id):
    notes = Note.objects.filter(reading=reading_id).order_by('create_date')
    print notes
    p = Reading.objects.all()
    print p[0].id
    reading = get_object_or_404(Reading, pk=reading_id)
    return render(request, 'reading_notes/detail.html', {'notes' : notes, 'reading' : reading})

def update(request):
    update_notes_from_github()
    return render(request, 'reading_notes/update.html')
