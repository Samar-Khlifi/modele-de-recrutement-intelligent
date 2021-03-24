class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

#erreurs de catalogue
class CatalogueAlreadyExistsError(Exception):
    pass

class UpdatingCatalogueError(Exception):
    pass

class DeletingCatalogueError(Exception):
    pass

class CatalogueNotExistsError(Exception):
    pass

#erreurs de produit
class ProduitAlreadyExistsError(Exception):
    pass

class UpdatingProduitError(Exception):
    pass

class DeletingProduitError(Exception):
    pass

class ProduitNotExistsError(Exception):
    pass

#erreurs de promotion
class PromotionAlreadyExistsError(Exception):
    pass

class UpdatingPromotionError(Exception):
    pass

class DeletingPromotionError(Exception):
    pass

class PromotionNotExistsError(Exception):
    pass


#erreurs de commande
class CommandeAlreadyExistsError(Exception):
    pass

class UpdatingCommandeError(Exception):
    pass

class DeletingCommandeError(Exception):
    pass

class CommandeNotExistsError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class EmailDoesnotExistsError(Exception):
    pass

class BadTokenError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     #catalogue
     "CatalogueAlreadyExistsError": {
         "message": "Catalogue  already exists",
         "status": 400
     },
     "UpdatingCatalogueError": {
         "message": "Updating catalogue added by other is forbidden",
         "status": 403
     },
     "DeletingCatalogueError": {
         "message": "Deleting catalogue added by other is forbidden",
         "status": 403
     },
     "CatalogueNotExistsError": {
         "message": "Catalogue with given id doesn't exists",
         "status": 400
     },
     #produit
      "ProduitAlreadyExistsError": {
         "message": "Produit already exists",
         "status": 400
     },
     "UpdatingProduitError": {
         "message": "Updating produit added by other is forbidden",
         "status": 403
     },
     "DeletingProduitError": {
         "message": "Deleting produit added by other is forbidden",
         "status": 403
     },
     "ProduitNotExistsError": {
         "message": "Produit with given id doesn't exists",
         "status": 400
     },

     #promotion
      "PromotionAlreadyExistsError": {
         "message": "Promotion  already exists",
         "status": 400
     },
     "UpdatingPromotionError": {
         "message": "Updating promotion added by other is forbidden",
         "status": 403
     },
     "DeletingPromotionError": {
         "message": "Deleting promotion added by other is forbidden",
         "status": 403
     },
     "PromotionNotExistsError": {
         "message": "Promotion with given id doesn't exists",
         "status": 400
     },

    #Commande
      "CommandeAlreadyExistsError": {
         "message": "Commande   already exists",
         "status": 400
     },
     "UpdatingCommandeError": {
         "message": "Updating Commande added by other is forbidden",
         "status": 403
     },
     "DeletingCommandeError": {
         "message": "Deleting commande added by other is forbidden",
         "status": 403
     }, 
     "CommandeNotExistsError": {
         "message": "Commande with given id doesn't exists",
         "status": 400
     },

     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     },

     "EmailDoesnotExistsError": {
         "message": "Couldn't find the user with given email address",
         "status": 400
     },
     "BadTokenError": {
         "message": "Invalid token",
         "status": 403
      }
}