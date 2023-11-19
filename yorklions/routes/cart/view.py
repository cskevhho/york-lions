from flask import render_template, session
from flask_login import current_user

def view_cart():
    cart_items = session.get('cart', [])
    # Calculate the total price of items in the cart
    total = sum(item['total_price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total, current_user=current_user)