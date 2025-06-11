from django.contrib import admin
from .models import Product, Commande, LigneCommande

admin.site.register(Product)
admin.site.register(Commande)
admin.site.register(LigneCommande)
