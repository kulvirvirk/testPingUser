

# this program is used to test authentication type required for various user types. 



# this "user_active = True" variable can be used to test both cases (if user is active or disabled - toggle true false values)
user_active = True

# this user_w_ping variable can be used to test both cases (w/ ping and w/o ping - toggle true false values)
user_w_ping = True

# this user_w_ping variable can be used to test both cases (w/ ping and w/o ping - toggle true false values)
user_w_mobile_ping = True

# this user_w_secureVoice variable can be used to test both cases (w/ secureVoice and w/o secureVoice - toggle true false values)
user_w_secureVoice = True


if (user_w_ping == True):
  print("user have ping")
else: print("user doesn't have ping")