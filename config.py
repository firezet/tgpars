from os import getenv

shared = getenv("SHARED_FOLDER", 'shared/')

"""
TELEGRAM
"""

api_id = 29464630
api_hash = 'a4d41f39d5ac2a2298d84247a1f4ab89'
api_sess_name = 'anon' # anon.session

target_chat_id = -1001525675264 # found messages will be posted here
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