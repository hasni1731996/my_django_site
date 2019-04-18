import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosite.settings")
django.setup()

import threading
thread1 = threading.Thread(target=function_1)
thread2 = threading.Thread(target=function_2)
# Will execute both in parallel
thread1.start()
thread2.start()
