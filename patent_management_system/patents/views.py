from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PatentRegistrationForm
from .models import Patent
from .blockchain import register_patent, get_patent_details
import hashlib

# Create your views here.


def patent_register(request):
    if request.method == 'POST':
        form = PatentRegistrationForm(request.POST, request.FILES) # Add request.FILES
        if form.is_valid():
            patent = form.save(commit=False)
            patent.owner = request.user
            patent.save()
            return redirect('patent_list')
    else:
        form = PatentRegistrationForm()
    return render(request, 'patents/patent_register.html', {'form': form})

def patent_list(request):
    patents = Patent.objects.all()
    return render(request, 'patents/patent_list.html', {'patents': patents})

def user_patents(request):
    patents = Patent.objects.filter(owner=request.user)
    return render(request, 'patents/user_patents.html', {'patents': patents})


@login_required
def patent_register(request):
    if request.method == 'POST':
        form = PatentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            patent = form.save(commit=False)
            patent.owner = request.user

            # Calculate document hash (SHA256)
            document = request.FILES['document']
            document_hash = hashlib.sha256(document.read()).hexdigest()

            # Save document to the database (without storing file itself)
            patent.document_url = document_hash
            patent.save()

            # Get user's Ethereum address and private key
            user_address = request.user.profile.ethereum_address
            private_key = request.user.profile.private_key

            # Register patent on the blockchain
            try:
                tx_hash = register_patent(patent.title, patent.description, document_hash, user_address, private_key)
                messages.success(request, f'Patent registered successfully on the blockchain. Tx Hash: {tx_hash}')
            except Exception as e:
                messages.error(request, f'Error registering patent on the blockchain: {e}')

            return redirect('user_patents')
    else:
        form = PatentRegistrationForm()
    return render(request, 'patents/patent_register.html', {'form': form})

@login_required
def patent_list(request):
    patents = Patent.objects.all()
    for patent in patents:
        patent.details = get_patent_details(patent.id)
    return render(request, 'patents/patent_list.html', {'patents': patents})

@login_required
def user_patents(request):
    patents = Patent.objects.filter(owner=request.user)
    for patent in patents:
        patent.details = get_patent_details(patent.id)
    return render(request, 'patents/user_patents.html', {'patents': patents})