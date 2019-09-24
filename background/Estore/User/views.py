from User import user

@user.route("/test")
def user_index():
    return "hello user"
