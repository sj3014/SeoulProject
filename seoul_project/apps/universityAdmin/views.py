from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .serializers import UniversityAdminSerializer
from .models import UniversityAdmin
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.student.utils import generate_access_token, generate_refresh_token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import ensure_csrf_cookie
from .authentication import UniversityAdminJWTAuthentication
from .permissions import UniversityAdminPermission
from apps.student.models import Student
from apps.student.serializers import StudentSerializer
from django.http import Http404
from rest_framework.decorators import renderer_classes
from rest_framework import renderers, response, schemas


# get admin lists or add new admin
class UniversityAdminListAPIView(APIView):
    def get(self, request):
        serializer = UniversityAdminSerializer(
            UniversityAdmin.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UniversityAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# get universityAdmin detail or update/delete universityAdmin
class UniversityAdminDetailAPIView(APIView):
    def get_object(self, uuid):
        return get_object_or_404(UniversityAdmin, uuid=uuid)

    def get(self, request, uuid, format=None):
        universityAdmin = self.get_object(uuid)
        serializer = UniversityAdminSerializer(universityAdmin)
        return Response(serializer.data)

    def put(self, request, uuid):
        universityAdmin = self.get_object(uuid)
        serializer = UniversityAdminSerializer(
            universityAdmin, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        universityAdmin = self.get_object(uuid)
        universityAdmin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([UniversityAdminJWTAuthentication])
@ensure_csrf_cookie
def university_student_list_view(request):
    students = list(Student.objects.select_related('quarantine', 'address').filter(
        university_id=request.user.university_id))

    for student in students:
        university_of_admin = request.user.university_id
        university_of_student = student.university_id

        if university_of_admin != university_of_student:
            return Response({"error": "The admin is not authorized to get information of the student(s)"})

    serialized_students = StudentSerializer(students, many=True)
    return Response(serialized_students.data)


@api_view(['GET'])
@authentication_classes([UniversityAdminJWTAuthentication])
@ensure_csrf_cookie
def university_student_detail_view(request, uuid: str):
    try:
        student = Student.objects.select_related(
            'quarantine', 'address').get(uuid=uuid, university_id=request.user.university_id)
    except Student.DoesNotExist:
        return Response({"error": "Student with the provided university_id does not exist"}, status=404)

    university_of_admin = request.user.university_id
    university_of_student = student.university_id

    if university_of_admin != university_of_student:
        return Response({"error": "The admin is not authorized to get information of the student(s)"})

    serialized_student = StudentSerializer(student)
    return Response(serialized_student.data)


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    response = Response()
    if (email is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'email and password required')

    university_admin = get_object_or_404(UniversityAdmin, email=email)
    if(university_admin is None):
        raise exceptions.AuthenticationFailed('university_admin not found')

    serialized_university_admin = UniversityAdminSerializer(
        university_admin).data
    if (serialized_university_admin['password'] != password):
        raise exceptions.AuthenticationFailed('wrong password')

    if not university_admin.is_verified:
        return Response({"error: university admin is not verified"}, status=400)

    serialized_university_admin = UniversityAdminSerializer(
        university_admin).data

    access_token = generate_access_token(serialized_university_admin)
    refresh_token = generate_refresh_token(serialized_university_admin)

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
    email = request.data.get('email')
    password = request.data.get('password')
    university_id = request.data.get("university_id")
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')

    try:
        university_admin = UniversityAdmin.objects.create(email=email, password=password, first_name=first_name,
                                                          last_name=last_name, university_id=university_id)
    except:
        return Response(data={"error": "Either the university admin already exists or provided fields are wrong"}, status=400)

    serialized_university_admin = UniversityAdminSerializer(
        university_admin).data
    access_token = generate_access_token(serialized_university_admin)
    refresh_token = generate_refresh_token(serialized_university_admin)

    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
    }
    response.status_code = 201
    return response
