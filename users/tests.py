import re
from django.test import TestCase, override_settings
from django.core import mail
from django.core.cache import cache
from rest_framework.test import APIClient

@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class AuthFlow(TestCase):
    def test_flow(self):
        cache.clear(); c=APIClient()
        r=c.post('/users/register/',dict(name='A',surname='B',username='u1',phone_number='1',password='Str0ng!pass_77',email='u1@x.com'),format='json')
        self.assertEqual(r.status_code,201,r.content)
        r=c.post('/users/login/',dict(username='u1',password='Str0ng!pass_77'),format='json')
        link=re.search(r'verify-email/(\S+?)/(\S+?)/',mail.outbox[0].body)
        r=c.get(f'/users/verify/{link[1]}/{link[2]}/'); self.assertEqual(r.status_code,200,r.content)
        r=c.post('/users/login/',dict(username='u1',password='Str0ng!pass_77'),format='json')
        self.assertEqual(r.status_code,200,r.content); self.assertIn('access',r.json())
        # reset
        r=c.post('/users/reset-password/',dict(email='nobody@x.com'),format='json'); self.assertEqual(r.status_code,200)
        self.assertEqual(len(mail.outbox),1)
        r=c.post('/users/reset-password/',dict(email='u1@x.com'),format='json'); self.assertEqual(r.status_code,200)
        m=re.search(r'reset-password/(\S+?)/(\S+?)/',mail.outbox[1].body)
        r=c.post(f'/users/reset-password/{m[1]}/{m[2]}/',dict(password='123'),format='json'); self.assertEqual(r.status_code,400)
        r=c.post(f'/users/reset-password/{m[1]}/{m[2]}/',dict(password='New!pass_9876x'),format='json'); self.assertEqual(r.status_code,200,r.content)
        r=c.post('/users/login/',dict(username='u1',password='New!pass_9876x'),format='json'); self.assertEqual(r.status_code,200)
        r=c.post(f'/users/reset-password/{m[1]}/{m[2]}/',dict(password='Another!pass_5'),format='json'); self.assertEqual(r.status_code,400)  # токен одноразовый
        for u in ['/library/genres/','/library/libraries/']:
            t=c.get(u,HTTP_AUTHORIZATION='Bearer '+c.post('/users/login/',dict(username='u1',password='New!pass_9876x'),format='json').json()['access'])
