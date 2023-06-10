from graphene_django import DjangoObjectType
from ...models import joke


class JokeType(DjangoObjectType):
    class Meta:
        model = joke
        fields = ("id", "name", "punchline", "date_submitted", "verified")