from flask import session, request, flash, redirect, url_for
from flask_login import current_user
from ...models.vehicle import Vehicle

from ..address.create import create_address
from ..po.create import create_po
from ..user.create import create_user
from ..user.read import get_user
from ..user.delete import delete_guest_users

import uuid

def submit_order():
    fname = request.form["fname"]
    lname = request.form["lname"]

    phone = request.form["phone"]
    street_address = request.form["street_address"]
    city = request.form["city"]
    postal_code = request.form["postal_code"]
    province = request.form["province"]

    cc_type = request.form["cc_type"]
    cc_num = request.form["cc_num"]
    cc_cvv = request.form["cc_cvv"]
    cc_name = request.form["cc_name"]
    cc_exp_month = request.form["cc_exp_month"]
    cc_exp_year = request.form["cc_exp_year"]
    # TODO: Use banking information

    cart_items = session.get('cart', [])
    # Calculate the total price of items in the cart
    total = sum(item['total_price'] for item in cart_items)

    vehicles = []
    for item in cart_items:
        vehicle = Vehicle.query.get(item["id"])
        if vehicle is not None:
            vehicles.append(vehicle)

    if current_user.is_anonymous:
        unique_str = f'guest_user_{uuid.uuid4().hex}'
        dummy_email = f"{unique_str}@guest.com"
        user_id = create_user(username=unique_str, email=dummy_email, password="", is_guest=True)[0]["new_user_id"]
        user = get_user(user_id)
    else:
        user = current_user

    result, status_code = create_address(street_address, city, province, postal_code, phone, user)
    address_id = result["new_address_id"]

    result, status_code = create_po(fname=fname, lname=lname, address_id=address_id, vehicles=vehicles, cc_type=cc_type, cc_last_4_digits=cc_num[-4:], user=user)
    po_id = result["new_po_id"]
    
    if "cart" in session:
        session.pop("cart")
    delete_guest_users()
    # should return redirect for confirmed-order.html
    return redirect(url_for("confirmedorder.confirmed", po_id=po_id), code=307)
