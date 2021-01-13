from app.ext import login_manager

@login_manager.load_user
def laod_user(user_id):
    return 