from .role  import RoleApi,RolesApi
from .Authentification_entreprise import Signup,Login
from .Authentification_candidat import Signup_candidat,Login_candidat
from .offreemploi import Offre,Offres
from .photos import upload
from .apprentissage import apprentissages

def initialize_routes(api):
    api.add_resource(RoleApi,'/api/Role')
    api.add_resource(RolesApi,'/api/Roles/<id>')

    api.add_resource(Signup,'/api/Signup')
    api.add_resource(Login,'/api/Login')

    api.add_resource(Signup_candidat,'/api/Signupcandidat')
    api.add_resource(Login_candidat,'/api/Logincandidat')

    api.add_resource(Offre,'/api/offre')
    api.add_resource(Offres,'/api/offre/<id>')

    api.add_resource(upload,'/api/upload')
    
    api.add_resource(apprentissages,'/api/apr')