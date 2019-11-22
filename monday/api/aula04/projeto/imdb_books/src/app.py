import falcon
from resources import AuthorResource
from resources import BookResource
from resources import CommentResource
from resources import GenreResource
from resources import UserResource

app = falcon.API()

# authors
app.add_route('/authors', AuthorResource())
app.add_route('/authors/{id}', AuthorResource(), suffix='author')

# books
app.add_route('/books', BookResource())
app.add_route('/books/{id}', BookResource(), suffix='book')

# comments
app.add_route('/comments', CommentResource())
app.add_route('/comments/{id}', CommentResource(), suffix='comment')

# genres
app.add_route('/genres', GenreResource())
app.add_route('/genres/{id}', GenreResource(), suffix='genre')

# users
app.add_route('/users', UserResource())
app.add_route('/users/{id}', UserResource(), suffix='user')
