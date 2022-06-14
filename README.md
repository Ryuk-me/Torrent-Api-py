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

---

## Installation

```sh

# Clone the repo
$ git clone https://github.com/Ryuk-me/Torrent-Api-py

# Install Depedencies
$ pip install -r requirements.txt

# Install Redis
> Windows user (use ubuntu terminal)
$ sudo apt-get install redis

# Start redis server
$ redis-server

# Start
$ python main.py

```

## Setup Env File

```sh
# Change Environment variables

Go to .env file / okteto-stack.yaml and add the following

# Get it from https://redistogo.com/
REDIS_URI=redis://redistogo:f99edf3de0cyryty324fe462@sole.redistogo.com:10393/
CACHE_EXPIRATION=180 # set cache expire time in seconds default is 180
PYTHON_ENV=prod (if you are hosting)
PYTHON_ENV=dev (if running local)
```

---

## Supported Sites

|    Website     |     Keyword      |             Url              | Cloudfare |
| :------------: | :--------------: | :--------------------------: | :-------: |
|     1337x      |     `1337x`      |      https://1337xx.to       |    ❌     |
| Torrent Galaxy |      `tgx`       |   https://torrentgalaxy.to   |    ❌     |
|    Torlock     |    `torlock`     |   https://www.torlock.com    |    ❌     |
|   PirateBay    |   `piratebay`    |  https://thepiratebay10.org  |    ❌     |
|     Nyaasi     |     `nyaasi`     |       https://nyaa.si        |    ❌     |
|     Zooqle     |     `zooqle`     |      https://zooqle.com      |    ❌     |
|    KickAss     |    `kickass`     |  https://kickasstorrents.to  |    ❌     |
|   Bitsearch    |   `bitsearch`    |     https://bitsearch.to     |    ❌     |
|    MagnetDL    |    `magnetdl`    |   https://www.magnetdl.com   |    ✅     |
|     Libgen     |     `libgen`     |      https://libgen.is       |    ❌     |
|      YTS       |      `yts`       |        https://yts.mx        |    ❌     |
|  Limetorrent   |  `limetorrent`   | https://www.limetorrents.pro |    ❌     |
|  TorrentFunk   |  `torrentfunk`   | https://www.torrentfunk.com  |    ❌     |
|     Glodls     |     `glodls`     |      https://glodls.to       |    ❌     |
| TorrentProject | `torrentproject` | https://torrentproject2.com  |    ❌     |
| YourBittorrent |      `ybt`       |  https://yourbittorrent.com  |    ❌     |

---

<details open>
<summary style='font-size: 20px'><span style='font-size: 25px;font-weight:bold;'>Supported Methods and categories</span></summary>

