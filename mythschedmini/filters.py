
from app.main import main

@main.app_template_filter()
def mythtvtimedeltaformat(value):
    return str(value).split('.')[0]
