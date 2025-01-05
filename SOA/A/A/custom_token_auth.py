import graphene
from graphql_jwt.mutations import ObtainJSONWebToken
from graphql_jwt.decorators import login_required
from graphql import GraphQLError

from users.schemas.nodes import UserNode

class CustomObtainJSONWebToken(ObtainJSONWebToken):
    user = graphene.Field(UserNode)
    @classmethod
    def Field(cls, *args, **kwargs):
        return super().Field(*args, **kwargs)

    @classmethod
    @login_required
    def resolve(cls, root, info, **kwargs):
        result = super().resolve(root, info, **kwargs)
        if result:
            user = info.context.user  # Access the authenticated user
            # Here we're setting customField to a string representation of the user
            # You might want to customize this to return specific user information
            result.user = user  # or user.email, user.username, etc.

            # if user.id != 1:  # Check if user's ID is not 1
            #     # Raise a GraphQL error with a specific message
            #     raise GraphQLError("Only user with ID 1 can access this mutation.")
        # print(result)
        return result

