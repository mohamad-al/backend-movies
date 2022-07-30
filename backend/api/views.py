

from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .makejson.makejson import Search , Home , Movies , Play , Watch


def mhome(request):
    import requests

    r = requests.get("https://x.cimalight.vip/",)
    print(r)
    return HttpResponse('ggg')


class WatchApiView(APIView):
    def get(self, request):
        # try:
        id = request.query_params['id']
        return Response(Watch(id).getresult())
        # except Exception as e:
        #     response = {'message': f"no query params name 'id' {e}"}
        #     return Response(response, status=status.HTTP_400_BAD_REQUEST) 

class SearchApiView(APIView):
    def get(self, request):
        try:
            key_word = request.query_params['key_word']
            try:
                page = request.query_params['page']
                return Response(Search(key_word,page).getresult())
            except:
                return Response(Search(key_word).getresult())
        except:
            response = {'message': "no query params name 'key_word'"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 



class PlayApiView(APIView):
    def get(self, request):
        try:
            id =request.query_params['id']
            name =request.query_params['name']
            return Response(Play(name = name, id = id).getResult())
        except:
            response = {'message': "no query params name 'name' and 'id"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 



class HomeApiView(APIView):
    def get(self, request):
        return Response(Home().getResult())




class MoviesApiView(APIView):
    def get(self, request):
        try:
            cat = request.query_params['cat']
            try:
                page = int(request.query_params['page'])
                return Response(Movies(cat =cat,page=page).getResult())
            except Exception as e:
                
                 return Response(Movies(cat =cat).getResult() )
        except Exception as e:
            response = {'message': "You can't search like that"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 
