import falcon
from resources import AuthorResource
from resources import BookResource
from resources import CommentResource
from resources import GenreResource
from resources import UserResource

app = falcon.API()

# authors
app.add_route('/authors', AuthorResource())

# books
app.add_route('/books', BookResource())

# comments
app.add_route('/comments', CommentResource())

# genres
app.add_route('/genres', GenreResource())

# users
app.add_route('/users', UserResource())
