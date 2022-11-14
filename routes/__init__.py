from flask import Blueprint
routes = Blueprint('routes', __name__)

from .mypage import *
from .home import *
from .login import *