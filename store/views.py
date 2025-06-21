from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})


from django.contrib.auth.decorators import login_required
from .models import Product, Commande, LigneCommande
from django.shortcuts import redirect

@login_required
def add_to_cart(request, product_id):
    produit = Product.objects.get(id=product_id)
    utilisateur = request.user

    
    commande, created = Commande.objects.get_or_create(utilisateur=utilisateur, complete=False)

    
    ligne, created = LigneCommande.objects.get_or_create(commande=commande, produit=produit)

    
    if not created:
        ligne.quantite += 1
        ligne.save()

    return redirect('cart_detail')  
@login_required
def cart_detail(request):
    utilisateur = request.user
    commande = Commande.objects.filter(utilisateur=utilisateur, complete=False).first()
    items = commande.lignecommande_set.all() if commande else []
    total = sum([item.get_total() for item in items])

    return render(request, 'store/cart.html', {
        'items': items,
        'total': total
    })
from django.views.decorators.http import require_POST

@require_POST
@login_required
def valider_commande(request):
    utilisateur = request.user
    commande = Commande.objects.filter(utilisateur=utilisateur, complete=False).first()

    if commande:
        commande.complete = True
        commande.save()

    return redirect('home')
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

