#
#    Copyright (C) 2015 Team Kodi
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import xbmc
import xbmcaddon
import xbmcvfs

CONTENT_ROOT = 'content://'

__addon__        = xbmcaddon.Addon()
__addonversion__ = __addon__.getAddonInfo('version')
__addonname__    = __addon__.getAddonInfo('name')
__addonpath__    = __addon__.getAddonInfo('path').decode('utf-8')
__addonprofile__ = xbmc.translatePath(__addon__.getAddonInfo('profile')).decode('utf-8')
__icon__         = __addon__.getAddonInfo('icon')

def log(msg):
    print msg

class Main:
    def __init__(self):
        subfolders, files = xbmcvfs.listdir(CONTENT_ROOT)
        print 'Listing %s' % CONTENT_ROOT
        print 'Subfolders: %s' % subfolders
        print 'Files: %s' % files

if (__name__ == '__main__'):
    log('Metadata service %s started' % __addonversion__)
    Main()
