import unittest
from bucketlist import Bucketlist

class Buckettest(unittest.TestCase):
    """
       Class performing unit testing for class BucketList
    """
       
    def setUp(self):
        """Defining setUp() method that runs prior to each test."""
        self.buckets = Bucketlist()       
        
    def test_for_creating_a_bucketlist(self):
        """ defining method to test for Creating a bucket list """
        self.buckets.Bucketlists = {}
        output = self.buckets.create('Bucketlist 1', 'Fashion', 'owner@gmail.com')
        self.assertEqual(1, output, "Bucket successfully created")

    def test_if_title_empty(self):
        """defining method to test for adding a bucket list with an empty title """
        output = self.buckets.create('', 'this is my bucketlist by the age of 29', 'owner')
        self.assertEqual(3, output, "please fill all fields")

    def test_if_description_empty(self):
        """defining method to test for adding a bucket list with an empty description"""
        output = self.buckets.create('By 28', '', 'anto@gmail.com')
        self.assertEqual(3, output, "please fill the description")
        
    def tests_if_bucket_exists(self):
        """defining method to test for adding a bucket list That already exists """
        self.buckets.create('By28', 'my dreams by 28', 'anto@gmail.com')
        output = self.buckets.create('By28', 'my goals', 'anto@gmail.com')
        self.assertEqual(2, output, "That bucket already exists!") 

    def tests_delete_bucket(self):
        """defining method to test for deleting a bucketlist"""
        self.buckets.Bucketlists = {}
        self.buckets.create('By28', 'my goals', 'anto@gmail.com')
        output = self.buckets.delete('By28')
        self.assertEqual(1, output, "Succesfully deleted!")

    def tests_delete_an_unavailable_bucketlist(self):
        """defining method to test for deleting a bucketlist That doesnot exist""" 
        self.buckets.Bucketlists = {}
        self.buckets.create('By28', 'my goals', 'anto@gmail.com')
        output = self.buckets.delete('Bucket1')
        self.assertEqual(2, output, "You can not delete a bucket thay does not exist")    

    def tests_edit_bucket(self):
        """defining method to test for editing a bucketlist"""
        self.buckets.Bucketlists = {} 
        self.buckets.create('By28', 'my goals', 'anto@gmail.com')
        output = self.buckets.edit('By28', 'by30', 'vlogger', 'anto@gmail.com')
        self.assertEqual(1, output, "bucket successfully edited")

    def tests_edit_null_title(self):
        """defining method to test for editing a bucketlist and leaving the title null"""
        self.buckets.Bucketlists = {} 
        self.buckets.create('By28', 'my goals', 'anto@gmail.com')
        output = self.buckets.edit('By28', '', 'vlogger', 'anto@gmail.com')
        self.assertEqual(3,output,"Please fill the title field")

    def tests_edit_null_description(self):
        """defining method to test for editing a bucketlist and leaving the Description null"""
        self.buckets.Bucketlists = {}
        self.buckets.create('By28', 'my goals','anto@gmail.com')
        output = self.buckets.edit('By28', 'vlogger', '', 'anto@gmail.com')
        self.assertEqual(2, output, "Please fill the description field")

    def tests_Add_item(self):
        """defining method to test adding an item in a bucketlist"""
        self.buckets.BucketItems = []
        output = self.buckets.createitem('Fashion', 'By20')
        self.assertEqual(1, output, "Item successfully added")

    def tests_addEmpty_item(self):
        """defining method to test adding an empty item in a bucketlist"""
        self.buckets.BucketItems = []
        output = self.buckets.createitem('post', '')
        self.assertEqual(2,output,"Cannot add an empty item ") 

    def tests_delete_null_item(self):
        """defining method to test deleting an item that doesn't exist in a bucketlist"""
        self.buckets.BucketItems = []
        self.buckets.createitem('Fashion', 'By20')
        output = self.buckets.deleteitem('fish')
        self.assertEqual(2, output, "Cannot Delete an item that does not exist") 

    def tests_delete_items(self):
        """defining method to test deleting an  existing item"""
        self.buckets.BucketItems = []
        item = self.buckets.createitem('Fashion', 'By20')
        output = self.buckets.deleteitem(item)
        self.assertEqual(2, output, "Item successfully deleted") 

    def tests_edit_item(self):
        """defining method to test editing an  existing item"""
        self.buckets.BucketItems = []
        self.buckets.createitem('golf', 'By30')
        output = self.buckets.itemedit('by40', 'By30')
        self.assertEqual(1, output, "Item successfully edited")

    def tests_edit_null_item(self):
        """defining method to test editing an empty item field"""
        self.buckets.BucketItems = []
        self.buckets.createitem('golf', 'By30')
        output = self.buckets.itemedit('', 'By30')
        self.assertEqual(2, output, "The item can not be empty")    

if __name__ == "__main__":
    unittest.main()        