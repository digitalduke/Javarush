def action(message_action: MessageAction):
    def decorator_action(func):
        if message_action in MAP_ACTION_TO_METHOD:
            logger.debug('Нельзя просто так взять и зарегистрировать '
                         'два обработчика на одно действие!')
            return
        MAP_ACTION_TO_METHOD[message_action] = func
        @functools.wraps(func)
        def wrapper_action(*args, **kwargs):
            value = func(*args, **kwargs)
            return value
        return wrapper_action
    return decorator_action
