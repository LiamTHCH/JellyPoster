import requests, json, os, sys, time
from urllib.parse import urlparse
  

class JellyFin:
    def __init__(self, jellyfin_url ,jellyfin_api_key):
        self.jellyfin_url = jellyfin_url
        self.jellyfin_api_key = jellyfin_api_key

    def get_userid(self,username):
        response = requests.get(f'{self.jellyfin_url}/Users?api_key={self.jellyfin_api_key}')
        print(response.status_code)
        for userid in response.json():
            if userid.get('Name') == username:
                jellyfin_userid= userid.get('Id')
                return(userid)

    def get_PLAYING_device(self,jellyfin_client_ip):
        playing_devices = requests.get(f'{self.jellyfin_url}/Sessions?ActiveWithinSeconds=90&api_key={self.jellyfin_api_key}')
        for playing_device in playing_devices.json():
            #print(playing_device) #Used for Debugging
            if playing_device.get('NowPlayingItem'):

                #Check Remote IP for match with Client IP
                if (playing_device.get('RemoteEndPoint') == jellyfin_client_ip):
                    jellyfin_playback_type = playing_device['NowPlayingItem']['Type']

                    #Episode Display
                    if (jellyfin_playback_type == 'Episode'):
                        print('Client Playing a TV Episode')

                        #Setup Variable
                        jellyfin_episode_name = playing_device['NowPlayingItem']['SeriesName']
                        jellyfin_episode_id = playing_device['NowPlayingItem']['SeriesId']
                        jellyfin_episode_overview = playing_device['NowPlayingItem']['Overview']

                        jellyfin_playback_poster = (f'{self.jellyfin_url}/items/{jellyfin_episode_id}/Images/Primary')

                        

                        return jellyfin_episode_name,jellyfin_episode_overview,jellyfin_playback_poster

                    #Movie Display
                    if (jellyfin_playback_type == 'Movie'):
                        print('Client Playing a Movie')

                        #Setup Variable
                        jellyfin_movie_id = playing_device['NowPlayingItem']['Id']
                        jellyfin_movie_name = playing_device['NowPlayingItem']['Name']
                        jellyfin_movie_overview = playing_device['NowPlayingItem']['Overview']

                        jellyfin_playback_poster = (f'{self.jellyfin_url}/items/{jellyfin_movie_id}/Images/Primary')


                        return jellyfin_movie_name, jellyfin_playback_poster

                    #TV Channel Display
                    if (jellyfin_playback_type == 'TvChannel'):
                        print('Client Playing a Live TV')

                        #Setup Variable
                        jellyfin_channel_id = playing_device['NowPlayingItem']['Id']
                        jellyfin_channel_name = playing_device['NowPlayingItem']['Name']
                        jellyfin_channel_number = playing_device['NowPlayingItem']['ChannelNumber']
                        jellyfin_channel_program_title = playing_device['NowPlayingItem']['CurrentProgram']['EpisodeTitle']

                        jellyfin_playback_poster = (f'{jellyfin_url}/items/{jellyfin_channel_id}/Images/Primary')

                        return jellyfin_channel_name, jellyfin_channel_program_title


