
class Post(): 
    def __init__(self, image, caption, tags, time, postType, posted = False, deleted = False):
        self.image   = image
        self.caption = caption
        self.tags    = tags
        self.time    = time
        self.type    = postType
        self.posted  = posted
        self.deleted = deleted 