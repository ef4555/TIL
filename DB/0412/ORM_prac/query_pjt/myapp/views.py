from django.shortcuts import render
from django.db import connection
from django.db import reset_queries


from .models import Pet, PetSitter

# Create your views here.

def get_sql_queries(origin_func):
    def wrapper(*args, **kwargs):
        reset_queries()
        origin_func(*args, **kwargs)
        
        query_info = connection.queries
        for query in query_info:
            print(query['sql'])
    return wrapper


@get_sql_queries
def get_pet_data():
    # reset_queries()
    
    pets = Pet.objects.all()
    for pet in pets:
        print(f'{pet.name} |집사 {pet.pet_sitter.first_name}')
        
        # query_info = connection.queries
        # for query in query_info:
        #     print(query['sql'])