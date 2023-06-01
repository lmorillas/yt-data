""" Pull All Youtube Videos from a Playlist """

from apiclient.discovery import build
from apiclient.errors import HttpError
import json
from descarga_videos import *
from crea_ex_json import *
from dotenv import load_dotenv

RUTA = 'docs/static/'
RUTAINDEX = 'docs/acornago/index.html'
        

load_dotenv()

API_KEY = os.getenv('API_KEY')

description = "Comparto estrategias y materiales para que, desde la comprensión y el respeto al autismo, nuestros hijos avancen sintiéndose orgullosos de sí mismos, valorados, regulados y cada vez más autosuficientes. "
title = "Autismo con Naturalidad"
schema = json.load(open('schema.json'))

yt = connect_youtube(API_KEY)

usuario = "AnabelCornago"
# channelId = "UC5ulFfNeWSJuzeKJFY-hUvQ"
channelId = get_channel_id_from_username(yt, usuario)

playlists = get_playlists(yt, channelId)

#videos = fetch_all_youtube_videos(yt, "PLybE0q7GFyrbQSrWNgci8QJ60gQjQKLlH")
videos  = todos_los_videos_playlist(yt, playlists)
#videos2 = todos_los_videos_2(yt, channelId)

json.dump(playlists, open('playlists_acornago_yt.json', 'w'))
json.dump(videos, open('videos_acornago_yt.json', 'w'))
#crea_videos_exhibit('videos_acornago_yt.json', RUTA + 'videos_acornago.json')
#crea_playlist_exhibit('playlists_acornago_yt.json', RUTA + 'playlists_acornago.json')
videosex = crea_videos_exhibit('videos_acornago_yt.json' )
playlistex = crea_playlist_exhibit('playlists_acornago_yt.json')

crea_index(ruta = RUTAINDEX, schema = schema, data = {"items": videosex + playlistex},
    title = title, description = description, playlist=True)







    