import graphene
from ..types.JokeType import JokeType
from ...models import joke
import queue
class JokeQueries:
    jokes = graphene.List(JokeType)
    joke = graphene.Field(JokeType, id=graphene.Int())
    
    def resolve_jokes(self, info):
        return joke.objects.all()
    def resolve_joke(self, info, id):
        return joke.objects.get(pk=id)
    def number_jokes(self, info):
        return joke.objects.count()
    def verified_jokes(self, info):
        return joke.objects.filter(verified=True)
    
    #get 10 random verified jokes
    def random_verified_jokes(self, info, num_jokes=10):
        jokes_queue = queue.Queue()
        for joke in joke.objects.filter(verified=True).order_by('?')[:num_jokes]:
            jokes_queue.put(joke)

        return jokes_queue