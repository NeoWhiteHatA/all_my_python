def delete_product(prod_id, user):
    assert user.is_admin(), 'here must be admin'
    assert store.has_product(prod_id), 'Unknown product'
    store.get_product(prod_id).delete()