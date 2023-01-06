from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView #apiview es como el view del django normal
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer,TestUserSerializer

@api_view(['GET','POST'])
def UserApiView(request):
    if request.method == 'GET':
        user = User.objects.all()
        users_serializer =UserSerializer(user,many=True)#el many es para que serialize todos los usuarios si no solo serializaria uno, asi el serializador sabe que no le enviamos uno solo si no un listado
        
        test_data = {
            'name':'developer',
            'email':'holapapu@gmail.com'
        }
        test_user = TestUserSerializer(data=test_data,context=test_data)
        if test_user.is_valid():
            user_instance = test_user.save()
            print(user_instance)
        else:
            print(test_user.errors)

        
        
        return Response(users_serializer.data,status=status.HTTP_200_OK) #tenemos que poner el status es una buena practica 
        #el data es importante no podemos mandar el json asi nomas
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'mensanje':'usuario creado correctamente!'},status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT','DELETE'])
def user_detail_view(request,pk=None):
    user = User.objects.filter(id =pk).first()
    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data,status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            # users_serialezer = UserSerializer(user,data=request.data)
            # if users_serialezer.is_valid():
            #     users_serialezer.save()
            #     return Response(users_serialezer.data,status=status.HTTP_200_OK)
            # return Response(users_serialezer.errors,status=status.HTTP_400_BAD_REQUEST)


            users_serialezer = TestUserSerializer(user,data=request.data)
            if users_serialezer.is_valid():
                users_serialezer.save()
                return Response(users_serialezer.data,status=status.HTTP_200_OK)
            return Response(users_serialezer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method =='DELETE':
            user.delete()
            return Response({'mensanje':'usuario eliminado correctamente!'},status=status.HTTP_200_OK) #pasamos el mensaje como un diccionaraio y el fronet tomaja la variable mesanje para mostrar el mensaje
    return Response({'mensaje':'no se a encontrado usuario con estos datos'},status=status.HTTP_400_BAD_REQUEST)