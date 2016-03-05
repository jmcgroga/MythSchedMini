
from app.main import main

@main.app_template_filter()
def mythtvtimedeltaformat(value):
    return str(value).split('.')[0]

@main.app_template_filter()
def mythtvfulldate(value):
    return value.strftime('%A, %B %d, %Y %I:%M:%S %p')

@main.app_template_filter()
def mythtvdateonly(value):
    return value.strftime('%%B %d, %Y')

@main.app_template_filter()
def mythtvtimeonly(value):
    return value.strftime('%I:%M:%S %p')

@main.app_template_filter()
def mythtvdowonly(value):
    return value.strftime('%A')

