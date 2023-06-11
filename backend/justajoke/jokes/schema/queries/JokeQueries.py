import graphene
from graphene import List
from ..types.JokeType import JokeType
from ...models import joke

class JokeQueries:
    jokes = graphene.List(JokeType)
    joke = graphene.Field(JokeType, id=graphene.Int())
    random_joke = graphene.Field(JokeType)
    random_verified_jokes = List(
        JokeType, num_jokes=graphene.Int(default_value=10))
    number_jokes = graphene.Int()

    def resolve_jokes(self, info):
        return joke.objects.all()
    def resolve_joke(self, info, id):
        return joke.objects.get(pk=id)
    def resolve_number_jokes(self, info):
        return joke.objects.count()
    def resolve_verified_jokes(self, info):
        return joke.objects.filter(verified=True)
    #pull a random joke
    def resolve_random_joke(self, info):
        return joke.objects.filter(verified=True).order_by('?').first()
    #get 10 random verified jokes
    def resolve_random_verified_jokes(self, info, num_jokes=3):
        return list(joke.objects.filter(verified=True).order_by('?')[:num_jokes])