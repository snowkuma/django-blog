# django-blog
A little blog project to learn more about Django. Based on the 'Django 2 by example' book.


# Added a tagging module to the blog

Utilising a third party tagging application [django-taggit](https://github.com/alex/django-taggit)
Installed via pip

# Added filter by tag.

# Retrieve posts by similarity.

By adding a count we can find similar posts based onThe number of tags they share.

1. Retrieve all tags for current post
2. Get all posts that are tagged with any of those tags
3. Exclude the current post from that list to avoid recommending same post
4. OrderThe results byThe number of tags shared with the current post
5. In a case where there is a tie, recommend the most recent post
6. Limit the query to the number of posts we want to recommend
