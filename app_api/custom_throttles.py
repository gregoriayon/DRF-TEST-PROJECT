from rest_framework.throttling import UserRateThrottle

class CustomThrottlingRate(UserRateThrottle):
    scope = 'custom'