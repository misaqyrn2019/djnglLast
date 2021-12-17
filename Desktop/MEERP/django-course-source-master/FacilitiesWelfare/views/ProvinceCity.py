from .models import (
    Storeroom,GroupCommodity,CategoryCommodity,UnitPack,Supplier,UnitofMeasurement,
    Commodity,GroupCommodity,UnitPack,Customer,drivers,EntryCommodity,Transportation,
    productRepaired,TransfersbetweenStoreroom,Receipt,SettlementArrived,PurchaseRequest
    )

from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import City,Province

class CityList(APIView):
    def get(self,request, format=None):
        Data = []
        NData = []
        StoreroomOne = Storeroom.objects.all()
        for item in StoreroomOne:
            COM = Commodity.objects.filter(IdStoreroom=item.Id)
            DataPrice = []
            NData.append(item.Name)
            for i in COM:
                DataPrice.append(i.amount)
            SumPrice = sum(DataPrice)
            Data.append(SumPrice)
        Dict = {"Name":NData,
                "Price":Data}
        return Response(Dict)