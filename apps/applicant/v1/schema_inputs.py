import graphene


class ApplicantInput(graphene.InputObjectType):
    id = graphene.Int(required=False)
    user_id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    location = graphene.String()


class ApplicantUpdateInput(graphene.InputObjectType):
    id = graphene.Int(required=True)
    user_id = graphene.Int(required=False)
    title = graphene.String(required=False)
    description = graphene.String(required=False)
    location = graphene.String(required=False)


class ApplicantDeleteInput(graphene.InputObjectType):
    id = graphene.Int(required=True)
