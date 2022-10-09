import random
from django.urls import reverse
from django.contrib.auth.models import User

from core.tests import BaseTestCase
from .models import Post


class BlogTestCase(BaseTestCase):
    def setUp(self) -> None:
        res = super().setUp()

        self.post1 = Post.objects.create(body=f"post body 1", author=self.user1)
        self.post2 = Post.objects.create(body=f"post body 2", author=self.user2)

        return res

    def test_post_list_without_login(self):
        res = self.client.get(reverse("blog:post-list"))
        post_bodylist = list(Post.objects.values_list("body", flat=True))
        for post_body in post_bodylist:
            self.assertContains(res, post_body, html=True)

    def test_post_list_with_login(self):
        self.client.force_login(self.user1)
        res = self.client.get(reverse("blog:post-list"))
        # we assume that user1 NOT follows user2 and then user1 will see only itself and followed user posts
        post_bodylist = list(
            Post.objects.filter(author=self.user1).values_list("body", flat=True)
        )
        for post_body in post_bodylist:
            self.assertContains(res, post_body, html=True)

    def test_post_create(self):
        self.client.force_login(self.user1)
        payload = {
            "body": "post body new",
        }
        res = self.client.post(reverse("blog:post-create"), data=payload)
        self.assertEqual(res.status_code, 302)
        new_post = Post.objects.get(body="post body new")
        self.assertEqual(
            res.url, reverse("blog:post-detail", kwargs={"pk": new_post.pk})
        )
        self.assertEqual(Post.objects.count(), 3)

    def test_post_detail(self):
        res = self.client.get(reverse("blog:post-detail", kwargs={"pk": self.post1.pk}))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.post1.body, html=True)
