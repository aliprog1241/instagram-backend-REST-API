from rest_framework.throttling import UserRateThrottle

class CustomThrottle(UserRateThrottle):
    scope = 'custom'


