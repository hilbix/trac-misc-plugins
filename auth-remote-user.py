from trac.core import *
from trac.config import BoolOption
from trac.web.api import IAuthenticator

class MyRemoteUserAuthenticator(Component):

    implements(IAuthenticator)

    def authenticate(self, req):
#        print('I AM HERE - auth')
        if req.get_header('Remote-User'):
            return req.get_header('Remote-User')
        return None

