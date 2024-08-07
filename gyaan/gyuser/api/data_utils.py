from _gybase.api.data_utils import BaseDataUtils

from gyuser.models.base import User, Profile, PublisherApproval


class UserDataUtils(BaseDataUtils):
    model_class = User


class ProfileDataUtils(BaseDataUtils):
    model_class = Profile

    @staticmethod
    def map_profile_object(profile):
        return {"profile_id": profile.id,
                "full_name": profile.full_name,
                "phone": profile.phone}


class ApprovalDataUtils(BaseDataUtils):
    model_class = PublisherApproval

