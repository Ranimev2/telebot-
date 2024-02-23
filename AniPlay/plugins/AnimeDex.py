import requests
import urllib.parse
from AniPlay.plugins.other import emoji


class AnimeDex:
    def __init__(self) -> None:
        pass

    def search(keyword):
        url = "https://latipharkat-api.my.id/api/otakudesu/search/" + str(
            urllib.parse.quote(keyword)
        )
        data = requests.get(url).json()["results"]
        return data

    def anime(slug):
        data = requests.get("https://kumanimeapi.vercel.app/api/anime/" + slug).json()[
            "results"
        ]
        if data["source"] != "gogoanime":
            return

        title = data["name"]
        text = f"{emoji()} **{title}**\n"
        img = data["image"]

        for i, j in data.items():
            if i not in ["name", "image", "slug", "plot_summary", "source", "episodes"]:
                text += (
                    "\n**" + i.title().strip() + " :** " + j.strip().replace("\n", " ")
                )

        text += "\n**Episodes :** " + str(len(data["episodes"]))

        return img, text, data["episodes"]

    def episode(slug):
        data = requests.get("https://kumanimeapi.vercel.app/api/episode/" + slug).json()[
            "results"
        ]
        text = data["name"]
        surl = [
            ("Stream 1", data["stream"]["sources"][0]["file"]),
            ("Stream 2", data["stream"]["sources_bk"][0]["file"]),
        ]
        murl = data["servers"].items()

        return text, surl, murl

    def download(id):
        data = requests.get("https://api.anime-dex.workers.dev/download/" + id).json()[
            "results"
        ]
        return data
