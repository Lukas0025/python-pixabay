##
# Pixabay API (unofficial)
# @author qualityassurance
# @email qualityassurance21@163.com
# @date 2022.9.17

import requests

class video:
    ##
    # Init video object
    # @param data data of video in JSON format
    # @return video obj
    def __init__(self, data):
        self._raw_data = data

    ##
    # Get ID of video
    def getId(self):
        return self._raw_data['id']
    
    ##
    # Get page url of video
    def getPageURL(self):
        return self._raw_data['pageURL']

    ##
    # Get type of video
    def getType(self):
        return self._raw_data['type']
    
    ##
    # Get tags of video
    def getTags(self):
        return self._raw_data['tags']

    ##
    # Get url of Preview
    def getDuration(self):
        return self._raw_data['duration']

    ##
    # Get width of Preview
    def getPictureId(self):
        return self._raw_data['picture_id']

    ##
    # Get Height of Preview
    def getVideoLarge(self):
        return self._raw_data['videos']['large']['url']

    ##
    # Get Height of Preview
    def getVideoSmall(self):
        return self._raw_data['videos']['small']['url']

    ##
    # Get Height of Preview
    def getVideoMedium(self):
        return self._raw_data['videos']['medium']['url']

    ##
    # Get Height of Preview
    def getVideoTiny(self):
        return self._raw_data['videos']['tiny']['url']
    
    ##
    # Get views of video
    def getViews(self):
        return self._raw_data['views']

    ##
    # Get downloads of video
    def getDownloads(self):
        return self._raw_data['downloads']

    ##
    # Get likes of video
    def getLikes(self):
        return self._raw_data['likes']

    ##
    # Get comments of video
    def getComments(self):
        return self._raw_data['comments']

    ##
    # Get author id of video
    def getUserId(self):
        return self._raw_data['user_id']
    
    ##
    # Get name of author of video
    def getUser(self):
        return self._raw_data['user']

    ##
    # Get url of video of author of video
    def getUservideoURL(self):
        return self._raw_data['uservideoURL']

    ##
    # Download video to varaible
    # @param imtype type if video (webformat, preview, largevideo) (Default: webformat)
    # @return byte array of video
    def downloadRaw(self, imtype = 'medium'):
        
        uri = None

        if (imtype == 'large'):
            uri = self.getVideoLarge()
        elif (imtype == 'medium'):
            uri = self.getVideoMedium()
        elif (imtype == 'small'):
            uri = self.getVideoSmall()
        elif (imtype == 'tiny'):
            uri = self.getVideoTiny()
        else:
            raise ValueError('supported types is large, medium, small and tiny.', imtype, 'unsupported')

        r = requests.get(uri, allow_redirects=True)

        if (r.status_code != 200):
            raise ValueError('Pixabay return status code != 200 for uri', uri, 'Invalid parameters?')

        return r.content

    ##
    # Download video to file
    # @param dst location of file to save
    def download(self, dst, imtype = 'medium'):
        with open(dst, 'wb') as handler:
            handler.write(self.downloadRaw(imtype))

        