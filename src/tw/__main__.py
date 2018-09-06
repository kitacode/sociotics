from tw.users import TwitterUsers
from tw.store.users import TwitterStoreUsers


def main():
    tw_usr = TwitterUsers()
    tw_st_usr = TwitterStoreUsers()

    profile = tw_usr.get_profile('agnezmo')
    tw_st_usr.update_daily_stat(profile)
