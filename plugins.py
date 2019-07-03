import typing
from datetime import datetime

from gilbert.content import Templated, Content

class BlogPost(Templated, Content):
    title: str
    author: str
    posted: typing.Union[None, datetime]
    template: str = "blog/post.html"