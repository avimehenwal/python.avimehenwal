class StandardTestsMixin(object):
    def setUp(self):
        """
        Download a valid test URL.
        """
        self.storage_file, self.web_file = download_avatar(self.TEST_URL)
 
    def tearDown(self):
        """
        Remove image from disk.
        """
        os.remove(self.storage_file)
 
    def test_download_avatar_A(self):
        """
        Confirm that the image was downloaded correctly.
        """
        self.assertIsNotNone(self.storage_file)
        self.assertTrue(os.path.exists(self.storage_file))
 
    def test_download_avatar_B(self):
        """
        Confirm that the image is a JPEG and was scaled properly.
        """
        I = Image.open(self.storage_file)
 
        self.assertEqual(I.format, 'JPEG')
        self.assertEqual(I.mode,   'RGB')
        self.assertEqual(I.size,   (256, 256))
        self.assertIsNone(I.palette)
 
    def test_download_avatar_C(self):
        """
        Accessing image via BASE_HREF + web_file works correctly.
        """
        TX_AVATAR_URL = BASE_HREF + self.web_file
 
        r = requests.get(TX_AVATAR_URL)
 
        self.assertTrue(r.ok)
 
        # Compare the byte-sizes of what was just retrieved
        # with the what is on the local disk.
        #
        # They must be equal, or something went wrong.
        image_local  = open(self.storage_file, 'rb').read()
        image_gotten = r.content
 
        self.assertEqual(image_local, image_gotten)

 
class GoodAvatar(StandardTestsMixin, unittest.TestCase):
    TEST_URL = 'https://www.tandemexchange.com/static/images/unittest/DSC02879.JPG'
 
class JpgPaletteAvatar(StandardTestsMixin, unittest.TestCase):
    TEST_URL = 'https://www.tandemexchange.com/static/images/unittest/palette.jpg'
 
class AnimatedGifAvatar(StandardTestsMixin, unittest.TestCase):
    TEST_URL = 'https://www.tandemexchange.com/static/images/unittest/animated.gif'
