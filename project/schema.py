import graphene

import project.apps.ingredients.schema as ingredients_schema


class Query(ingredients_schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)