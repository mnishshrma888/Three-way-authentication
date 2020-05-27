import requests
import cv2
import face_recognition
import json
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import person
import random
# Create your views here.



def home( request):
    return render(request,'home.html')

def about( request):
    return render(request,'about.html')


def login(request):
    if request.method == 'POST':
        email1 = request.POST.get('email', "")
        password1 = request.POST.get('password', "")
        ver1 = person.objects.all()
        for i in ver1:
            ename1 = i.user_name1
            pswrd=i.password
            fname=i.first_name
            mob=i.mobile
            if ename1 == email1 and pswrd==password1:
                request.session['name']=fname
                request.session['email'] = email1
                request.session['phn']=mob
                return redirect('/otp_gen')
        else:
            messages.info(request, "Wrong id and password ,Please try again")
            return redirect('/login')
    else:
        return render (request,'login1.html')

def forgot_pswrd(request):
    if request.method == 'POST':
        email2 = request.POST.get('email3', "")
        password2 = request.POST.get('password1', "")
        password3 = request.POST.get('password2', "")
        try:
            ver2 = person.objects.get(user_name1=email2)
            mob = ver2.mobile
            print(mob)
            request.session['phn'] = mob
            if password2==password3:
                print(ver2.password)
                ver2.password=password2
                ver2.save()
                return redirect('/otp_gen2')
            else:
                messages.info(request, "Password not match ,Please try again")
                return redirect('/forgot_pswrd')
        except:
            messages.info(request, "Enter valid data,Please try again")
            return redirect('/forgot_pswrd')
    else:
        return render(request, 'forgot_pss.html')

def signup(request):
    if request.method == 'POST':
        first = request.POST.get('first_name', "")
        last = request.POST.get("last_name", "")
        email2 = request.POST.get("email1", "")
        password2 = request.POST.get("password1", "")
        mobile = request.POST.get("mobile", "")
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")
        gender = request.POST.get("gender", "")
        request.session['email'] = email2
        ver = person.objects.all()
        for i in ver:
            ename=i.user_name1
            if ename==email2:
                messages.info(request,"Email already exist")
                return redirect('/signup')
            elif len(mobile) != 10:
                messages.info(request, "Enter valid mobile no")
                return redirect('/signup')

        else:
            sig = person(first_name=first,last_name=last,user_name1=email2,password=password2,mobile=mobile,address=address,city=city,gender=gender)
            sig.save()
            return redirect('/capture')
    else:
        return render (request,'signup1.html')


def capture(request):
    email2=request.session['email']
    ver5 = person.objects.get(user_name1=email2)
    name5 = ver5.first_name
    param={'name':name5,'id':'images/'+email2+'.jpg'}
    return render(request, 'capture.html',param)

def click(request):
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    id2=request.session['email']
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite("C:/Users/Manish sharma/PycharmProjects/django1/newapp/static/images/" + str(id2) + ".jpg", img1)
    cv2.imshow("face", img1)
    cap.release()
    return redirect('/capture')



def otp_gen(request):
    a = random.randint(10000, 55555)
    request.session['otp'] = str(a)
    phn = request.session['phn']
    URL = 'https://www.sms4india.com/api/v1/sendCampaign'
    def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
        req_params = {
            'apikey': apiKey,
            'secret': secretKey,
            'usetype': useType,
            'phone': phoneNo,
            'message': textMessage,
            'senderid': senderId
        }
        return requests.post(reqUrl, req_params)
    response = sendPostRequest(URL, 'FW7GPHO9N17RWMDX4IJXKGJRRCJJESS8', 'IRAJ4NFA6GNDIC3H', 'stage', phn,
                               'SMSIND', 'your OTP  is :' + str(a))
    print(response.text)
    return redirect('/otp')

def otp_gen2(request):
    a = random.randint(10000, 55555)
    request.session['otp1'] = str(a)
    phn = request.session['phn']
    URL = 'https://www.sms4india.com/api/v1/sendCampaign'
    def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
        req_params = {
            'apikey': apiKey,
            'secret': secretKey,
            'usetype': useType,
            'phone': phoneNo,
            'message': textMessage,
            'senderid': senderId
        }
        return requests.post(reqUrl, req_params)
    response = sendPostRequest(URL, 'FW7GPHO9N17RWMDX4IJXKGJRRCJJESS8', 'IRAJ4NFA6GNDIC3H', 'stage', phn,
                               'SMSIND', 'your OTP  is :' + str(a))
    print(response.text)
    return redirect('/otp1')

def otp(request):
    value=request.session['otp']
    if request.method == 'POST':
        opt1 = request.POST.get("otp1", "")
        if opt1==value:
            return redirect('/face')
        else:
            messages.info(request, "Wrong OTP")
            return redirect('/otp')
    else:
        return render (request,'otp1.html')


def otp1(request):
    value1=request.session['otp1']
    if request.method == 'POST':
        opt2 = request.POST.get("otp2", "")
        if opt2==value1:
            return redirect('/login')
        else:
            messages.info(request, "Wrong OTP")
            return redirect('/otp1')
    else:
        return render (request,'otp2.html')


def face(request):
    email=request.session['email']

    def facedect(loc):
        cam = cv2.VideoCapture(0)
        s, img = cam.read()
        if s:
            cv2.namedWindow("cam-test")
            cv2.imshow("cam-test", img)
            cv2.waitKey(10000)
            cv2.destroyWindow("cam-test")

            cv2.imwrite("filename.jpg", img)
            loc = ("C:/Users/Manish sharma/PycharmProjects/django1/newapp/static/images/" + str(loc) + ".jpg")
            print(loc)
            face_1_image = face_recognition.load_image_file(loc)
            face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]
            small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

            rgb_small_frame = small_frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            check = face_recognition.compare_faces(face_1_face_encoding, face_encodings)

            print(check)
            if check[0]:
                return True

            else:
                return False


    facedect(email)

    return render(request, 'face.html')
