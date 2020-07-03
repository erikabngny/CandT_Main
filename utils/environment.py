""" SITE CONSTANTS GO HERE """

from pages import candtHome as ch#, \
   # samplePage as smp, \


class Pages(object):
    Home = ch.TestCNT
  #  SamplePage = smp.SamplePage

# ENVIRONMENT
environments = {
    'C&T_PROD': 'https://www.codeandtheory.com/'
}
page_url = environments['C&T_PROD']
force_logout = page_url+'/user/logout'



