from _gybase.api.data_utils import BaseDataUtils

from gyuser.models.base import User, Profile, PublisherApproval


# class UserDataUtils(BaseDataUtils):
#     pass

UserDataUtils = BaseDataUtils(User)
ProfileDataUtils = BaseDataUtils(Profile)
ApprovalDataUtils = BaseDataUtils(PublisherApproval)