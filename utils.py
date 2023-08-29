

def coloredString(message):
    if ':allowed to' in message:
        ReturnStr = '```diff\n+ {}\n```'.format(message)
    if ':denied to' in message:
        ReturnStr = '```diff\n- {}\n```'.format(message)
    return ReturnStr
