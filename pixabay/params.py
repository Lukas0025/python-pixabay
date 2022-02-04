##
# Pixabay API (unofficial)
# @author Luká¹ Plevaè <lukas@plevac.eu>
# @date 3.2.2022

class params:
    ##
    # Init params object
    # @param host host of API (default: https://pixabay.com/api/)
    # @param query search words (ex: big tree)
    # @param apiKey api key for API
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
    # @return params object
    def __init__(self, host='https://pixabay.com/api/', query='', apiKey='', lang='en', orientation='all', perPage=25, order="popular", safeSearch=False, minWidth=0, minHeight=0, editorsChoice=False, category='all', colors='all', id=-1):
        self.host          = host
        self.query         = query
        self.apiKey        = apiKey
        self.lang          = lang
        self.orientation   = orientation
        self.perPage       = perPage
        self.order         = order
        self.safeSearch    = 'true' if safeSearch else 'false'
        self.minWidth      = minWidth
        self.minHeight     = minHeight
        self.editorsChoice = 'true' if editorsChoice else 'false'
        self.category      = category
        self.colors        = colors
        self.id            = -1