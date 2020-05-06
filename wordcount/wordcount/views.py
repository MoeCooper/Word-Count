from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def count(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word not in word_dictionary:
            word_dictionary[word] = 1
        else:
            word_dictionary[word] += 1

    return render(request, 'count.html', {'fulltext': full_text, 'count': len(word_list), 'sorted_dictionary': sorted(word_dictionary.items(), reverse=False)})
