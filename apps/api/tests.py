from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Issue, Project, Client, Comment


class IssueTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        get_user_model()
        testuser1 = get_user_model().objects.create_user(email='testemail1@email.com',
                                                         password='abc123')
        testuser1.save()
        test_client = Client.objects.create(
            name='Test Client',
            contact='Bill Braski',
            email='billyb@email.com'
        )
        test_client.save()

        test_project = Project.objects.create(
            name='Test Project 1',
            description='Test Project 1 description',
            client=test_client,
            priority=3,
            status=2
        )
        test_project.save()

        test_issue = Issue.objects.create(
            summary='This is the issue summary',
            description='This is the issue description',
            project=test_project,
            status=2,
            priority=1,
            issueType=2,
        )
        test_issue.save()

        test_comment = Comment.objects.create(
            comment='This is a test comment',
            issue=test_issue
        )
        test_comment.save()

    def test_issue_content(self):
        issue = Issue.objects.get(id=1)
        summary = f'{issue.summary}'
        description = f'{issue.description}'
        project = f'{issue.project}'
        status = f'{issue.status}'
        priority = f'{issue.priority}'
        issue_type = f'{issue.issueType}'

        self.assertEqual(summary, 'This is the issue summary')
        self.assertEqual(description, 'This is the issue description')
        self.assertEqual(project, 'Test Project 1')
        self.assertEqual(status, '2')
        self.assertEqual(priority, '1')
        self.assertEqual(issue_type, '2')

    def test_comment_content(self):
        comment1 = Comment.objects.get(id=1)
        comment = f'{comment1.comment}'
        issue = f'{comment1.issue}'

        self.assertEqual(comment, 'This is a test comment')
        self.assertEqual(issue, 'This is the issue summary')
