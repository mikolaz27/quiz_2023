from django.contrib import admin

from quiz.models import Category, Choice, Question, Quiz

admin.site.register([Quiz, Question, Choice, Category])
