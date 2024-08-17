import unittest


from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from news.models import News


# class Test(TestCase):

#     # @classmethod
#     # def setUpClass(cls):
#     #     super().setUpClass()  # Вызов метода setUpClass()
#     #  из родительского класса.
#     # А здесь код, который подготавливает данные
#     # перед выполнением тестов этого класса.

#     def test_example_success(self):
#         self.assertTrue(True)  # Этот тест всегда будет проходить успешно.

#     # @classmethod
#     # def tearDownClass(cls):
#     #     ...  # Выполнение необходимых операций.
#     #     super().tearDownClass()  # Вызов родительского метода.


# class YetAnotherTest(TestCase):

#     def test_example_fails(self):
#         self.assertTrue(False)  # Этот тест всегда будет проваливаться.
User = get_user_model()


class TestNews(TestCase):

    TITLE = 'Заголовок новости'
    TEXT = 'Тестовый текст'

    # В методе класса setUpTestData создаём тестовые объекты.
    # Оборачиваем метод соответствующим декоратором.
    @classmethod
    def setUpTestData(cls):
        # Стандартным методом Django ORM create() создаём объект класса.
        # Присваиваем объект атрибуту класса: назовём его news.
        cls.news = News.objects.create(
            title=cls.TITLE,
            text=cls.TEXT,
        )
        # Создаём пользователя.
        cls.user = User.objects.create(username='testUser')
        # Создаём объект клиента.
        cls.user_client = Client()
        # "Логинимся" в клиенте при помощи метода force_login().
        cls.user_client.force_login(cls.user)
        # Теперь через этот клиент можно отправлять запросы
        # от имени пользователя с логином "testUser".

    @unittest.skip('Этот тест мы просто пропускаем')
    def test_successful_creation(self):
        # При помощи обычного ORM-метода посчитаем количество записей в базе.
        news_count = News.objects.count()
        self.assertEqual(news_count, 1)

    @unittest.skip('Этот тест мы просто пропускаем')
    def test_title(self):
        self.assertEqual(self.news.title, self.TITLE)
