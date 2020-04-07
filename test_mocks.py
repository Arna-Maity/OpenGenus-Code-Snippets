import unittest 
from unittest.mock import Mock, patch

import requests

import Mocks

class APITests(unittest.TestCase):

    # Testing if the API endpoint is alive.
    def test_request_response(self):
        response = requests.get('https://api.github.com/user/repos', auth=('Arna-Maity','am2441999'))

        self.assertTrue(response.ok)

    # Testing the actual logic.
    @patch.object('Mocks.github.Github')
    def test_logic(self,mock_git):
        # Setting up the mock
        mock_git.return_value.ok = True
        response = requests.get('https://api.github.com/user/repos', auth=('Arna-Maity','am2441999'))

        self.assertTrue(response.ok)

if __name__=="__main__":
    unittest.main()


