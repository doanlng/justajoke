from django.urls import path
from graphene_django.views import GraphQLView
from jokes.schema.schema import schema
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", views.index, name="index"),
    path("graphql",csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
