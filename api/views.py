from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import CartSerializer, CartDeleteItemSerializer
from apps.checkout.models import CartItem
from django.db.models import Sum, F


@api_view(["GET"])
def api_get_cart_header(request):
    items = CartItem.objects.filter(user=request.user)
    total_price = items.annotate(item_total=F("price") * F("quantity")).aggregate(
        total_price=Sum("item_total")
    )["total_price"]
    serializer = CartSerializer(items, many=True)
    response_data = {"items": serializer.data, "total_price": total_price}
    return Response(response_data)


@api_view(["POST"])
def api_add_cart(request):
    data = request.data.copy()
    data["user"] = request.user.id
    serializer = CartSerializer(data=data)
    if serializer.is_valid():
        try:
            cart_item = CartItem.objects.get(
                user=request.user, item_name=data["item_name"]
            )
            cart_item.quantity += int(data["quantity"])
            cart_item.save()
            return Response({"Success": "Data was added to existed product!"})
        except CartItem.DoesNotExist:
            serializer.save()
            return Response({"Success": "New item was added to the cart!"})
    return Response(serializer.errors)


@api_view(["DELETE"])
def api_delete_cart(request):
    data = {"user": request.user.id, "item_name": request.data["item_name[produce]"]}
    serializer = CartDeleteItemSerializer(data=data)
    if serializer.is_valid():
        try:
            cart_item = CartItem.objects.get(
                user=request.user, item_name=data["item_name"]
            )
            cart_item.delete()
            return Response({"Success": "Item was delete from the cart!"})
        except CartItem.DoesNotExist:
            return Response({"Error": "Item dont exist!"})

    return Response(serializer.errors)
