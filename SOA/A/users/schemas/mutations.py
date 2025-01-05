import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType

from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import get_token #, create_refresh_token
from graphql_jwt.refresh_token.shortcuts import refresh_token_lazy
# from users.models import User

from .nodes import UserNode




# Input type for user registration
class RegisterUserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String(required=True)
    first_name = graphene.String()
    last_name = graphene.String()
    date_of_birth = graphene.Date()
    address = graphene.String()
    avatar = graphene.String()

# Mutation for registering a user
class RegisterUserMutation(graphene.Mutation):
    class Arguments:
        input = RegisterUserInput(required=True)
    
    user = graphene.Field(UserNode)
    token = graphene.String()
    refresh_token = graphene.String()

    @staticmethod
    def mutate(root, info, input):
        User = get_user_model()
        # User = User()

        # Check if the username or email already exists
        if User.objects.filter(username=input.username).exists():
            raise GraphQLError("Username already exists.")
        if User.objects.filter(email=input.email).exists():
            raise GraphQLError("Email already exists.")

        # Create the user
        user = User(
            username=input.username,
            email=input.email,
            first_name=input.first_name,
            last_name=input.last_name,
            date_of_birth=input.date_of_birth,
            address=input.address,
        )
        # Set the password
        user.set_password(input.password)

        # Save the user
        user.save()

        token =  get_token(user)
        # refresh_token = create_refresh_token(user)
        refresh_token = refresh_token_lazy(user)
        return RegisterUserMutation(user=user, token=token, refresh_token = refresh_token)

# Add the mutation to the schema
class UsersMutation(graphene.ObjectType):
    register = RegisterUserMutation.Field()

# schema = graphene.Schema(mutation=Mutation)
