import graphene
from .queries.JokeQueries import JokeQueries
from .mutations.JokeMutations import JokeMutations

class Query(JokeQueries, graphene.ObjectType):
    pass

class Mutation(JokeMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation = Mutation)