## Finding the flag in this challenge is quite tricky

First response from  http://titan.picoctf.net:61532/ will give you Register form However, There is nothing to discuss about that Regester-Form because it pass all user inputs well.

And it redirect you to new directory  http://titan.picoctf.net:61532/dashboard. surprisingly, that entity ask OTP what we do not have. when I intercepted it using Burpsuite the request only take one parameter (otp) so I sent lot of request changing its value I did not get the flag.

TO get the flag, you need to omit the whole parameter (Just wipe it out) then send the request. Boom! you will get the flag

**picoCTF{#0TP_Bypvss_SuCc3$S_c94b61ac}**