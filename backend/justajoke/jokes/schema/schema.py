import graphene
from .queries.JokeQueries import JokeQueries
from .queries.ProceedQueries import ProceedQueries

from .mutations.JokeMutations import JokeMutations


class Query(JokeQueries, ProceedQueries, graphene.ObjectType):
    pass

class Mutation(JokeMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation = Mutation)