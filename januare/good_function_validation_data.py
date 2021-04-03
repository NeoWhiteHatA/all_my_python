def delete_product(product_id, user):
    if not user.is_admin():
        raise AuthError('for delete yoy have admin')
    if not store.has_product(product_id):
        raise ValueError('identificator unknown product')
    store.get_product(product_id).delete()