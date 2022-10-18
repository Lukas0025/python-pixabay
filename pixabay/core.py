##
# Pixabay API (unofficial)
# @author Luk� Pleva� <lukas@plevac.eu>
# @date 3.2.2022

import requests
from .params import params
from .query  import query as queryCore
from .image  import image as imageCore
from .video  import video as videoCore

class core:
    ##
    # Init function
    # @param apiKey api key for pixabay API
    # @param host host of api (default: https://pixabay.com/api/)
    # @return core obj
    def __init__(self, apiKey, host='https://pixabay.com/api/'):
        self.apiKey = apiKey
        self.host   = host

    ##
    # Make search qvery on API
    # @param query search words (ex: big tree)
    # @param lang language of search words (default "en") 
    # supported: cs, da, de, en, es, fr, id, it, hu, nl, no, pl, pt, ro, sk, fi, sv, tr, vi, th, bg, ru, el, ja, ko, zh
    # @param orientation orientation of image (default "all")
    # supported: all, horizontal, vertical
    # @param perPage number of images per one request (default: 25)
    # @param order order of images (default: "popular")
    # supported: popular, latest
    # @param safeSearch a flag indicating that only images suitable for all ages should be returned (Default: False)
    # @param minWidth min width of image (default: 0)
    # @param minHeight min height of image (default: 0)
    # @param editorsChoice images that have received an Editor's Choice award (Default: False)
    # @param category filter images by category (default: "all")
    # supported: all, backgrounds, fashion, nature, science, education, feelings, health, people, religion, places, animals, industry, computer, food, sports, transportation, travel, buildings, business, music
    # @param colors filter images by color properties. A comma separated list of values may be used to select multiple properties. (Default: "all")
    # supported: all, grayscale, transparent, red, orange, yellow, green, turquoise, blue, lilac, pink, white, gray, black, brown 
    #
    # @return query object
    def query(self, query='', lang='en', orientation='all', perPage=50, order="popular", safeSearch=False, minWidth=0, minHeight=0, editorsChoice=False, category='all', colors='all'):
        param = params(
            host          = self.host,
            apiKey        = self.apiKey,
            query         = query,
            lang          = lang,
            orientation   = orientation,
            perPage       = perPage,
            order         = order,
            safeSearch    = safeSearch,
            minWidth      = minWidth,
            minHeight     = minHeight,
            editorsChoice = editorsChoice,
            category      = category,
            colors        = colors
        )

        return queryCore(param)

    ##
    # Get image by ID
    # @param iid image id
    # @return image object
    def image(self, iid):
        uri = "{host}?key={api}&id={id}".format(
            host    = self.host,
            id      = iid,
            api     = self.apiKey,
        )

        r = requests.get(uri)

        if (r.status_code != 200):
            raise ValueError('Pixabay return status code != 200 for uri', uri, 'Invalid parameters?')

        return imageCore(r.json()['hits'][0])

##
    # Get video by ID
    # @param iid video id
    # @return video object
    def video(self, iid):
        uri = "{host}videos/?key={api}&id={id}".format(
            host    = self.host,
            id      = iid,
            api     = self.apiKey,
        )

        r = requests.get(uri)

        if (r.status_code != 200):
            raise ValueError('Pixabay return status code != 200 for uri', uri, 'Invalid parameters?')

        return videoCore(r.json()['hits'][0])

    # @return query object
    def queryVideo(self, query='', lang='en', orientation='all', perPage=50, order="popular", safeSearch=False, minWidth=0, minHeight=0, editorsChoice=False, category='all', colors='all'):
        param = params(
            host          = self.host+'videos/',
            apiKey        = self.apiKey,
            query         = query,
            lang          = lang,
            orientation   = orientation,
            perPage       = perPage,
            order         = order,
            safeSearch    = safeSearch,
            minWidth      = minWidth,
            minHeight     = minHeight,
            editorsChoice = editorsChoice,
            category      = category,
            colors        = colors
        )

        return queryCore(param)