import typing
from datetime import datetime

from gilbert.content import Templated, Content

class BlogPost(Templated, Content):
    title: str
    authors: list
    posted: datetime
    modified: typing.Union[None, datetime]
    category: str
    tags: list
    template: str = "blog/post_detail.html"
    summary: str
    draft: bool

class Page(Templated, Content):
    in_menu: bool = True
    call_to_action_text: str

class TeamMember(Templated, Content):
    name: str
    role: str
    location: str
    template: str="team/team_detail.html"
    summary: str
    img: str
    personalURL: typing.Union[None, str]
    socialURL: typing.Union[None, dict]

class Service(Templated, Content):
    name: str
    template: str="service/service_detail.html"
    summary: str