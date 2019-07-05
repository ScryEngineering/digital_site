import typing
from datetime import datetime

from gilbert.content import Templated, Content

class BlogPost(Templated, Content):
	title: str
	author: str
	posted: typing.Union[None, datetime]
	modified: typing.Union[None, datetime]
	category: str
	tags: list
	template: str = "blog/post.html"
	summary: str
	draft: bool