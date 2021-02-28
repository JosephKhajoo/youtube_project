from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube
# import youtube_dl
import os

# Create your views here.


# def youtube_dl_test(url):
# 	with youtube_dl.YoutubeDL() as ytd:
# 		_url = ytd.extract_info(url, download=False)
# 		download_link = (url["formats"][-1]["url"])
# 		return download_link


def about(request):
	return HttpResponse("about page")


def _get_resolutions(youtube_obj):
	resolutions = []
	streams = youtube_obj.streams.all()
	for i in streams:
		if i.resolution is not None:
			resolutions.append(i.resolution)
	resolutions = list(dict.fromkeys(resolutions))

	return resolutions


def _validate(url: str) -> bool:
	if url.startswith("https://www.youtube.com/"):
		return True
	else:
		return False


def search(request):
	return render(request, "search_download/search.html")


def download(request):
	url = request.GET.get('url')
	# try:
	if _validate(url):
		youtube_object = YouTube(url)
	# except VideoUnavailable:
	# 	return render(request, "search_download/unavailable.html")

		embedded_url = url.replace("watch?v=", "embed/").split("&")[0]
		resolutions = _get_resolutions(youtube_object)

		if request.method == "POST":
			video = youtube_object.streams.first()

			downloaded = video.download()
			# print(downloaded)
			context = {
				"resolutions" : resolutions,
				"embedded_url" : embedded_url
			}
			
		return render(request, "search_download/download.html")
	else:
		results = youtube_search(url)
		return render(request, "search_download/results.html")