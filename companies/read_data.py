import csv
from companies.models import realestatedata
from django.contrib.auth.models import User
user=User.objects.get(username='hassan')
with open('C:/Users/Muhammad Hassan/PycharmProjects/django-projects-master/Django_site/test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        street=row[0]
        city=row[1]
        zip=row[2]
        state=row[3]
        beds=row[4]
        baths=row[5]
        new_revo = realestatedata(user=user,street=street, city=city,zip=zip,state=state,beds=beds,baths=baths)
        new_revo.save()

