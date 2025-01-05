import graphene
import graphql_jwt
from users.schemas.nodes import UserNode
from users.schemas.queries import UsersQuery
from users.schemas.mutations import UsersMutation

from .custom_token_auth import CustomObtainJSONWebToken



class AuthMutation(graphene.ObjectType):
    # register = mutations.Register.Field()
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    token_auth = CustomObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()


class Query(
        UsersQuery,
        graphene.ObjectType):
    pass


class Mutation(
    AuthMutation, 
    UsersMutation, 
    graphene.ObjectType):
    pass



# class Subscription(graphene.ObjectType):
#    pass

# schema = graphene.Schema(query=Query, mutation=Mutation,
#                          subscription=Subscription)


schema = graphene.Schema(query=Query, mutation=Mutation)
