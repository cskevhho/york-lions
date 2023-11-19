from flask import session

def remove_vehicle(item_id):
    if 'cart' in session:
        cart_items = session['cart']
        # Find the index of the item to remove from the cart
        for index, item in enumerate(cart_items):
            if item['id'] == int(item_id):
                del cart_items[index]  # Remove the item from the cart
                session['cart'] = cart_items  # Update the cart in the session
                return {"message": "Item removed successfully"}, 200
    return {"message": "item not found in cart"}, 200
