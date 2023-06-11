from graphene_django import DjangoObjectType
from ...models import proceed

class ProceedType(DjangoObjectType):
    class Meta:
        model = proceed
        fields = ("text")