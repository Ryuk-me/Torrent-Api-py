from torrents.torlock import Torlock
from torrents.zooqle import Zooqle
from torrents.magnet_dl import Magnetdl
from torrents.x1337 import x1337
from torrents.torrent_galaxy import TorrentGalaxy
from torrents.nyaa_si import NyaaSi
from torrents.pirate_bay import PirateBay
from torrents.bitsearch import Bitsearch
from torrents.kickass import Kickass
from torrents.libgen import Libgen
from torrents.yts import Yts
from torrents.limetorrent import Limetorrent
from torrents.torrentfunk import TorrentFunk
from torrents.glodls import Glodls
from torrents.torrentProject import TorrentProject


def check_if_site_available(site):
    all_sites = {
        "1337x": {
            "website": x1337,
            "trending_available": True,
            "trending_category": True,
            "search_by_category": True,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ['anime', 'music', 'games', "tv",
                           "apps", "documentaries", "other", "xxx", "movies"]
        },
        "torlock": {
            "website": Torlock,
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ['anime', 'music', 'games', "tv",
                           "apps", "documentaries", "other", "xxx", "movies", 'books', 'images']  # ebooks
        },
        "zooqle": {
            "website": Zooqle,
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": []
        },
        "magnetdl": {
            "website": Magnetdl,
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            # e-books
            "categories": ['apps', 'movies', 'music', 'games', 'tv', 'books']
        },
        'tgx': {
            "website": TorrentGalaxy,
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ['anime', 'music', 'games', "tv",
                           "apps", "documentaries", "other", "xxx", "movies", 'books']
        },
        'nyaasi': {
            "website": NyaaSi,
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": False,
            "categories": []
        },
        'piratebay': {
            "website": PirateBay,
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ['tv']
        },
        'bitsearch': {
            "website": Bitsearch,
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": []
        },
        'kickass': {
            "website": Kickass,
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ['anime', 'music', 'games', "tv",
                           "apps", "documentaries", "other", "xxx", "movies", 'books']  # television applications
        },
        'libgen': {
            "website": Libgen,
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": []
        },
        'yts': {
            "website": Yts,
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": False,
            "categories": []
        },
        'limetorrent': {
            "website": Limetorrent,
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ['anime', 'music', 'games', "tv",
                           'apps', "other", "movies", 'books']  # applications and tv-shows
        },
        'torrentfunk': {
            "website": TorrentFunk,
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ['anime', 'music', 'games', "tv",
                           'apps', "xxx", "movies", 'books']  # television # software #adult # ebooks
        },
        'glodls': {
            "website": Glodls,
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": False,
            "categories": []
        },
        'torrentproject': {
            "website": TorrentProject,
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": []
        }

    }

    if site in all_sites.keys():
        return all_sites
    return False
