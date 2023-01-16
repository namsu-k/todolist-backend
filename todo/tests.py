from rest_framework.test import APITestCase
from . import models
from users.models import User

"""
1. class 생성하기
- APITestCase 상속받아야함
2. test function 작성하기
- 모든 테스트 펑션 이름은 test_ 를 앞에 작성해주어야함
- 테스트는 기존 데이터베이스를 사욯하지 않기 때문에 
아무것도 저장되어있지 않은 상태로 시작된다
- 또한 테스트가 진행된 후 모든 데이터가 롤백되기 때문에 
다른 테스트를 진행하려면 다시 데이터를 생성해야한다
- 테스트를 하기 전에 def setUp(self): 를 정의해놓고 데이터를 추가할 수 있다
- 시스템적으로 리퀘스트를 할 수 있는 기능은 self.client.get post put delete 등이 있다

"""


class TestTodo(APITestCase):

    URL = "/api/v1/todo/"
    TITLE = "test title"

    def setUp(self):
        user = User.objects.create(username="test")
        user.set_password("123")
        user.save()
        self.user = user
        models.Todo.objects.create(title=self.TITLE, user=user)

    def test_get_todos(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 200, "status code is not 200")
        self.assertIsInstance(data, list, "data is not list")
        self.assertIn("pk", data[0], "pk is not contain todo")
        self.assertIn("title", data[0], "title is not contain todo")
        self.assertIn("done", data[0], "done is not contain todo")
        self.assertIn("deadline", data[0], "deadline is not contain todo")
        self.assertIn("is_owner", data[0], "is_owner is not contain todo")

        self.assertFalse(data[0]["is_owner"], "is_owner is not False")

        self.client.force_login(user=self.user)
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 200, "status code is not 200")
        self.assertIsInstance(data, list, "data is not list")
        self.assertIn("pk", data[0], "pk is not contain todo")
        self.assertIn("title", data[0], "title is not contain todo")
        self.assertIn("done", data[0], "done is not contain todo")
        self.assertIn("deadline", data[0], "deadline is not contain todo")
        self.assertIn("is_owner", data[0], "is_owner is not contain todo")

        self.assertTrue(data[0]["is_owner"], "is_owner is not True")
