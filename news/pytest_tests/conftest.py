import pytest

from django.test.client import Client

from news.models import News, Comment


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username='Автор')


@pytest.fixture
def not_author(django_user_model):
    return django_user_model.objects.create(username='Не автор')


@pytest.fixture
def author_client(author):
    client = Client()
    client.force_login(author)
    return client


@pytest.fixture
def not_author_client(not_author):
    client = Client()
    client.force_login(not_author)
    return client


@pytest.fixture
def new():
    new = News.objects.create(
        title='Заголовок',
        text='Текст',
    )
    return new


@pytest.fixture
def comment(author):
    new = News.objects.create(
        title='Заголовок',
        text='Текст',
    )
    comment = Comment.objects.create(
        news=new,
        author=author,
        text='Текст комментария'
    )
    return comment


@pytest.fixture
def note_id_for_args(new):
    return (new.id,)


@pytest.fixture
def comment_id_for_args(comment):
    return (comment.id,)
