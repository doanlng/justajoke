import graphene
from ..types.ProceedType import ProceedType
from ...models import proceed
import queue
class ProceedQueries:
    proceed = graphene.Field(ProceedType)
    
    def resolve_proceed(self, info):
        return proceed.objects.get(pk=1)
    def resolve_proceeds(self, info):
        return proceed.objects.all()
    
    #get 10 random proceeds
    def random_proceeds(self, info, num_proceeds=10):
        proceeds_queue = queue.Queue()
        for proceed in proceed.objects.order_by('?')[:num_proceeds]:
            proceeds_queue.put(proceed)

        return proceeds_queue
