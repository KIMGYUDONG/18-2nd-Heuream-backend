import jwt
import json
import bcrypt
from unittest.mock import patch, MagicMock

from django.test  import TestCase, Client
from django.http  import JsonResponse

from account.models import User
from my_settings    import SECRET_KEY, ALGORITHM

class KakaoSignUpTest(TestCase):
    @patch('account.views.requests')
    def test_kakao_signup(self, mocked_request):
        client = Client()
        class MockResponse:
            def json(self):
                return {
                    'id':1,
                    'kakao_account':{
                        'email':'test_email@kakao.com'
                    }
                }
        
        mocked_request.get = MagicMock(return_value = MockResponse())
        headers = {'HTTP_Authorization':'kakao_token'}
        access_token = jwt.encode({'user_id':2}, SECRET_KEY, ALGORITHM)
        response = client.post('/account/kakaosignin', content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message':'SUCCESS', 'access_token':access_token})

class KakaoSignInTest(TestCase):
    def setUp(self):
        User.objects.create(email='gyudong1594@wecode.com', password='12345678')
    
    def tearDown(self):
        User.objects.all().delete()

    @patch('account.views.requests')
    def test_kakao_signin(self, mocked_request):
        client = Client()
        class MockResponse:
            def json(self):
                return {
                    'id':1,
                    'kakao_account':{
                        'email':'gyudong1594@wecode.com'
                    }
                }
        
        mocked_request.get = MagicMock(return_value = MockResponse())
        headers = {'HTTP_Authorization':'kakao_token'}
        access_token = jwt.encode({'user_id':1}, SECRET_KEY, ALGORITHM)
        response = client.post('/account/kakaosignin', content_type='application/json', **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message':'SUCCESS', 'access_token':access_token})
