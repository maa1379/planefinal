from django.contrib.auth import authenticate
from rest_framework import status, serializers, generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import LoginSerializer, PasswordChangeSerializer, UserUpdateSerializer,RegisterUserSerializer,\
    RegisterVerifiedSerializer,PasswordResetSerializer,PasswordResetVerifiedSerializer
from django.contrib.auth import authenticate
import random
from accounts.models import OtpCode
from accounts.uitils import send_otp

User = get_user_model()


class LoginApiView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            phone_number = serializer.data['phone_number']
            password = serializer.data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'first_name': user.profile.first_name,
                    'last_name': user.profile.last_name,
                    'email': user.profile.email,
                    'birthday': user.profile.birthday,
                }, status=status.HTTP_200_OK)
            else:
                content = {'detail': 'Unable to login with provided credentials.'}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# class Logout(APIView):
#     permission_classes = [IsAuthenticated, ]
#
#     def get(self, request, format=None):
#         """
#         Remove all auth tokens owned by request.user.
#         """
#         tokens = Token.objects.filter(user=request.user)
#         for token in tokens:
#             token.delete()
#         content = {'success': 'User logged out.'}
#         return Response(content, status=status.HTTP_200_OK)


class PasswordChangeApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = PasswordChangeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            new_password = serializer.data['new_password']
            old_password = serializer.data['old_password']

            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            content = {'detail': 'your old password is not valid'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserUpdateSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user.profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = self.serializer_class(data=request.data, instance=request.user.profile, partial=True)
        if serializer.is_valid():
            serializer.save()
            content = {'success': 'update account.'}
            return Response(content, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterUserApiView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = RegisterUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            phone_number = serializer.data.get('phone_number')
            password = serializer.data.get('password')
            user = None
            try:
                user_exists = User.objects.get(phone_number=phone_number)
                if user_exists.is_active:
                    content = {'error': 'Duplicate user.'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)
                else:
                    user = user_exists
            except:
                random_code = random.randint(1000, 9999)
                send_otp(phone_number, random_code)
                OtpCode.objects.create(phone_number=phone_number, code=random_code)
            content = {'success': 'otp code send.','phone_number':phone_number,'password':password,'code':random_code}
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterVerifyApiView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = RegisterVerifiedSerializer

    def post(self, request):
        serilizer = self.serializer_class(data=request.data)
        if serilizer.is_valid():
            phone_number = serilizer.data.get('phone_number')
            password = serilizer.data.get('password')
            code=serilizer.data.get('code')
            user_otp = OtpCode.objects.filter(phone_number=phone_number).last()
            if str(code) == str(user_otp.code):
                user=User.objects.create_user(phone_number=phone_number,password=password)
                user_otp.delete()
                token= Token.objects.create(user=user)
                content = {'success': 'user created',"token":token.key}
                return Response(content, status=status.HTTP_201_CREATED)

        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordReset(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            phone_number = serializer.data['phone_number']

            try:
                user = User.objects.get(phone_number=phone_number)
                random_code = random.randint(1000, 9999)
                send_otp(phone_number, random_code)
                OtpCode.objects.create(phone_number=phone_number, code=random_code)
                content = {'success': 'code sent.'}
                return Response(content, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                content = {'error': 'phone_number dose not exists..'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PasswordResetVerify(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = PasswordResetVerifiedSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            code = serializer.data['code']
            phone_number = serializer.data['phone_number']
            new_password = serializer.data['new_password']
            code_obj = OtpCode.objects.get(phone_number=phone_number,code=code)
            user_obj=User.objects.get(phone_number=phone_number)
            if code_obj :
                user_obj.set_password(new_password)
                user_obj.save()
                content = {'success': 'verify password.'}
                return Response(content, status=status.HTTP_200_OK)
            else:
                content={'error':'code is not match'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


