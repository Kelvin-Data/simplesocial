#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simplesocial.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# User = testuser
# Password = testpassword

# User = Kelvin
# Password = simple 789
# Email = simple123@yahoo.com

# User = new_user
# Email = new@gmail.com
# Email = testpassword


# django-admin startapp posts
# django-admin startapp groups

# python -m pip install --upgrade pip
# pip install misaka
# C:\Users\BHL\Source\Repos\misaka\.vs	

