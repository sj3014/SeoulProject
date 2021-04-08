from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, exceptions
from .serializers import StudentSerializer
from .models import Student
from apps.quarantine import models as qm, serializers as qs
from apps.country import models as cm, serializers as cs
from apps.university import models as um, serializers as us
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import APIException
from django.views.decorators.csrf import ensure_csrf_cookie
from .utils import generate_access_token, generate_refresh_token
from django.utils import timezone


# get student lists or add new student
class StudentListAPIView(APIView):
    def get(self, request):
        serializer = StudentSerializer(Student.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# get student detail or update/delete student
class StudentDetailAPIView(APIView):
    def get_object(self, uuid):
        return get_object_or_404(Student, uuid=uuid)

    def get(self, request, uuid, format=None):
        student = self.get_object(uuid)
        serializer = StudentSerializer(uuid)
        return Response(serializer.data)

    def put(self, request, uuid):
        student = self.get_object(uuid)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        student = self.get_object(uuid)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @authentication_classes((SessionAuthentication, BasicAuthentication))


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    response = Response()
    if (email is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'studentname and password required')

    student = get_object_or_404(Student, email=email)
    if(student is None):
        raise exceptions.AuthenticationFailed('student not found')

    serialized_student = StudentSerializer(student).data
    if (serialized_student['password'] != password):
        raise exceptions.AuthenticationFailed('wrong password')

    serialized_student = StudentSerializer(student).data

    access_token = generate_access_token(serialized_student)
    refresh_token = generate_refresh_token(serialized_student)

    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
    }
    return response


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def signup_view(request):
    response = Response()
    print(request)
    print(request.data)
    email = request.data.get('email')
    password = request.data.get('password')
    countryID = request.data.get("countryID")
    universityID = request.data.get("universityID")

    try:
        student = Student.objects.create(email=email, password=password,
                                         country_id=countryID, university_id=universityID)
    except:
        return Response(data={"error": "Email is already associated with an student"}, status=400)
    quarantine = qm.Quarantine.objects.create()
    student.quarantine = quarantine
    student.save()

    serialized_student = StudentSerializer(student).data
    access_token = generate_access_token(serialized_student)
    refresh_token = generate_refresh_token(serialized_student)

    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
    }
    response.status_code = 201
    return response
