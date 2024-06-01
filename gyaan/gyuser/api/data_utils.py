from _gybase.api.data_utils import BaseDataUtils

from gyuser.models.base import User, Profile, PublisherApproval


class UserDataUtils(BaseDataUtils):
    model_class = User
    pass


class ProfileDataUtils(BaseDataUtils):
    model_class = Profile


class ApprovalDataUtils(BaseDataUtils):
    model_class = PublisherApproval

