PLUGIN_PREFIX   = "/photos/From10to300mm"
RSS_FEED        = "http://from10to300mm.aminus3.com/feed/images/"

####################################################################################################

def Start():
	Plugin.AddPrefixHandler(PLUGIN_PREFIX, HandlePhotosRequest, "From 10 to 300mm", "icon-default.jpg", "art-default.jpg")
	Plugin.AddViewGroup("Pictures", viewMode="Pictures", mediaType="photos")
	MediaContainer.art = R('art-default.jpg')
	MediaContainer.viewGroup = 'Pictures'
	
####################################################################################################

def HandlePhotosRequest():
	dir = MediaContainer()
	feed = RSS.FeedFromURL(RSS_FEED)
	for item in feed.entries:
		title = item.title
		node = HTML.ElementFromString(item.description)
		thumb = node.xpath("//img")[0].get('src')
		#src = thumb.replace('gen/500/','')
		dir.Append(PhotoItem(thumb, title=title, thumb=thumb))

	return dir