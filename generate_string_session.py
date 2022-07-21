from pyrogram import Client

print('Required pyrogram V2 or greater.')
API_KEY = int(input("15481415"))
API_HASH = input("b603d6056effe5a54130424ebc121eff")
with Client(name='USS', api_id=API_KEY, api_hash=API_HASH, in_memory=True) as app:
    print(app.export_session_string())
