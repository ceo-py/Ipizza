# from django.test import TestCase
# from django.contrib.auth.models import Group, Permission
# from apps.accounts.models import User
#
#
# class UserModelTest(TestCase):
#     def setUp(self):
#         self.group = Group.objects.create(name='test_group')
#         self.permission = Permission.objects.create(
#             name='Can change user', codename='change_user', content_type=None
#         )
#
#         self.user = User.objects.create_user(
#             email='test@example.com', password='testpassword'
#         )
#         self.user.groups.add(self.group)
#         self.user.user_permissions.add(self.permission)
#
#     def test_user_creation(self):
#         self.assertEqual(self.user.email, 'test@example.com')
#         self.assertTrue(self.user.check_password('testpassword'))
#         self.assertTrue(self.user.is_active)
#         self.assertFalse(self.user.is_staff)
#         self.assertFalse(self.user.is_admin)
#
#     def test_user_permissions(self):
#         self.assertIn(self.group, self.user.groups.all())
#         self.assertIn(self.permission, self.user.user_permissions.all())
#
#
