##
# Pixabay API (unofficial)
# @author Luká¹ Plevaè <lukas@plevac.eu>
# @date 3.2.2022

import requests

class image:
    ##
    # Init image object
    # @param data data of image in JSON format
    # @return image obj
    def __init__(self, data):
        self._raw_data = data

    ##
    # Get ID of image
    def getId(self):
        return self._raw_data['id']
    
    ##
    # Get page url of image
    def getPageURL(self):
        return self._raw_data['pageURL']

    ##
    # Get type of image
    def getType(self):
        return self._raw_data['type']
    
    ##
    # Get tags of image
    def getTags(self):
        return self._raw_data['tags']

    ##
    # Get url of Preview
    def getPreviewURL(self):
        return self._raw_data['previewURL']

    ##
    # Get width of Preview
    def getPreviewWidth(self):
        return self._raw_data['previewWidth']

    ##
    # Get Height of Preview
    def getPreviewHeight(self):
        return self._raw_data['previewHeight']

    ##
    # Get webformat URL
    def getWebformatURL(self):
        return self._raw_data['webformatURL']

    ##
    # Get width of webformat
    def getWebformatWidth(self):
        return self._raw_data['webformatWidth']

    ##
    # Get height of webformat
    def getWebformatHeight(self):
        return self._raw_data['webformatHeight']

    ##
    # Get large Image URL
    def getLargeImageURL(self):
        return self._raw_data['largeImageURL']

    ##
    # Get width of image
    def getImageWidth(self):
        return self._raw_data['imageWidth']

    ##
    # Get height of image
    def getImageHeight(self):
        return self._raw_data['imageHeight']
    
    ##
    # Get size of image
    def getImageSize(self):
        return self._raw_data['imageSize']
    
    ##
    # Get views of image
    def getViews(self):
        return self._raw_data['views']

    ##
    # Get downloads of image
    def getDownloads(self):
        return self._raw_data['downloads']

    ##
    # Get collections of image
    def getCollections(self):
        return self._raw_data['collections']

    ##
    # Get likes of image
    def getLikes(self):
        return self._raw_data['likes']

    ##
    # Get comments of image
    def getComments(self):
        return self._raw_data['comments']

    ##
    # Get author id of image
    def getUserId(self):
        return self._raw_data['user_id']
    
    ##
    # Get name of author of image
    def getUser(self):
        return self._raw_data['user']

    ##
    # Get url of image of author of image
    def getUserImageURL(self):
        return self._raw_data['userImageURL']

    ##
    # Download image to varaible
    # @param imtype type if image (webformat, preview, largeImage) (Default: webformat)
    # @return byte array of image
    def downloadRaw(self, imtype = 'webformat'):
        
        uri = None

        if (imtype == 'webformat'):
            uri = self.getWebformatURL()
        elif (imtype == 'largeImage'):
            uri = self.getLargeImageURL()
        elif (imtype == 'preview'):
            uri = self.getPreviewURL()
        else:
            raise ValueError('supported types is webformat, largeImage and preview.', imtype, 'unsupported')

        r = requests.get(uri, allow_redirects=True)

        if (r.status_code != 200):
            raise ValueError('Pixabay return status code != 200 for uri', uri, 'Invalid parameters?')

        return r.content

    ##
    # Download image to file
    # @param dst location of file to save
    # @param imtype type if image (webformat, preview, largeImage) (Default: webformat)
    def download(self, dst, imtype = 'webformat'):
        with open(dst, 'wb') as handler:
            handler.write(self.downloadRaw(imtype))
    ##
    # Get published date of image
    # @return datetime UTC of image publication
    def getPublishedDate(self):
        preview_url = self.getPreviewUrl()
        
        #  year / month / day / hour / minute
        match = re.search('\d{4}/\d{2}/\d{2}/\d{2}/\d{2}', preview_url)
        if match:
            parts = match.group().split('/')
            return datetime.datetime(int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), tzinfo=datetime.timezone.utc)
        
        #  year / month / day
        match = re.search('\d{4}/\d{2}/\d{2}', preview_url)
        if match:
            parts = match.group().split('/')
            return datetime.datetime(int(parts[0]), int(parts[1]), int(parts[2]), tzinfo=datetime.timezone.utc)
