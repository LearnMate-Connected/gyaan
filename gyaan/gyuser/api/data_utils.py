from _gybase.api.data_utils import BaseDataUtils

from gyuser.models.base import User, Profile


UserDataUtils = BaseDataUtils(User)
ProfileDataUtils = BaseDataUtils(Profile)
