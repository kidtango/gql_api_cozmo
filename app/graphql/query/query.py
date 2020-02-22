from ariadne import ObjectType, QueryType, MutationType, gql, make_executable_schema
import cozmo
from app.cozmo.cozmo_speak import cozmo_speaks
from app.cozmo.random_animation import random_animation
# Map resolver functions to Query fields using QueryType
query = QueryType()

# Resolvers are simple python functions
@query.field("cozmoSpeak")
def resolve_cozmo_speak(*_, input):

    cozmo_speaks(input['sentence'])

    return input['sentence']


@query.field("random_animation")
def resolve_random_animation(*_, input):
    animation_list = random_animation()

    return animation_list
