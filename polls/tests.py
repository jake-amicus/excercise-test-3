from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase


class TestPolls(GraphQLTestCase):
    
    def test_returns_questions(self):
        poll_response = self.query("""
            {
                questions(n: 10) {
                    questionText
                }
            }
        """)
        self.assertEqual(len(poll_response.json()['data']['questions']), 0)

        