import graphene
from .nodes import UserNode
from graphene_django.filter import DjangoFilterConnectionField

class UsersQuery:
    user = graphene.relay.Node.Field(UserNode)
    users= DjangoFilterConnectionField(UserNode)

