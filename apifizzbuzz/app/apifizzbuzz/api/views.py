from django.http import HttpResponse
import json

def index(request):

    number = int(request.headers['number'])

    response = "Fizzbuzz" if number % 3==0 and number % 5==0 else "Fizz" if number % 3==0 else "Buzz" if number % 5==0 else str(number) + " is not fizzbuzzable!"
    data = {'response': response}

    return HttpResponse(json.dumps(data), content_type='application/json')

def healthcheck(request):
    return HttpResponse(status=200)