import graphene
from ..types.ProceedType import ProceedType
from ...models import proceed

class ProceedQueries:
    proceed = graphene.Field(ProceedType)
    random_proceeds = graphene.List(
        ProceedType, num_proceeds=graphene.Int(default_value=10))
    number_proceeds = graphene.Int()
    proceed_by_id = graphene.Field(ProceedType, id=graphene.Int(required=True))
    
    def resolve_proceed(self, info):
        return proceed.objects.order_by('?').first()
    def resolve_proceeds(self, info):
        return proceed.objects.all()
    #get 10 random proceeds
    def resolve_random_proceeds(self, info, num_proceeds=10):
        return list(proceed.objects.order_by('?')[:num_proceeds])
    def resolve_number_proceeds(self, info):
        return proceed.objects.count()
    def resolve_proceed_by_id(self, info, id):
        return proceed.objects.get(pk=id)