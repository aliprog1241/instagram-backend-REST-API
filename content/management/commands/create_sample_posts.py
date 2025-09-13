from random import choice, sample, randint


from django.contrib.auth.models import User
from django.core.management import BaseCommand


from content.models import PostMedia , Post
from  location.models import Location




SAMPLE_CAPTION = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat 
cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        media_images = PostMedia.objects.all()
        location = Location.objects.all()

        created_posts = list()


        for i in range(200):
            post = Post.objects.create(
                user=choice(users), location=choice(location), caption=choice(SAMPLE_CAPTION)
            )

            post.media.add(*sample(list(media_images), randint(1, len(media_images))))
            created_posts.append(post)


            return f"{len(created_posts)}created."

