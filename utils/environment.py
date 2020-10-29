""" SITE CONSTANTS GO HERE """

from pages import candtHome as ch,\
    candtWWM as cw,\
    candtTWM as ct,\
    candtSAL as cs,\
    candtAboutUs as ca,\
    candtCareer as cp,\
    candtContact as co,\
    candtSearch as cso


class Pages(object):
    Home = ch.TestCNT
    WWM = cw.TestCNTWWM
    TWM = ct.TestCNTTWM
    SAL = cs.TestCNTSAL
    ABOUT = ca.TestCNTABOUT
    CAREER = cp.TestCNTCAREER
    CONTACT = co.TestCNTCONTACT
    SEARCH = cso.TestCNTSEARCH


# ENVIRONMENT
environments = {
    'C&T_PROD': 'https://www.codeandtheory.com/'
}
page_url = environments['C&T_PROD']
force_logout = page_url+'/user/logout'



