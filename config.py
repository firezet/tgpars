from os import getenv

shared = getenv("SHARED_FOLDER", 'shared/')

"""
TELEGRAM
"""

api_id = 
api_hash = ''
api_sess_name = 'anon' # anon.session

target_chat_id = -1001525623232 # found messages will be posted here
link_template = "https://t.me/c/{{chat_id}}/{{message_id}}"

ignore_chats = []

joiner = ", "
keywords_file = shared + 'keywords.txt'

"""
WEB
"""

host = '0.0.0.0'
port = 8001
public_url = f"http://{host}:{port}"
