import logging
logging.basicConfig(level=logging.DEBUG)


def before_all(context):
    context.mobile_platform = context.config.userdata.get(
        'mobile_platform', 'ios')
