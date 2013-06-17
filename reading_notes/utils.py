from BeautifulSoup import BeautifulSoup
from reading_notes.models import Reading, Note, ReadingType
from datetime import datetime
from django.utils import timezone
import urllib2

def update_notes_from_github():
    for reading_type in ReadingType.objects.all():
        try :
            type_url = "https://github.com/watermelonlh/ReadingNotes/tree/gh-pages/repo/" + reading_type.url
            print type_url
            response = urllib2.urlopen(type_url)
            page = response.read()
            soup = BeautifulSoup(page)

            trs = soup.tbody.findAll(attrs = { 'class' : "content" })
            files = [tr.a['href'].split('/')[-1] for tr in trs]
            #print files
            for file in files:
                url = "http://watermelonlh.github.io/ReadingNotes/repo/" + reading_type.url + "/" + file
                print url
                response = urllib2.urlopen(url)
                doc = response.read()
                soup = BeautifulSoup(doc)

                title, = soup.body.h2.contents
                title = str(title).split('.')[0]
                author = ""
                if (soup.body.h5 != None):
                    author, = soup.body.h5.contents
                reading, created = Reading.objects.get_or_create(title=str(title), reading_type=reading_type)

                update_date = None
                if (not created):
                    exist_note = Note.objects.filter(reading=reading).order_by('-create_date')
                    if (exist_note):
                        update_date = reading.update_date
                divs = soup.body.div.findAll('div')
                divs_len = len(divs)

                #print "title: %s" % str(title)

                #print "author: %s" % str(author)
                i = 0
                while i + 3 < divs_len:
                    note_date = timezone.make_aware(datetime.strptime(divs[i + 1].contents[0], "%Y-%m-%d %H:%M:%S"), timezone.get_current_timezone())
                    note_contents = divs[i + 2].contents[0]
                    if (update_date is None or note_date > update_date): 
                        Note.objects.get_or_create(reading=reading, context=str(note_contents), create_date=note_date)
                    #print "'%s'" % str(note_contents)
                    i += 3
                reading.update_date = datetime.utcnow().replace(tzinfo=timezone.utc)
                if len(author) > 0:
                    reading.author = author
                reading.save()
        except Exception as e:
            print e
