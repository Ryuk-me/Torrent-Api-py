<h2 align='center'>Torrents Api ✨</h2>
<p align="center">
<a href="https://github.com/Ryuk-me"><img title="Author" src="https://img.shields.io/badge/Author-Ryuk--me-red.svg?style=for-the-badge&logo=github"></a>
</p>

<p align="center">
<a href="https://github.com/Ryuk-me"><img title="Followers" src="https://img.shields.io/github/followers/Ryuk-me?color=teal&style=flat-square"></a>
<a href="https://github.com/Ryuk-me/Torrent-Api-py/stargazers/"><img title="Stars" src="https://img.shields.io/github/stars/ryuk-me/Torrent-Api-py?color=brown&style=flat-square"></a>
<a href="https://github.com/Ryuk-me/Torrent-Api-py/network/members"><img title="Forks" src="https://img.shields.io/github/forks/ryuk-me/Torrent-Api-py?color=lightgrey&style=flat-square"></a>
<a href="https://github.com/Ryuk-me/Torrent-Api-py/issues"><img title="issues" src="https://img.shields.io/github/issues/Ryuk-me/Torrent-Api-py?style=flat-square">
</a>
<img src='https://visitor-badge.glitch.me/badge?page_id=ryuk-me.Torrent-Api-py'>
</p>

<p align="center">
<span style='font-size: 19px'>
An Unofficial API for <span style='font-weight:600;'>1337x</span>, <span style='font-weight:600;'>Piratebay</span>, <span style='font-weight:bold;'>Nyaasi</span>, <span style='font-weight:bold;'>Torlock</span>, <span style='font-weight:bold;'>Torrent Galaxy</span>, <span style='font-weight:600;'>Zooqle</span>, <span style='font-weight:600;'>Kickass</span>, <span style='font-weight:600;'>Bitsearch</span>, <span style='font-weight:600;'>MagnetDL, </span>Libgen, YTS, Limetorrent, TorrentFunk, Glodls, TorrentProject and YourBittorrent
</span>
</p>

## Installation

```sh

# Clone the repo
$ git clone https://github.com/Ryuk-me/Torrent-Api-py

# Go to the repository
$ cd Torrent-Api-py

# Install virtualenv
$ pip install virtualenv

# Create Virtual Env
$ py -3 -m venv api-py

# Activate Virtual Env [Windows]
$ .\api-py\Scripts\activate

# Activate Virtual Env [Linux]
$ source api-py/bin/activate

# Install Dependencies
$ pip install -r requirements.txt

# Start
$ python main.py

# (optional) To Use a PROXY, set the HTTP Proxy environment variable
# You can also use a tor proxy using dperson/torproxy:latest
$ export HTTP_PROXY="http://proxy-host:proxy-port"

# To access API Open any browser/API Testing tool & move to the given URL
$ localhost:8009 

```


---

## Supported Sites

|    Website     |     Keyword      |             Url              | Cloudfare |
| :------------: | :--------------: | :--------------------------: | :-------: |
|     1337x      |     `1337x`      |       https://1337x.to       |     ❌     |
| Torrent Galaxy |      `tgx`       |   https://torrentgalaxy.to   |     ❌     |
|    Torlock     |    `torlock`     |   https://www.torlock.com    |     ❌     |
|   PirateBay    |   `piratebay`    |  https://thepiratebay10.org  |     ❌     |
|     Nyaasi     |     `nyaasi`     |       https://nyaa.si        |     ❌     |
|     Zooqle     |     `zooqle`     |      https://zooqle.com      |     ❌     |
|    KickAss     |    `kickass`     |  https://kickasstorrents.to  |     ❌     |
|   Bitsearch    |   `bitsearch`    |     https://bitsearch.to     |     ❌     |
|    MagnetDL    |    `magnetdl`    |   https://www.magnetdl.com   |     ✅     |
|     Libgen     |     `libgen`     |      https://libgen.is       |     ❌     |
|      YTS       |      `yts`       |        https://yts.mx        |     ❌     |
|  Limetorrent   |  `limetorrent`   | https://www.limetorrents.pro |     ❌     |
|  TorrentFunk   |  `torrentfunk`   | https://www.torrentfunk.com  |     ❌     |
|     Glodls     |     `glodls`     |      https://glodls.to       |     ❌     |
| TorrentProject | `torrentproject` | https://torrentproject2.com  |     ❌     |
| YourBittorrent |      `ybt`       |  https://yourbittorrent.com  |     ❌     |

