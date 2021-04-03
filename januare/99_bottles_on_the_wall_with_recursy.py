def bottles_of_beer(bob):
    """Writing text song about 99 bottles of beer.
        :param bob: must be unit number.
    """
    if bob < 1:
        print("""No bottles of beer on the wall.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall.{} bottles of beer.
                take one around {} bottles of beer on the wall
                """.format(tmp, tmp, bob))
    bottles_of_beer(bob)