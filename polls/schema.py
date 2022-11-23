import graphene
from graphene_django import DjangoObjectType
from polls.models import Question

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question


class DeletePoll(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        return DeletePoll(success=True)

class Query(graphene.ObjectType):  # pylint: disable=no-init
    questions = graphene.List(QuestionType, n=graphene.Int(required=True))

    def resolve_questions(self, info, n=5):
        return Question.objects.all()[:n]

class Mutation(graphene.ObjectType):
    delete_poll = DeletePoll.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
