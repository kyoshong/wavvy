import django
django.setup()
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wavvy.settings")
from datetime import datetime, timedelta
from analysis.models import ForcastData

def delete_outdated_notice():
    notices = ForcastData.objects.filter(date__lte=datetime.now() - timedelta(days=1))
    print("Delete {} notices.".format(len(notices)))
    notices.delete()


if __name__ == '__main__':
    delete_outdated_notice()