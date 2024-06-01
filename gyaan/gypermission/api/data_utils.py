from _gybase.api.data_utils import BaseDataUtils
from gyuser.models.base import Subscription, UserSubscription


class SubscriptionDataUtils(BaseDataUtils):
    model_class = Subscription


class UserSubscriptionDataUtils(BaseDataUtils):
    model_class = UserSubscription

