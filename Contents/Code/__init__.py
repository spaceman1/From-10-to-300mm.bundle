from PMS import Plugin, Log, DB, Thread, XML, HTTP, JSON, RSS, Utils
from PMS.MediaXML import MediaContainer, DirectoryItem, PhotoItem

PLUGIN_PREFIX   = "/photos/From10to300mm"
RSS_FEED        = "http://from10to300mm.pixyblog.com/feed/entries/atom"

####################################################################################################
def Start():
  Plugin.AddRequestHandler(PLUGIN_PREFIX, HandlePhotosRequest, "From 10 to 300mm", "icon-default.jpg", "art-default.jpg")
  Plugin.AddViewGroup("Pictures", viewMode="Pictures", contentType="photos")

####################################################################################################
def HandlePhotosRequest(pathNouns, count):
  dir = MediaContainer('art-default.jpg', 'Pictures')
  feed = RSS.Parse(RSS_FEED)
  for item in feed.entries:
    node = XML.ElementFromString(item.content[0].value, True)
    summary = ' '.join(node.xpath("//text()")).replace('\n','').strip()
    thumb = node.xpath("//img")[0].get('src')
    src = thumb.replace('gen/500/','')
    dir.AppendItem(PhotoItem(src, item.title, summary, thumb))

  return dir.ToXML()