from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  cursos, aulas, User2
from .serializers import  CursosSerializer, AulasSerializer, UserSerializer, CursosAlunosSerializer, Cursosalunosid

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

class ProfessorCursoView(APIView):

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




class ProfessorCursoViewDetail(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, *args, **kwargs):

        if request.user.is_professor:
            queryset = cursos.objects.filter(pk=pk, professores=self.request.user)

            serializer = CursosSerializer(queryset, many=True)
            # print(serializer)
            return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        profile = cursos.objects.get(pk=pk, professores=self.request.user)
        serializer = CursosSerializer(profile, data=request.data)
        if request.user.is_professor:
            queryset = list(cursos.objects.filter(pk=pk, professores=self.request.user).values_list("usuarios", flat=True))

            #print(queryset.values_list("usuarios", flat=True))

            if serializer.is_valid():
                serializer.validated_data["id"] = pk
                serializer.validated_data["usuarios"] = queryset
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        if request.user.is_professor:
            queryset = cursos.objects.get(pk=pk, professores=self.request.user)
            queryset.delete()
            # if serializer.is_valid():
            return Response(HTTP_204_NO_CONTENT)


class ProfessorAulasView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        if request.user.is_professor:
            queryset = aulas.objects.filter(professor=self.request.user)

            serializer = AulasSerializer(queryset, many=True)
            #print(serializer)
            return Response(serializer.data)

        return Response(serializer.errors)
    def post(self, request, *args, **kwargs):
        serializer = AulasSerializer(data=request.data)
        if request.user.is_professor:

            if serializer.is_valid():
                serializer.validated_data["professor"] = self.request.user


                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)

            return Response(serializer.errors)

class ProfessorAulasDetailView(APIView):


    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, *args, **kwargs):

        if request.user.is_professor:
            queryset = aulas.objects.filter(pk=pk, professor=self.request.user)

            serializer = AulasSerializer(queryset, many=True)
            # print(serializer)
            return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        profile = aulas.objects.get(pk=pk, professor=self.request.user)
        serializer = AulasSerializer(profile, data=request.data)
        if request.user.is_professor:

            #print(queryset.values_list("usuarios", flat=True))

            if serializer.is_valid():
                serializer.validated_data["id"] = pk
                serializer.validated_data["professor"] = self.request.user
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        if request.user.is_professor:
            queryset = aulas.objects.get(pk=pk, professor=self.request.user)
            queryset.delete()
            # if serializer.is_valid():
            return Response(HTTP_204_NO_CONTENT)

class AlunoCursoView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):

        queryset = cursos.objects.filter()

        serializer = CursosAlunosSerializer(queryset, many=True)
        #print(serializer)
        return Response(serializer.data)

class AlunoCursoDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, *args, **kwargs):


        queryset = cursos.objects.filter(pk=pk )

        serializer = CursosAlunosSerializer(queryset, many=True)
        # print(serializer)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        queryset = cursos.objects.get(pk=pk)
        serializer = Cursosalunosid(queryset, data=request.data)



        if serializer.is_valid():

            userlist = list(cursos.objects.filter(pk=pk).values_list("usuarios", flat=True))
            if self.request.user.id in userlist:
                userlist.remove(self.request.user.id)
                print(userlist)
                print("removed")
                serializer.validated_data["usuarios"] = userlist
                serializer.save()
                return Response(request.data)
            else:
                userlist.append(self.request.user.id)
                print(userlist)
                print("append")
                serializer.validated_data["usuarios"] = userlist
                serializer.save()
                return Response(request.data)


        return Response(serializer.errors)


class AlunoAulasDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk_cursos,  *args, **kwargs):
        userlist = list(cursos.objects.filter(id=pk_cursos).values_list("usuarios", flat=True))
        if self.request.user.id in userlist:

            aulaslist = list(cursos.objects.filter(id=pk_cursos).values_list("aulas", flat=True))
            queryset = aulas.objects.filter(id__in=aulaslist)


            serializer = AulasSerializer(queryset, many=True)
            # print(serializer)
            return Response(serializer.data)

