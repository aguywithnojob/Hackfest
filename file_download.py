def downloadImage(self):
    request = urllib2.Request(self.url)
    pic = urllib2.urlopen(request)
    print "downloading: " + self.url
    print self.fileName
    filePath = localSaveRoot + self.catalog  + self.fileName + Picture.postfix
    # urllib.urlretrieve(self.url, filePath)
    with open(filePath, 'wb') as localFile:
        localFile.write(pic.read())
