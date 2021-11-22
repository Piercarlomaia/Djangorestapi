from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  cursos, aulas, User2
from .serializers import  CursosSerializer, AulasSerializer, UserSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated



from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.

class UserAdminView(APIView):

    permission_classes = (IsAdminUser,)
    def get(self, request, *args, **kwargs):
        queryset = User2.objects.all()
        serializer = UserSerializer(queryset, many=True)
        #if serializer.is_valid():

        #print(User2.objects.filter(email=request.user).values("professor"))
        #print(cursos.objects.filter(usuarios=self.request.user) )
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors)

class UseraAdminViewDetail(APIView):

    permission_classes = (IsAdminUser,)
    def get(self, request, pk, *args, **kwargs):

        queryset = User2.objects.filter(pk=pk)
        serializer = UserSerializer(queryset, many=True)
        #if serializer.is_valid():
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        queryset = User2.objects.get(pk=pk)
        serializer = UserSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    def delete(self, request, pk, *args, **kwargs):
        queryset = User2.objects.get(pk=pk)
        queryset.delete()
        #if serializer.is_valid():
        return Response(HTTP_204_NO_CONTENT)




class CursosAdminView(APIView):

    permission_classes = (IsAdminUser,)
    def get(self, request, *args, **kwargs):
        queryset = cursos.objects.all()
        serializer = CursosSerializer(queryset, many=True)
        #if serializer.is_valid():
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        serializer = CursosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors)

class CursosaAdminViewDetail(APIView):

    permission_classes = (IsAdminUser,)
    def get(self, request, pk, *args, **kwargs):

        queryset = cursos.objects.filter(pk=pk)
        serializer = CursosSerializer(queryset, many=True)
        #if serializer.is_valid():
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        queryset = cursos.objects.get(pk=pk)
        serializer = CursosSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    def delete(self, request, pk, *args, **kwargs):
        queryset = cursos.objects.get(pk=pk)
        queryset.delete()
        #if serializer.is_valid():
        return Response(HTTP_204_NO_CONTENT)


class AulasAdminView(APIView):

    permission_classes = (IsAdminUser,)
    def get(self, request, *args, **kwargs):
        queryset = aulas.objects.all()
        serializer = AulasSerializer(queryset, many=True)
        #if serializer.is_valid():
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AulasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors)

class AulasaAdminViewDetail(APIView):

    permission_classes = (IsAdminUser,)
    def get(self, request, pk, *args, **kwargs):

        queryset = aulas.objects.filter(pk=pk)
        serializer = AulasSerializer(queryset, many=True)
        #if serializer.is_valid():
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        queryset = aulas.objects.get(pk=pk)
        serializer = AulasSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    def delete(self, request, pk, *args, **kwargs):
        queryset = aulas.objects.get(pk=pk)
        queryset.delete()
        #if serializer.is_valid():
        return Response(HTTP_204_NO_CONTENT)

class ProfessorView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        if request.user.is_professor:
            queryset = cursos.objects.filter(professores=self.request.user)

            serializer = CursosSerializer(queryset, many=True)
            #print(serializer)
            return Response(serializer.data)

        return Response(serializer.errors)
    def post(self, request, *args, **kwargs):
        serializer = CursosSerializer(data=request.data)
        if request.user.is_professor:

            if serializer.is_valid():
                serializer.validated_data["usuarios"] = []


                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)

            return Response(serializer.errors)

class ProfessorViewDetail(APIView):

    permission_classes = (IsAdminUser,)
    def get(self, request, pk, *args, **kwargs):

        queryset = User2.objects.filter(pk=pk)
        serializer = UserSerializer(queryset, many=True)
        #if serializer.is_valid():
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        queryset = User2.objects.get(pk=pk)
        serializer = UserSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    def delete(self, request, pk, *args, **kwargs):
        queryset = User2.objects.get(pk=pk)
        queryset.delete()
        #if serializer.is_valid():
        return Response(HTTP_204_NO_CONTENT)