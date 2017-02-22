#Version : Phython/Django 2.7.6, PostgreSQL 9.3.4
#Author : Vaibhavi Desai
#Github username : desaivaibhavi
#email : ranihaileydesai@gmail.com

#!/usr/bin/env python
import os
import sys
import uuid
from signup.models import Pcuser
from django.core.management import execute_from_command_line
from django.contrib.auth.models import User

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "infohub.settings")

    execute_from_command_line(sys.argv)

    if sys.argv[1]== 'syncdb':
        sys.argv.append('--noinput')
        name='maccadmin'
        email='macc@systers.com'
        password = 'maccpassword'
        user = User.objects.create_superuser(name,email,password)
        user.first_name = ''
        user.last_name = ''
        user = Pcuser(user=user , location="", phone="",  gender="", reset_pass="", verified = uuid.uuid4().hex)
        user.save()
