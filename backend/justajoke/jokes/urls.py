from django.urls import path
from graphene_django.views import GraphQLView
from jokes.schema.schema import schema
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]
