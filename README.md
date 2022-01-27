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
An Unofficial API for <span style='font-weight:600;'>1337x</span>, <span style='font-weight:600;'>Piratebay</span>, <span style='font-weight:bold;'>Nyaasi</span>, <span style='font-weight:bold;'>Torlock</span>, <span style='font-weight:bold;'>Torrent Galaxy</span>, <span style='font-weight:600;'>Zooqle</span>, <span style='font-weight:600;'>Kickass</span>, <span style='font-weight:600;'>Bitsearch</span>, and <span style='font-weight:600;'>MagnetDL</span>
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

# Install  Requirements
$ pip install -r requirements.txt

# Start uvicorn
$ uvicorn main:app --port 8009 or python main.py

```

## Setup Env File

```sh
# Change Environment variables

Go to .env file and add the following

## Get it from https://redistogo.com/
REDIS_URI=redis://redistogo:f99edf3de0cyryty324fe462@sole.redistogo.com:10393/
CACHE_EXPIRATION=180 #set cache expire time in seconds default is 180
PYTHON_ENV=prod (if you are hosting)
PYTHON_ENV=dev (if running local)
```

---

## Supported Sites

|    Website     |   Keyword   |            Url             | Cloudfare |
| :------------: | :---------: | :------------------------: | :-------: |
|     1337x      |   `1337x`   |     https://1337xx.to      |    ❌     |
| Torrent Galaxy |    `tgx`    |  https://torrentgalaxy.to  |    ❌     |
|    Torlock     |  `torlock`  |  https://www.torlock.com   |    ❌     |
|   PirateBay    | `piratebay` | https://thepiratebay10.org |    ❌     |
|     Nyaasi     |  `nyaasi`   |      https://nyaa.si       |    ❌     |
|     Zooqle     |  `zooqle`   |     https://zooqle.com     |    ❌     |
|    KickAss     |  `kickass`  | https://kickasstorrents.to |    ❌     |
|   Bitsearch    | `bitsearch` |    https://bitsearch.to    |    ❌     |
|    MagnetDL    | `magnetdl`  |  https://www.magnetdl.com  |    ✅     |

---

<details open>
<summary style='font-size: 20px'><span style='font-size: 25px;font-weight:bold;'>Supported Methods and categories</span></summary>
<p>

```json

{
        "1337x": {
            "trending_available": True,
            "trending_category": True,
            "search_by_category": True,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["anime", "music", "games", "tv","apps","documentaries", "other", "xxx", "movies"]
        },
        "torlock": {
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["anime", "music", "games", "tv","apps", "documentaries", "other", "xxx", "movies", "books", "images"]
        },
        "zooqle": {
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": []
        },
        "magnetdl": {
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["apps", "movies", "music", "games", "tv", "books"]
        },
        "tgx": {
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["anime", "music", "games", "tv",
                           "apps", "documentaries", "other", "xxx", "movies", "books"]
        },
        "nyaasi": {
            "trending_available": False,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": False,
            "categories": []
        },
        "piratebay": {
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["tv"]
        },
        "bitsearch": {
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": False,
            "recent_category_available": False,
            "categories": []
        },
        "kickass": {
            "trending_available": True,
            "trending_category": True,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["anime", "music", "games", "tv","apps", "documentaries", "other", "xxx", "movies", "books"]
        }

    }
```

</p>
</details>

---

## API Endpoints

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Search</span></summary>
<p>

> `api/v1/search`

| Parameter | Required |  Type   | Default |                     Example                      |
| :-------: | :------: | :-----: | :-----: | :----------------------------------------------: |
|   site    |    ✅    | string  |  None   |            `api/v1/search?site=1337x`            |
|   query   |    ✅    | string  |  None   |    `api/v1/search?site=1337x&query=avengers`     |
|   page    |    ❌    | integer |    1    | `api/v1/search?site=1337x&query=avengers&page=2` |

</p>
</details>
<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Trending</span></summary>
<p>

> `api/v1/trending`

| Parameter | Required |  Type   | Default |                     Example                     |
| :-------: | :------: | :-----: | :-----: | :---------------------------------------------: |
|   site    |    ✅    | string  |  None   |          `api/v1/trending?site=1337x`           |
| category  |    ❌    | string  |  None   |    `api/v1/trending?site=1337x&category=tv`     |
|   page    |    ❌    | integer |    1    | `api/v1/trending?site=1337x&category=tv&page=2` |

</p>
</details>
<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Recent</span></summary>
<p>

> `api/v1/recent`

| Parameter | Required |  Type   | Default |                    Example                    |
| :-------: | :------: | :-----: | :-----: | :-------------------------------------------: |
|   site    |    ✅    | string  |  None   |          `api/v1/recent?site=1337x`           |
| category  |    ❌    | string  |  None   |    `api/v1/recent?site=1337x&category=tv`     |
|   page    |    ❌    | integer |    1    | `api/v1/recent?site=1337x&category=tv&page=2` |

</p>
</details>
<br>

<details open>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Search By Category</span></summary>
<p>

> `api/v1/category`

| Parameter | Required |  Type   | Default |                            Example                             |
| :-------: | :------: | :-----: | :-----: | :------------------------------------------------------------: |
|   site    |    ✅    | string  |  None   |                  `api/v1/category?site=1337x`                  |
|   query   |    ✅    | string  |  None   |          `api/v1/category?site=1337x&query=avengers`           |
| category  |    ✅    | string  |  None   |  `api/v1/category?site=1337x&query=avengers&category=movies`   |
|   page    |    ❌    | integer |    1    | `api/v1/category?site=1337x&query=avengers&category=tv&page=2` |

</p>
</details>

---

## Want to Try api ?

> https://torrent-api-py.ryukme.repl.co/api/v1/search?site=1337x&query=eternals

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
        "https://checkmy.pictures/images/2022/01/11/32162343474810151667.th.jpg",
        "https://checkmy.pictures/images/2022/01/11/38515612831471833686.th.jpg",
        "https://checkmy.pictures/images/2022/01/11/71518482909886223945.th.jpg"
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

---

## Donations

<p> If you feel like showing your appreciation for this project, then how about buying me a coffee.</p>

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/ryukmee)

---

#### You can fork the repo and deploy on VPS or deploy it on Heroku :)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)