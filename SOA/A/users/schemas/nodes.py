import graphene
from graphene import relay
from graphene_django import DjangoObjectType

# from graphql_relay import from_global_id
# from graphene_file_upload.scalars import Upload
# from graphene_django.filter import DjangoFilterConnectionField
# from graphql_jwt.decorators import login_required, superuser_required, staff_member_required
# from django.db.models import Q

from ..models import User

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['id',]
        exclude = ['password']  # Exclude the password field
        interfaces = (relay.Node,)
    
    
