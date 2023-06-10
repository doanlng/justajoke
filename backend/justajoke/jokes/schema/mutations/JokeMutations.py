import graphene
from ..types.JokeType import JokeType
from ...models import joke
import datetime

class JokeMutationAdd(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        punchline = graphene.String(required=True)
        verified = graphene.Boolean(required=False)
        date_submitted = graphene.DateTime(required=False)
    j = graphene.Field(JokeType)

    def mutate(self, info, name, punchline, verified=False):
        j = joke(name=name, punchline=punchline, verified=verified, date_submitted=datetime.datetime.now())
        j.save()
        return JokeMutationAdd(j=j)


class JokeMutationUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        punchline = graphene.String()
        verified = graphene.Boolean()

    j = graphene.Field(JokeType)

    def mutate(self, info, id, name=None, punchline=None, verified=None):
        j = joke.objects.get(id=id)
        if name is not None:
            j.name = name
        if punchline is not None:
            j.punchline = punchline
        if verified is not None:
            j.verified = verified
        j.save()
        return JokeMutationUpdate(j=j)


class JokeMutationDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        j = joke.objects.get(id=id)
        j.delete()
        return JokeMutationDelete(ok=True)
        
class JokeMutations(graphene.ObjectType):
    add_joke = JokeMutationAdd.Field()
    update_joke = JokeMutationUpdate.Field()
    delete_joke = JokeMutationDelete.Field()