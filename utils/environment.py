""" SITE CONSTANTS GO HERE """

from pages import candtHome as ch,\
    candtWWM as cw,\
    candtTWM as ct


class Pages(object):
    Home = ch.TestCNT
    WWM = cw.TestCNTWWM
    TWM = ct.TestCNTTWM


# ENVIRONMENT
environments = {
    'C&T_PROD': 'https://www.codeandtheory.com/'
}
page_url = environments['C&T_PROD']
force_logout = page_url+'/user/logout'



