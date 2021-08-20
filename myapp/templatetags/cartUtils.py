from django import template

register = template.Library()

@register.filter(name = "isInStock")
def isInStock(book,cart):
    return book.Qty > (0 if cart.get(str(book.Isbn_No)) is None else cart.get(str(book.Isbn_No)))

@register.filter(name = "remainingStock")
def remainingStock(book,cart):
    return book.Qty - (0 if cart.get(str(book.Isbn_No)) is None else cart.get(str(book.Isbn_No)))

@register.filter(name= "itemsInCart")
def itemsInCart(cart):
    noOfItems = 0
    for _,v in cart.items():
        noOfItems += v
    return noOfItems


@register.filter(name= "itemsCount")
def itemsCount(book,cart):
    return cart.get(str(book.Isbn_No))


@register.filter(name= "totalAmount")
def totalAmount(book,cart):
    return cart.get(str(book.Isbn_No)) * book.Price

@register.filter(name= "subtotal")
def subtotal(book,cart):
    sum = 0
    i = 0
    for _,v in cart.items():
        sum = sum + (v * book[i].Price)
        i += 1
    return sum

    