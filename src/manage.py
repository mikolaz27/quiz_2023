#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local_test")
    if sys.argv[1] == "test":
        print("NOTE: Running black formation:")
        print(os.popen(f"black --config {Path(__file__).resolve().parent.parent}/.black.toml .").read())
        print(os.popen("isort .").read())
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()


# 1. Пришвидшує процес розробки
# 2. Інкапсуляція
# 3. Передбачувана поведінка на всіх етапах розробки
# 4. Моніторинг
# 5. Можливість масштабування


# 1. IaaS - infractructure as a service
# 2. PaaS - platform as a service
# 3. SaaS - software as a service



# 750h - 1
# 375h - 2
# 75h - 10
#
#
# """Free tier: In your first year includes 750 hours of t2.micro
# (or t3.micro in the Regions in which t2.micro is unavailable)
# instance usage on free tier AMIs per month, 30 GiB of EBS storage,
# 2 million IOs, 1 GB of snapshots,
# and 100 GB of bandwidth to the internet."""