> If you want to change the default limit site wise [Visit Here](https://github.com/Ryuk-me/Torrent-Api-py/blob/main/helper/is_site_available.py#L30)

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
            "limit" : 20
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

> `api/v1/sites`

</p>
</details>
<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Search</span></summary>
<p>

> `api/v1/search`

| Parameter | Required |  Type   | Default |                         Example                          |
| :-------: | :------: | :-----: | :-----: | :------------------------------------------------------: |
|   site    |    ✅    | string  |  None   |                `api/v1/search?site=1337x`                |
|   query   |    ✅    | string  |  None   |        `api/v1/search?site=1337x&query=avengers`         |
|   limit   |    ❌    | integer | Default |    `api/v1/search?site=1337x&query=avengers&limit=20`    |
|   page    |    ❌    | integer |    1    | `api/v1/search?site=1337x&query=avengers&limit=0&page=2` |

</p>
</details>
<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Trending</span></summary>
<p>

> `api/v1/trending`

| Parameter | Required |  Type   | Default |                         Example                         |
| :-------: | :------: | :-----: | :-----: | :-----------------------------------------------------: |
|   site    |    ✅    | string  |  None   |              `api/v1/trending?site=1337x`               |
|   limit   |    ❌    | integer | Default |          `api/v1/trending?site=1337x&limit=10`          |
| category  |    ❌    | string  |  None   |    `api/v1/trending?site=1337x&limit=0&category=tv`     |
|   page    |    ❌    | integer |    1    | `api/v1/trending?site=1337x&limit=6&category=tv&page=2` |

</p>
</details>
<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Recent</span></summary>
<p>

> `api/v1/recent`

| Parameter | Required |  Type   | Default |                        Example                         |
| :-------: | :------: | :-----: | :-----: | :----------------------------------------------------: |
|   site    |    ✅    | string  |  None   |               `api/v1/recent?site=1337x`               |
|   limit   |    ❌    | integer | Default |           `api/v1/recent?site=1337x&limit=7`           |
| category  |    ❌    | string  |  None   |     `api/v1/recent?site=1337x&limit=0&category=tv`     |
|   page    |    ❌    | integer |    1    | `api/v1/recent?site=1337x&limit=15&category=tv&page=2` |

</p>
</details>
<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Search By Category</span></summary>
<p>

> `api/v1/category`

| Parameter | Required |  Type   | Default |                                Example                                 |
| :-------: | :------: | :-----: | :-----: | :--------------------------------------------------------------------: |
|   site    |    ✅    | string  |  None   |                      `api/v1/category?site=1337x`                      |
|   query   |    ✅    | string  |  None   |              `api/v1/category?site=1337x&query=avengers`               |
| category  |    ✅    | string  |  None   |      `api/v1/category?site=1337x&query=avengers&category=movies`       |
|   limit   |    ❌    | integer | Default |  `api/v1/category?site=1337x&query=avengers&category=movies&limit=10`  |
|   page    |    ❌    | integer |    1    | `api/v1/category?site=1337x&query=avengers&category=tv&limit=0&page=2` |

</p>
</details>

<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Search from all sites</span></summary>
<p>

> `api/v1/all/search`

| Parameter | Required |  Type   | Default |                  Example                   |
| :-------: | :------: | :-----: | :-----: | :----------------------------------------: |
|   query   |    ✅    | string  |  None   |     `api/v1/all/search?query=avengers`     |
|   limit   |    ❌    | integer | Default | `api/v1/all/search?query=avengers&limit=5` |

<pre>Here <b>limit = 5</b> will get 5 results from each site.</pre>

> https://torrents-api-py3.herokuapp.com/api/v1/all/search?query=avengers

> https://torrents-api-py3.herokuapp.com/api/v1/all/search?query=avengers&limit=5

</pre>
</details>

<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Get trending from all sites</span></summary>
<p>

> `api/v1/all/trending`

| Parameter | Required |  Type   | Default |            Example            |
| :-------: | :------: | :-----: | :-----: | :---------------------------: |
|   limit   |    ❌    | integer | Default | `api/v1/all/trending?limit=2` |

> https://torrents-api-py3.herokuapp.com/api/v1/all/trending

> https://torrents-api-py3.herokuapp.com/api/v1/all/trending?limit=2

</p>
</details>

<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Get recent from all sites</span></summary>
<p>

> `api/v1/all/recent`

| Parameter | Required |  Type   | Default |           Example           |
| :-------: | :------: | :-----: | :-----: | :-------------------------: |
|   limit   |    ❌    | integer | Default | `api/v1/all/recent?limit=2` |

> https://torrents-api-py3.herokuapp.com/api/v1/all/recent

> https://torrents-api-py3.herokuapp.com/api/v1/all/recent?limit=2

</p>
</details>

---

## Want to Try api ?

> https://torrents-api-py3.herokuapp.com/api/v1/search?site=1337x&query=eternals

<details open>
<summary> See response</summary>
<p>

```json
{
  "data": [
    {
      "name": "Eternals.2021.1080p.WEBRip.DDP5.1.x264-NOGRP",
      "size": "5.6 GB",
      "date": "Jan. 11th '22",
      "seeders": "10872",
      "leechers": "6820",
      "url": "https://1337xx.to/torrent/5110260/Eternals-2021-1080p-WEBRip-DDP5-1-x264-NOGRP/",
      "uploader": "TheMorozko",
      "screenshot": [
        "https://checkmy.pictures/images/2022/01/11/32162343474810151667.jpg",
        "https://checkmy.pictures/images/2022/01/11/38515612831471833686.jpg",
        "https://checkmy.pictures/images/2022/01/11/71518482909886223945.jpg"
      ],
      "category": "Movies",
      "poster": "https://1337xx.to/img/movie/Eternals-2021.jpg",
      "magnet": "magnet:?xt=urn:btih:A2AD2A669250A014BED19919E6C386DD4F82A883&dn=Eternals.2021.1080p.WEBRip.DDP5.1.x264-NOGRP&tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2950%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2870%2Fannounce&tr=udp%3A%2F%2Ftracker.tallpenguin.org%3A15720%2Fannounce&tr=udp%3A%2F%2Ftracker.thinelephant.org%3A12780%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce",
      "hash": "A2AD2A669250A014BED19919E6C386DD4F82A883"
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

# How to Host On Repl.it

```sh
> Fork this repo
> Import repo from github in repl
> Command : python main.py
> Install Requirements manually !very important
> Add Environment variables from .env file in repl
> And Run Your repl

Note :  Due to CPU limitations Repl will take much more time than Heroku and everytime you pull new changes to repl you have to add REDIS_URI

Test Here : https://Torrent-Api-py.ryukme.repl.co/api/v1/search?site=tgx&query=avengers&limit=5
```

---

# How to Host On Okteto

```sh
> Fork this repo
> Go to  okteto-stack.yaml file and add REDIS_URI in environment
> Now visit https://www.okteto.com/ and login via Github
> Now select the repository u want to deploy and and just click on deploy don't add any environment variable there
> Now wait for some time and your api will be live

```

## Donations

<p> If you feel like showing your appreciation for this project, then how about buying me a coffee.</p>

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/ryukmee)

---

#### You can fork the repo and deploy on VPS or deploy it on Heroku :)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
