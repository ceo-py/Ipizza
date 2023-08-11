# from django.test import TestCase, RequestFactory
# from django.contrib.auth.models import Group, AnonymousUser
# from django.contrib.auth import get_user_model
# from apps.checkout.views import CartView
#
# User = get_user_model()
#
# class CartViewTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             email='testuser', password='testpassword'
#         )
#         self.group = Group.objects.create(name='hot_kitchen')
#         self.user.groups.add(self.group)
#
#     def test_cart_view_authenticated(self):
#         request = self.factory.get('/cart/')
#         request.user = self.user
#
#         response = CartView.as_view()(request)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Cart Items:')
#         self.assertContains(response, 'Total Items in Cart:')
#         self.assertContains(response, 'Model Name: hot_kitchen')
#
#     def test_cart_view_unauthenticated(self):
#         request = self.factory.get('/cart/')
#         request.user = AnonymousUser()
#
#         response = CartView.as_view()(request)
#
#         self.assertEqual(response.status_code, 404)
#         self.assertRedirects(response, '/login/?next=/cart/')
#
