import instaloader
L = instaloader.Instaloader()
profile_name = input("Enter your username: ")
L.download_profile(profile_name, profile_pic_only=True)