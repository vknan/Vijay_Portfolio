# from django.contrib.auth.backends import ModelBackend
# from .models import Customer

# class CustomerBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             customer = Customer.objects.get(user__username=username)
#             if customer.user.check_password(password):
#                 return customer.user
#         except Customer.DoesNotExist:
#             pass
