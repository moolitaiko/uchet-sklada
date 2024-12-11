from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy # reverse_lazy -> Ждет пока окончится процесс, и только после перенаправляет



from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
import openpyxl
import os
from .experiments import *
from .permissions import *
from .models import *
from .serializers import *
from django.utils.timezone import localtime



class RegistrationApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        from django.contrib.auth.models import User
        from django.db import IntegrityError
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.create_user(username=username, password=password)
            owner = Owner(user=user)
            owner.save()
            return Response(data={'message': 'Registration success'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(data={'message': 'Username is already registered'}, status=status.HTTP_400_BAD_REQUEST)


class AuthApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        from django.contrib.auth import login, authenticate
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return Response(data={'message': 'Invalid username/password'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            login(request, user)
            return Response(data={'message': 'Auth success!'}, status=status.HTTP_200_OK)

class SellerRegistrationApiView(APIView):
    permission_classes = [IsOwner]

    def post(self, request):
        from django.contrib.auth.models import User
        from django.db import IntegrityError
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.create_user(username=username, password=password)
            seller = Seller(user = user, owner = Owner.objects.get(user = request.user.id))
            seller.save()
            return Response(data={'message': 'Registration success'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(data={'message': 'Username is already registered'}, status=status.HTTP_400_BAD_REQUEST)




class UserApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_user = request.user
        user = UserSerializer(current_user).data
        return Response(data=user, status=status.HTTP_200_OK)

    def delete(self, request):
        current_user = request.user
        current_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request):
        current_user = request.user
        serializer = UserSerializer(current_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OwnerApiView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request):
        owner = Owner.objects.get(user=request.user.id)
        owner = OwnerSerializer(owner).data
        return Response(data=owner, status=status.HTTP_200_OK)

    def delete(self, request):
        # seller = Seller.objects.get(user = request.user.id)
        # seller.delete()
        request.user.delete()
        return Response(data={'message': 'Username is deleted'}, status=status.HTTP_204_NO_CONTENT)


    def put(self, request):
        owner = Owner.objects.get(user=request.user.id)
        serializer = OwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SellerApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        seller = Seller.objects.get(user = request.user.id)
        seller = SellerSerializer(seller).data
        return Response(data=seller, status=status.HTTP_200_OK)

    def delete(self, request):
        # seller = Seller.objects.get(user = request.user.id)
        # seller.delete()
        request.user.delete()
        return Response(data={'message': 'Username is deleted'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        seller = Seller.objects.get(user = request.user.id)
        serializer = SellerSerializer(seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class SearchApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        search = request.GET.get('search')
        search_by_name = Product.objects.filter(name__contains=search)

        data = ProductSerializer(search_by_name, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

# class SearchApiView(APIView):
#     permission_classes = [AllowAny]
#
#     def get(self, request):
#         search = request.GET.get('search')
#         if search:
#             search_by_name = Product.objects.filter(name__contains=search)
#
#         data = ProductSerializer(search_by_name, many=True).data
#         return Response(data=data, status=status.HTTP_200_OK)



class TimeTestApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(data={'today': localtime()}, status=status.HTTP_200_OK)

# сортировка по возрастанию буыванию
class OtAdoYaApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        purchase_price = request.GET.get('purchase_price')
        sklad = Sklad.objects.all()

        if purchase_price is not None:
            if purchase_price == 'desc':
                sklad = sklad.order_by('-purchase_price')
            elif purchase_price == 'asc':
                sklad = sklad.order_by('purchase_price')

        data = SkladSerializer(sklad, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class ProductPaginatedApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        products = Product.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 50
        paginated_products = paginator.paginate_queryset(products, request)
        data = ProductSerializer(paginated_products, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

class AcrossSkladProductApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            request.data['product']=product.data['id']
            sklad = SkladSerializer(data=request.data)
            if sklad.is_valid():
                sklad.save()
                return Response(data={"message": "запись создана"}, status = status.HTTP_200_OK)
            else:
                return Response(data = sklad.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data = product.errors, status=status.HTTP_400_BAD_REQUEST)


class PrintCheck(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        sale_id = request.GET.get('sale_id')
        if sale_id is None:
            return Response(data={"message": "sale_id - это обязательный параметр"}, status = status.HTTP_400_BAD_REQUEST)
        sale = get_object_or_404(Sales, id = sale_id)
        file_name = GenerateCheck(sale)

        f = open(file_name, 'rb')
        response = FileResponse(f, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_name)}'
        return response

class CreateProductApiView(APIView):
    permission_classes = [IsOwner]
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