---

<details open>
<summary style='font-size: 20px'><span style='font-size: 25px;font-weight:bold;'>Supported Methods and categories</span></summary>

> If you want to change the default limit site wise [Visit Here](https://github.com/Ryuk-me/Torrent-Api-py/blob/main/helper/is_site_available.py#L39)

<p>

```json

{
        "1337x": {
            "trending_available": True,
            "trending_category": True,
            "search_by_category": True,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["anime", "music", "games", "tv","apps","documentaries", "other", "xxx", "movies"],
            "limit" : 100
        },
        "torlock": {
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["anime", "music", "games", "tv","apps", "documentaries", "other", "xxx", "movies", "books", "images"],
            "limit" : 50
        },
        "zooqle": {
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": [],
            "limit": 30
        },
        "magnetdl": {
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["apps", "movies", "music", "games", "tv", "books"],
            "limit": 40
        },
        "tgx": {
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["anime", "music", "games", "tv",
                           "apps", "documentaries", "other", "xxx", "movies", "books"],
            "limit": 50
        },
        "nyaasi": {
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": False,
            "categories": [],
            "limit": 50

        },
        "piratebay": {
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["tv"],
            "limit": 50
        },
        "bitsearch": {
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": [],
            "limit": 50
        },
        "kickass": {
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["anime", "music", "games", "tv","apps", "documentaries", "other", "xxx", "movies", "books"],
            "limit": 50
        },
        "libgen'": {
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": [],
            "limit": 25
        },
        "yts": {
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": False,
            "categories": [],
            "limit": 20
        },
        "limetorrent": {
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["anime", "music", "games", "tv",
                           "apps", "other", "movies", "books"],  # applications and tv-shows
            "limit": 50
        },
        "torrentfunk": {
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["anime", "music", "games", "tv",
                           "apps", "xxx", "movies", "books"],  # television # software #adult # ebooks
            "limit": 50
        },
        "glodls": {
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": False,
            "categories": [],
            "limit": 45
        },
        "torrentproject": {
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": [],
            "limit": 20
        },
        "ybt": {
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["anime", "music", "games", "tv",
                           "apps", "xxx", "movies", "books", "pictures", "other"],  # book -> ebooks
            "limit": 20
        }

    }
```

</p>
</details>

---

## API Endpoints

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Supported sites list</span></summary>
<p>

> [`api/v1/sites`](https://torrent-api-py-nx0x.onrender.com/api/v1/sites)

</p>
</details>
<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Site Configs</span></summary>
<p>

> [`api/v1/sites/config`](https://torrent-api-py-nx0x.onrender.com/api/v1/sites/config)

</p>
</details>
<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Search</span></summary>
<p>

> [`api/v1/search`](https://torrent-api-py-nx0x.onrender.com/api/v1/search)

| Parameter | Required |  Type   | Default |                         Example                          |
| :-------: | :------: | :-----: | :-----: | :------------------------------------------------------: |
|   site    |    ✅     | string  |  None   |                `api/v1/search?site=1337x`                |
|   query   |    ✅     | string  |  None   |        `api/v1/search?site=1337x&query=avengers`         |
|   limit   |    ❌     | integer | Default |    `api/v1/search?site=1337x&query=avengers&limit=20`    |
|   page    |    ❌     | integer |    1    | `api/v1/search?site=1337x&query=avengers&limit=0&page=2` |

</p>
</details>
<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Trending</span></summary>
<p>

> `api/v1/trending`

| Parameter | Required |  Type   | Default |                         Example                         |
| :-------: | :------: | :-----: | :-----: | :-----------------------------------------------------: |
|   site    |    ✅     | string  |  None   |              `api/v1/trending?site=1337x`               |
|   limit   |    ❌     | integer | Default |          `api/v1/trending?site=1337x&limit=10`          |
| category  |    ❌     | string  |  None   |    `api/v1/trending?site=1337x&limit=0&category=tv`     |
|   page    |    ❌     | integer |    1    | `api/v1/trending?site=1337x&limit=6&category=tv&page=2` |

</p>
</details>
<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Recent</span></summary>
<p>

> `api/v1/recent`

| Parameter | Required |  Type   | Default |                        Example                         |
| :-------: | :------: | :-----: | :-----: | :----------------------------------------------------: |
|   site    |    ✅     | string  |  None   |               `api/v1/recent?site=1337x`               |
|   limit   |    ❌     | integer | Default |           `api/v1/recent?site=1337x&limit=7`           |
| category  |    ❌     | string  |  None   |     `api/v1/recent?site=1337x&limit=0&category=tv`     |
|   page    |    ❌     | integer |    1    | `api/v1/recent?site=1337x&limit=15&category=tv&page=2` |

</p>
</details>
<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Search By Category</span></summary>
<p>

> `api/v1/category`

| Parameter | Required |  Type   | Default |                                Example                                 |
| :-------: | :------: | :-----: | :-----: | :--------------------------------------------------------------------: |
|   site    |    ✅     | string  |  None   |                      `api/v1/category?site=1337x`                      |
|   query   |    ✅     | string  |  None   |              `api/v1/category?site=1337x&query=avengers`               |
| category  |    ✅     | string  |  None   |      `api/v1/category?site=1337x&query=avengers&category=movies`       |
|   limit   |    ❌     | integer | Default |  `api/v1/category?site=1337x&query=avengers&category=movies&limit=10`  |
|   page    |    ❌     | integer |    1    | `api/v1/category?site=1337x&query=avengers&category=tv&limit=0&page=2` |

</p>
</details>

<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Search from all sites</span></summary>
<p>

> `api/v1/all/search`

| Parameter | Required |  Type   | Default |                  Example                   |
| :-------: | :------: | :-----: | :-----: | :----------------------------------------: |
|   query   |    ✅     | string  |  None   |     `api/v1/all/search?query=avengers`     |
|   limit   |    ❌     | integer | Default | `api/v1/all/search?query=avengers&limit=5` |

<pre>Here <b>limit = 5</b> will get 5 results from each site.</pre>

> [api/v1/all/search?query=avengers](https://torrent-api-py-nx0x.onrender.com/api/v1/all/search?query=avengers)

> [api/v1/all/search?query=avengers&limit=5](https://torrent-api-py-nx0x.onrender.com/api/v1/all/search?query=avengers&limit=5)

</pre>
</details>

<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Get trending from all sites</span></summary>
<p>

> `api/v1/all/trending`

| Parameter | Required |  Type   | Default |            Example            |
| :-------: | :------: | :-----: | :-----: | :---------------------------: |
|   limit   |    ❌     | integer | Default | `api/v1/all/trending?limit=2` |

> [api/v1/all/trending](https://torrent-api-py-nx0x.onrender.com/api/v1/all/trending)

> [api/v1/all/trending?limit=2](https://torrent-api-py-nx0x.onrender.com/api/v1/all/trending?limit=2)

</p>
</details>

<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Get recent from all sites</span></summary>
<p>

> `api/v1/all/recent`

| Parameter | Required |  Type   | Default |           Example           |
| :-------: | :------: | :-----: | :-----: | :-------------------------: |
|   limit   |    ❌     | integer | Default | `api/v1/all/recent?limit=2` |

> [api/v1/all/recent](https://torrent-api-py-nx0x.onrender.com/api/v1/all/recent)

> [api/v1/all/recent?limit=2](https://torrent-api-py-nx0x.onrender.com/api/v1/all/recent)

</p>
</details>

---

## Authentication

To enable authentication, set your API key in the environment variable `PYTORRENTS_API_KEY`. Clients must include this key in the `x-api-key` header of their requests to authenticate successfully.

## Want to Try api ?

> [api/v1/search?site=1337x&query=eternals](https://torrent-api-py-nx0x.onrender.com/api/v1/search?site=1337x&query=eternals)

<details open>
<summary> See response</summary>
<p>

```json
{
  "data": [
    { 
      "name": "Eternals.2021.1080p.WEBRip.1600MB.DD5.1.x264-GalaxyRG",
      "size": "1.6 GB",
      "date": "Jan. 11th '22",
      "seeders": "3674",
      "leechers": "983",
      "url": "https://1337x.to/torrent/5110228/Eternals-2021-1080p-WEBRip-1600MB-DD5-1-x264-GalaxyRG/",
      "uploader": "TGxGoodies",
      "screenshot": [
        "https://everest.picturedent.org/images/2022/01/11/tmpposter23827.jpg",
        "https://everest.picturedent.org/images/2022/01/11/Harone8014.th.jpg",
        "https://everest.picturedent.org/images/2022/01/11/Harone31320.th.jpg",
        "https://everest.picturedent.org/images/2022/01/11/Harone8129XqiKn.th.jpg",
        "https://everest.picturedent.org/images/2022/01/11/Harone27162.th.jpg",
        "https://everest.picturedent.org/images/2022/01/11/Harone1352.th.jpg",
        "https://everest.picturedent.org/images/2022/01/11/Harone14355.th.jpg"
      ],
      "category": "Movies",
      "files": [
        "Eternals.2021.1080p.WEBRip.1600MB.DD5.1.x264-GalaxyRG.mkv (1.6 GB)",
        "[TGx]Downloaded from torrentgalaxy.to .txt (0.7 KB)"
      ],
      "poster": "https://lx1.dyncdn.cc/cdn/02/0251ab7772c031c1130bc92810758cd4.jpg",
      "magnet": "magnet:?xt=urn:btih:20F8D7C2942B143E6E2A0FB5562CDE7EE1B17822&dn=Eternals.2021.1080p.WEBRip.1600MB.DD5.1.x264-GalaxyRG&tr=udp://open.stealth.si:80/announce&tr=udp://tracker.tiny-vps.com:6969/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://tracker.torrent.eu.org:451/announce&tr=udp://explodie.org:6969/announce&tr=udp://tracker.cyberia.is:6969/announce&tr=udp://ipv4.tracker.harry.lu:80/announce&tr=udp://p4p.arenabg.com:1337/announce&tr=udp://tracker.birkenwald.de:6969/announce&tr=udp://tracker.moeking.me:6969/announce&tr=udp://opentor.org:2710/announce&tr=udp://tracker.dler.org:6969/announce&tr=udp://9.rarbg.me:2970/announce&tr=https://tracker.foreverpirates.co:443/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=http://tracker.openbittorrent.com:80/announce&tr=udp://opentracker.i2p.rocks:6969/announce&tr=udp://tracker.internetwarriors.net:1337/announce&tr=udp://tracker.leechers-paradise.org:6969/announce&tr=udp://coppersurfer.tk:6969/announce&tr=udp://tracker.zer0day.to:1337/announce",
      "hash": "20F8D7C2942B143E6E2A0FB5562CDE7EE1B17822"
    }
  ],
  "current_page": 1,
  "total_pages": 7,
  "time": 1.276763677597046,
  "total": 20
}
```

</p>
</details>

---

## Donations

<p> If you feel like showing your appreciation for this project, then how about buying me a coffee?</p>

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/ryukmee)

---

## DEPLOY

<a href="https://render.com/deploy?repo=https://github.com/Ryuk-me/Torrent-Api-py">
<img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render" />
</a>

</br>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
