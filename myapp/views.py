from rest_framework import mixins#混合视图
from rest_framework import generics#视图的基类
from rest_framework.response import Response
from rest_framework import status
from .models import Publisher
from .serializers import PublisherSerializer
from rest_framework import permissions #权限
from rest_framework.views import APIView
from .mypermissions import IsOwerOrReadOnly



# class PublisherList(generics.ListCreateAPIView#获取所有模型类对象
#     ,mixins.CreateModelMixin#创建一个新的资源到数据库
#     ,generics.GenericAPIView):
class PublisherList(generics.ListCreateAPIView):  # 获取所有模型类对象

    queryset = Publisher.objects.all()#数据源
    serializer_class = PublisherSerializer#序列化
    permission_class = (IsOwerOrReadOnly,)#进过认正以后的用户进行相关的操作



    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs)
    #
    # def post(self,request,*args,**kwargs):
    #     return self.create(request,*args,**kwargs)
    #
    # """
    # 获取单个 修改单个 删除单个  模型类对象 （出版社)
    # """
# class PublisherDetail(generics.RetrieveDestroyAPIView,mixins.UpdateModelMixin):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer

class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_class = (IsOwerOrReadOnly,)  # 进过认正以后的用户进行相关的操作

    #
    # def get(self,request,*args,**kwargs):
    #     return self.retrieve(request,*args,**kwargs)
    #
    # def put(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)
    #
    # def delete(self,request,*args,**kwargs):
    #     return self.destroy(request,*args,**kwargs)
# import json
# from rest_framework.views import APIView
# from .models import Publisher
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import PublisherSerializer#序列化
#
# class PublisherList(APIView):
#     """
#     获取一个出版社信息提交一个新的出版社
#
#     """
#     def get(self,request,*args,**kwargs):
#         queryset = Publisher.objects.all()
#         s = PublisherSerializer(queryset,many=True)#序列
#         return Response(s.data,status=status.HTTP_200_OK)
#
#
#     def post(self,request,*args,**kwargs):
#         s = PublisherSerializer(data=request.data)#反序列化
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class PublisherDetail(APIView):
#     """
#     获取单个 修改 删除 单个出版社
#
#     """
#
#     def get_obj(self,pk):
#         #新区数据库找用户要获取删除 修改的 那个出版社
#         pub_obj = Publisher.objects.filter(pk=pk)
#         if pub_obj is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             return pub_obj
#
#
#     def get(self,request,pk,*args,**kwargs):
#         pub_obj = self.get_obj(pk)
#         s = PublisherSerializer(pub_obj,many=True)
#         return Response(s.data,status=status.HTTP_200_OK)
#
#
#
#     def put(self,request,pk,*args,**kwargs):
#         pub_obj = self.get_obj(pk)
#         s = PublisherSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,*args,**kwargs):
#         pub_obj = self.get_obj(pk=pk)
#         pub_obj.delete()
#         return Response(status=status.HTTP_200_OK)



# from .models import Publisher#模型类
# from .serializers import PublisherSerializer#序列化
# from rest_framework.response import Response#响应
# from rest_framework.decorators import api_view#drf请求
# from rest_framework import status#drf提供的常用
# """
# 需要，获取一个出版社的信息，提交一个新的出版社
# """
# @api_view(["GET","POST"])
# def publisher_list(request):
#     if request.method == "GET":
#         """GET"""
#         queryset = Publisher.objects.all()
#         s = PublisherSerializer(queryset,many=True)
#         return Response(s.data)
#
#     if request.method =="POST":
#         pass
#         s = PublisherSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(["GET","DELETE","PUT"])
# def publisher_detial(request,pk):
#     publisher = Publisher.objects.filter(pk=int(pk)).first()#返回列表
#     if publisher is None:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
#     if request.method == "GET":
#         """
#         获取当前出版社
#         """
#         s = PublisherSerializer(publisher,many=False)
#         return Response(s.data,status=status.HTTP_200_OK)
#
#     if request.method == "PUT":
#         """
#         对某个进行修改
#         """
#         #反序列化  穿两个参数 publisher
#         s = PublisherSerializer(publisher,data = request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#     if request.method == "DELETE":
#         publisher.delete()
#         return Response(status=status.HTTP_200_OK)
#
#


