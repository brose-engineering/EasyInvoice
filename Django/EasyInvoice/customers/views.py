from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Customer
from .forms import NewCustomerForm

# Define a view function called 'index' which handles requests to the URL '/customers/'
def index(request):
    # Check if the request method is POST (e.g., when submitting a form)
    if request.method == "POST":
        pass  # This block does nothing for now, but might be used later
    else:  # If it's not a POST request, render an HTML template
        return render(request, "customers/index.html", {
            # Pass the title 'Easy Invoice - Kunden' to the template
            "title": "Easy Invoice - Kunden",
            # Get all customers from the database and pass them to the template
            "customers": Customer.objects.all()
        })
       

# Function to edit a customer's details
def edit(request, customer_id):
    """
    Edit a customer's information
    
    Parameters:
        request: The HTTP request object
        customer_id: The ID of the customer to be edited
        
    Returns:
        A rendered template with the form data if the request is valid,
        or an error message if the form is invalid
    """
    # Get the customer object by their ID using a custom function
    customer = get_object_or_404(Customer, customer_id = customer_id)

    if request.method == 'POST':
        """
        If the request method is POST (i.e., the user submitted the form),
        create a new instance of the NewCustomerForm with the existing customer data
        and validate it. If the form is valid, save the changes and redirect to the customers page.
        """
        form = NewCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/customers/")
    else:
        # If the request method is not POST (i.e., the user loaded the edit page for the first time),
        # create a new instance of the NewCustomerForm with the existing customer data
        form = NewCustomerForm(instance=customer)

    return render(request, 'customers/edit.html', {
        "form": form, 
        "customer": customer,
        "title": "Easy Invoice - Kunde bearbeiten",
    })



def delete(request, customer_id):
    """
    Deletes a customer from the database and redirects back to the customers list.

    :param request: The HTTP request object.
    :param customer_id: The ID of the customer to be deleted.
    """
    # Retrieve the customer object with the given customer_id. If not found, raise a 404 error.
    customer = get_object_or_404(Customer, customer_id=customer_id)
    
    # Delete the customer from the database
    customer.delete()
    
    # Redirect back to the customers list after deletion
    return HttpResponseRedirect("/customers/")

    
    
def add_new(request):
    """
    This function handles the request to create a new customer.
    It checks if the request method is POST, and if so, 
    validates and saves the form data. If the request method is not POST,
    it renders an empty form for adding a new customer.

    Args:
        request (object): The HTTP request object.

    Returns:
        HttpResponse: A response containing either a successful message or
            a rendered HTML template.
    """
    
    # Check if the request method is POST
    if request.method == "POST":
        """
        If the request method is POST, create a form instance with the 
        submitted data.
        """
        form = NewCustomerForm(request.POST)
        
        # Check if the form is valid (i.e., all fields are filled correctly)
        if form.is_valid():
            """
            If the form is valid, save it to the database and return a 
            successful message.
            """
            form.save()
            return HttpResponseRedirect("/customers/")
    
    else:
        """
        If the request method is not POST, create an empty form for adding
        a new customer. Then render this form as an HTML template.
        """
        form = NewCustomerForm()
        return render(request, "customers/add_new.html", {
            "title": "Easy Invoice - Neuer Kunden",
            "form": form
        })
