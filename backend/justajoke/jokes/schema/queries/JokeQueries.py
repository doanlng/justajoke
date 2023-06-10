import graphene
from ..types.JokeType import JokeType
from ...models import joke

class JokeQueries:
    jokes = graphene.List(JokeType)
    joke = graphene.Field(JokeType, id=graphene.Int())
    
    def resolve_jokes(self, info):
        return joke.objects.all()
    def resolve_joke(self, info, id):
        return joke.objects.get(pk=id)
    def number_jokes(self, info):
        return joke.objects.count()