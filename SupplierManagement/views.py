from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Supplier


def add_supplier(request):
    suppliers = Supplier.objects.all()
    edit_supplier = None
    clear_form = False  # Flag to clear the form

    if 'supplier_id' in request.GET:
        # Fetch the supplier to edit
        supplier_id = request.GET.get('supplier_id')
        edit_supplier = Supplier.objects.get(pk=supplier_id)


    if request.method == 'POST':
        supplier_id = request.POST.get('supplier_id')
        supplier_code = request.POST.get('supplier_code')
        supplier_name = request.POST.get('supplier_name')
        supplier_address = request.POST.get('supplier_address')
        supplier_city = request.POST.get('supplier_city')
        supplier_country = request.POST.get('supplier_country')
        supplier_postalCode = request.POST.get('supplier_postalCode')

        if supplier_id:  # Update existing supplier
            supplier = Supplier.objects.get(pk=supplier_id)
            supplier.supplier_code = supplier_code
            supplier.supplier_name = supplier_name
            supplier.supplier_address = supplier_address
            supplier.supplier_city = supplier_city
            supplier.supplier_country = supplier_country
            supplier.supplier_postalCode = supplier_postalCode

            if Supplier.objects.filter(supplier_code=supplier_code).exclude(pk=supplier_id).exists():
                error_message = "Supplier code already exists for another supplier"
                return render(request, 'add_supplier.html',
                              {'error_message': error_message, 'edit_supplier': supplier, 'suppliers': suppliers})

            supplier.save()

            success_message = "Supplier updated successfully"
            clear_form = True  # Set flag to clear the form

            if 'delete_supplier' in request.POST:
                # Delete the supplier if delete button clicked
                supplier_id = request.POST.get('supplier_id')
                supplier = Supplier.objects.get(pk=supplier_id)
                supplier.delete()
                return HttpResponseRedirect('/add_supplier/')

            return render(request, 'add_supplier.html',
                          {'add_supplier': supplier, 'success_message': success_message, 'suppliers': suppliers,'clear_form': clear_form})

        else:  # Add new supplier
            if Supplier.objects.filter(supplier_code=supplier_code).exists():
                error_message = "Supplier code already exists"
                return render(request, 'add_supplier.html', {'error_message': error_message, 'suppliers': suppliers})

            new_supplier = Supplier(
                supplier_code=supplier_code,
                supplier_name=supplier_name,
                supplier_address=supplier_address,
                supplier_city=supplier_city,
                supplier_country=supplier_country,
                supplier_postalCode=supplier_postalCode
            )
            new_supplier.save()

            success_message = "Supplier added successfully"
            return render(request, 'add_supplier.html', {'success_message': success_message, 'suppliers': suppliers})

    return render(request, 'add_supplier.html', {'edit_supplier': edit_supplier, 'suppliers': suppliers,'clear_form': clear_form})
