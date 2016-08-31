#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus,sys

session_bus = dbus.SessionBus()
wait = 10
max_artist_len = 25
max_title_len = 25

def run():
    try:
        obj = session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
        properties_manager = dbus.Interface(obj, 'org.freedesktop.DBus.Properties')
        metadata = properties_manager.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
        playback = properties_manager.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus')
        artist = metadata.get('xesam:artist')
        artist = artist[0]
        title = metadata.get('xesam:title')
        if len(artist) > max_artist_len:
            artist = artist[:max_artist_len].strip()+u"\u2026"
        if len(title) > max_title_len:
            title = title[:max_title_len].strip()+u"\u2026"

        if str(playback) == "Playing":
            playback = u'\u25B6 '
        else:
            playback = ''
        sys.stderr.write(u'%s%s - %s' % (playback, artist, title))
        #return {
        #    'full_text': u'%s%s - %s' % (playback, artist, title),
        #    'color': 'white',
        #    'name': 'music'
        #}
    except Exception:
        return None
run()
