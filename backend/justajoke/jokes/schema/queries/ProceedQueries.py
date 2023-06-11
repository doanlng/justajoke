import graphene
from ..types.ProceedType import ProceedType
from ...models import proceed

class ProceedQueries:
    proceed = graphene.Field(ProceedType)
    random_proceeds = graphene.List(
        ProceedType, num_proceeds=graphene.Int(default_value=10))

    def resolve_proceed(self, info):
        return proceed.objects.order_by('?').first()
    def resolve_proceeds(self, info):
        return proceed.objects.all()
    #get 10 random proceeds
    def resolve_random_proceeds(self, info, num_proceeds=10):
        return list(proceed.objects.order_by('?')[:num_proceeds])
