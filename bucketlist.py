BucketItems = []
"""an empty list to store my items"""

class Bucketlist(object):
    Bucketlists = {}
    """an empty list to store my buckets"""
    def __init__(self, post=None, description=None, owner=None):
        """initializing class instance variables"""
        self.post = post
        self.description = description
        self.owner = owner

    def create(self, post, description, owner):
        """defining method to create bucket list"""
        if description != ''and post != '':
            #call the get_mybucket_lists function that contains individual user buckets 
            my_buckets = self.get_mybucket_lists(owner)
            if my_buckets != {}:
                #check's if user already has a bucket
                if post not in my_buckets.keys():
                    self.Bucketlists[post] = {
                    'description':description,
                    'post':post,
                    'owner':owner,
                    }
                    return 1
                else:
                    return 2
            else:
                #user's first bucket
                self.Bucketlists[post] = {
                'description':description,
                'post':post,
                'owner':owner,
                }
                return 1
        else:
            return 3

    def delete(self, post):
        """defining method to delete bucket list"""
        if post in self.Bucketlists.keys():
            #checks if the post being deleted exists
            del self.Bucketlists[post]
            return 1
        else:
            return 2

    def edit(self, old, post, description, owner):
        """defining method to delete bucket list"""
        if  post != '':
            if description != '':
                del self.Bucketlists[old]
                self.Bucketlists[post] = {
                'description' : description,
                'post' : post,
                'owner' : owner,
                }
                return 1
            else:
                return 2
        else:
            return 3

    def get_bucket_lists(self):
        """defining method to get all bucket lists"""
        return self.Bucketlists

    def get_mybucket_lists(self, owner):
        """defining method to get one user's bucket lists"""
        data = self.Bucketlists
        my_buckets = {}
        for post in data.keys():
            #loop through the posts in the bucketlist and assign the dictionary to variables
            bucket = data[post]
            description = bucket['description']
            bucketowner = bucket['owner']
            if bucketowner == owner:
                my_buckets[post] = {
                'description': description,
                'post': post,
                'owner': owner,
                }
            else:
                result = my_buckets
        return my_buckets

    def get_bucket_list(self, post):
        """defining method to get one bucket lists"""
        return self.Bucketlists[post]

    def createitem(self, post, item):
        """defining method to create an item in a bucket"""
        if item != '':
            items = {}
            items['item'] = item 
            items['post'] = post
            BucketItems.append(items)
            return 1
        else: 
            return 2	

    def itemedit(self, item, old):
        """defining method to create an item in a bucket"""
        if item != "":
            for dic in range(len(BucketItems)):
                if BucketItems[dic]['item'] == old:
                    del BucketItems[dic]['item']
                    BucketItems[dic]['item'] = item
                    return 1
        else:
            return 2

    def getitems(self):
        """ defining method to delete an item from bucket"""
        return BucketItems

    def deleteitem(self,item):
        """ defining method to delete an item from bucket"""
        for dic in range(len(BucketItems)):
            if BucketItems[dic]['item'] == item:
                del BucketItems[dic]
                result = 1
            else:
                result = 2

        return result   
