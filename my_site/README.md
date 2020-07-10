Login to admin: SF
Password: 123
route for check: /publish
см. views.py


Book.objects.all().filter(debeter=Friend.objects.all().filter(full_name='Friend1').first())