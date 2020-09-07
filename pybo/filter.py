from datetime import datetime as dt
today = dt.now().date()
def format_datetime(value, fmt='%Y년 %m월 %d일 %H:%M'):
    date =     today.strftime(
        '%Y년 %m월 %d일'.encode('unicode-escape').decode()
    ).encode().decode('unicode-escape')
    return date
