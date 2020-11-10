from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import OperationalError

from viewcount.models import Viewcount

#Functions
def is_fizzbuzzable(number):
    return "Fizzbuzz" if number % 3==0 and number % 5==0 else "Fizz" if number % 3==0 else "Buzz" if number % 5==0 else str(number) + " is not fizzbuzzable!"


def get_visit_count():

    visits_db_object = Viewcount.objects.all()
    
    if len(visits_db_object) == 0:
        print("Creating first visit")
        v = Viewcount(visits = 0)
        v.save()
        return v

    return visits_db_object[0]


def increment_visitor_count():
    v = Viewcount.objects.all()[0]
    v.visits += 1
    v.save()
    return


def get_sum_of(number):
    return sum( i for i in range(number + 1))


#Views
def index(request):

    #Handle database connection error
    try:
        visit_num = get_visit_count().visits
        increment_visitor_count()
    except OperationalError as e:
        return HttpResponse("Error, could not connect to the database: " + str(e))

    fizzbuzz = is_fizzbuzzable(visit_num)

    sum_visits = get_sum_of(visit_num)

    response = ["Hello world!", "Visit count is " + str(visit_num), "The fizzbuzz value of your number is: " + fizzbuzz, "The sum of all the visits is: " + str(sum_visits)]

    #Output response using html template
    template = loader.get_template("viewcount/index.html")
    context = {
        "response":response,
    }

    return HttpResponse(template.render(context, request))

def healthcheck(request):
    return HttpResponse(status=200)