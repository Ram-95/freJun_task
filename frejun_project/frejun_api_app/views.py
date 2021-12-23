from django.shortcuts import render
from django.http import HttpResponse
from .models import PhoneNumber, Account
from .authentication import AccountAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .serializers import AccountSerializer
# Create your views here.


def index(request):
    return HttpResponse("Welcome to FreJun API.")


def data_validation(input_param, txt: str) -> dict:
    """Validation code for the input parameters."""
    data_dictionary = {'message': '', 'errors': ''}
    if input_param is None: # checks if input_param is None
        data_dictionary['errors'] = txt + ' is missing'
    else:   # check the length of strings
        if txt == 'text':
            if len(input_param) not in range(1, 121):
                data_dictionary['errors'] = txt + ' is invalid'
        else:
            if len(input_param) not in range(6, 17):
                data_dictionary['errors'] = txt + ' is invalid'

    return data_dictionary



@csrf_exempt
@api_view(['POST'])
def inbound(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            account = data.get('username')
            frm = data.get('from', None)
            to = data.get('to', None)
            text = data.get('text', None)
            input_params_list = [(frm,'from'), (to, 'to'), (text, 'text')] 
            # Looping through the parameters
            for k,v in input_params_list:
                res_dict = data_validation(k, v)
                if res_dict['errors'] != '':
                    return Response(res_dict)

            # Checking if "to" is present in PhoneNumber model for this account 
            try:
                account_id = Account.objects.get(username=account)
                ph = PhoneNumber.objects.get(account=account_id, number=to)
            except PhoneNumber.DoesNotExist:
                return Response({'message': '', 'errors': 'to parameter not found'})

            return Response({'message': 'inbound sms ok', 'error': ''}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



def outbound(request):
    return HttpResponse("You are at OUTBOUND SMS Route.")


