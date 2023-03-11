from django.http import HttpResponse
from faker import Faker

from blog.models import Blog, Entry


def create_blog(request):
    faker = Faker()
    saved = Entry(
        blog=[Blog(name=faker.word(), text=faker.paragraph(nb_sentences=5), author=faker.word()) for _ in range(10)],
        headline=faker.paragraph(nb_sentences=1),
    ).save()
    return HttpResponse(f"Done: {saved}")


def all_blogs(request):
    blogs_timestamps = list(Entry.objects.values_list("timestamp"))

    print(blogs_timestamps)

    return HttpResponse(f"Done: {blogs_timestamps}")
