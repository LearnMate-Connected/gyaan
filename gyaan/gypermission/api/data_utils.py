from _gybase.api.data_utils import BaseDataUtils
from gyuser.models.base import Subscription, UserSubscription


SubscriptionDataUtils = BaseDataUtils(Subscription)
UserSubscriptionDataUtils = BaseDataUtils(UserSubscription)