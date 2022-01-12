from django.urls import path
from .views import *

app_name = "inventory"
urlpatterns = [
	path('d', CommodityPriceByStoreroom.as_view(), name="d"),
	path('d1', PurchaseBuyNPriceByStoreroom.as_view(), name="d1"),
	path('d2', PurchaseBuyYPriceByStoreroom.as_view(), name="d2"),
	
	path('Dashboard', Dashboard.as_view(), name="Dashboard"),

	path('homeSL', StoreroomList.as_view(), name="homeSL"),
	path('inventory/Create', StoreroomCreate.as_view(), name="Create"),
	path('inventory/delete/<int:pk>', StoreroomDelete.as_view(), name="Storeroom-Delete"),
	path('inventory/update/<int:pk>', StoreroomUpdate.as_view(), name="Storeroom-update"),
	path('StoreroomListReport/<int:IdStoreroom>',StoreroomListReport.as_view(),name="StoreroomListReport"),
	path('APIStoreroomListCreate',APIStoreroomCreate.as_view(),name="APIStoreroomListCreate"),
	
	path('homeGC', GroupCommodityList.as_view(), name="homeGC"),
	path('GroupCommodity/Create', GroupCommodityCreate.as_view(), name="GroupCommodity-Create"),
	path('GroupCommodity/delete/<int:pk>', GroupCommodityDelete.as_view(), name="GroupCommodity-Delete"),
	path('GroupCommodity/update/<int:pk>', GroupCommodityUpdate.as_view(), name="GroupCommodity-update"),
	path('APIGroupCommodityCreate', APIGroupCommodityCreate.as_view(), name="APIGroupCommodityCreate"),

	path('homeCC', CategoryCommodityList.as_view(), name="homeCC"),
	path('CategoryCommodity/Create', CategoryCommodityCreate.as_view(), name="CategoryCommodity-Create"),
	path('CategoryCommodity/delete/<int:pk>', CategoryCommodityDelete.as_view(), name="CategoryCommodity-Delete"),
	path('CategoryCommodity/update/<int:pk>', CategoryCommodityUpdate.as_view(), name="CategoryCommodity-update"),
	path('APICategoryCommodityCreate', APICategoryCommodityCreate.as_view(), name="APICategoryCommodityCreate"),
	

	path('homeUP', UnitPackList.as_view(), name="homeUP"),
	path('UnitPack/Create', UnitPackCreate.as_view(), name="UnitPack-Create"),
	path('UnitPack/delete/<int:pk>', UnitPackDelete.as_view(), name="UnitPack-Delete"),
	path('UnitPack/update/<int:pk>', UnitPackUpdate.as_view(), name="UnitPack-update"),
	path('APIUnitPackCreate', APIUnitPackCreate.as_view(), name="APIUnitPackCreate"),

	path('homeSU', SupplierList.as_view(), name="homeSU"),
	path('Supplier/Create', SupplierCreate.as_view(), name="Supplier-Create"),
	path('Supplier/delete/<int:pk>', SupplierDelete.as_view(), name="Supplier-Delete"),
	path('Supplier/update/<int:pk>', SupplierUpdate.as_view(), name="Supplier-update"),
	path('SupplierListReport/<int:IdSupplier>',SupplierListReport.as_view(),name="SupplierListReport"),
	path('APISupplierCreate',APISupplierCreate.as_view(),name="APISupplierCreate"),

	path('homeUM', UnitofMeasurementList.as_view(), name="homeUM"),
	path('UnitofMeasurement/Create', UnitofMeasurementCreate.as_view(), name="UnitofMeasurement-Create"),
	path('UnitofMeasurement/delete/<int:pk>', UnitofMeasurementDelete.as_view(), name="UnitofMeasurement-Delete"),
	path('UnitofMeasurement/update/<int:pk>', UnitofMeasurementUpdate.as_view(), name="UnitofMeasurement-update"),
	path('APIUnitofMeasurementCreate', APIUnitofMeasurementCreate.as_view(), name="APIUnitofMeasurementCreate"),

	path('homeCO', CommodityList.as_view(), name="homeCO"),
	path('Commodity/Create', CommodityCreate.as_view(), name="Commodity-Create"),
	path('Commodity/delete/<int:pk>', CommodityDelete.as_view(), name="Commodity-Delete"),
	path('Commodity/update/<int:pk>', CommodityUpdate.as_view(), name="Commodity-update"),
	path('CommodityListReport/<int:IdCommodity>', CommodityListReport.as_view(), name="Commodity-Report"),
	path('CommodityAllListReport/', CommodityAllListReport.as_view(), name="CommodityAll-Report"),
	path('APICommodityCreate', APICommodityCreate.as_view(), name="APICommodityCreate"),

	path('homeCU', CustomerList.as_view(), name="homeCU"),
	path('Customer/Create', CustomerCreate.as_view(), name="Customer-Create"),
	path('Customer/delete/<int:pk>', CustomerDelete.as_view(), name="Customer-Delete"),
	path('Customer/update/<int:pk>', CustomerUpdate.as_view(), name="Customer-update"),
	path('CustomerReport/', CustomerListReport.as_view(), name="Customer-Report"),

	path('homeDL', driversList.as_view(), name="homeDL"),
	path('drivers/Create', driversCreate.as_view(), name="drivers-Create"),
	path('drivers/delete/<int:pk>', driversDelete.as_view(), name="drivers-Delete"),
	path('drivers/update/<int:pk>', driversUpdate.as_view(), name="drivers-update"),
	path('DriversReport', DriversReport.as_view(), name="Drivers-Report"),

	path('homeEC', EntryCommodityList.as_view(), name="homeEC"),
	path('EntryCommodity/Create', EntryCommodityCreate.as_view(), name="EntryCommodity-Create"),
	path('EntryCommodity/delete/<int:pk>', EntryCommodityDelete.as_view(), name="EntryCommodity-Delete"),
	path('EntryCommodity/update/<int:pk>', EntryCommodityUpdate.as_view(), name="EntryCommodity-update"),
	path('EntryCommodityReport/<int:IdStoreroom>/<int:Type>', EntryCommodityReport.as_view(), name="EntryCommodity-Report"),

	path('homeTP', TransportationList.as_view(), name="homeTP"),
	path('Transportation/Create', TransportationCreate.as_view(), name="Transportation-Create"),
	path('Transportation/delete/<int:pk>', TransportationDelete.as_view(), name="Transportation-Delete"),
	path('Transportation/update/<int:pk>', TransportationUpdate.as_view(), name="Transportation-update"),

	path('homePR', ProductRepairedList.as_view(), name="homePR"),
	path('productRepaired/Create', ProductRepairedCreate.as_view(), name="productRepaired-Create"),
	path('productRepaired/delete/<int:pk>', ProductRepairedDelete.as_view(), name="productRepaired-Delete"),
	path('productRepaired/update/<int:pk>', ProductRepairedUpdate.as_view(), name="productRepaired-update"),
	path('ProductPerStoreroom/<int:IdStoreroom>', ProductPerStoreroom.as_view(), name="ProductPerStoreroom-Report"),

	path('homeRE', ReceiptList.as_view(), name="homeRE"),
	path('Receipt/Create', ReceiptCreate.as_view(), name="Receipt-Create"),
	path('Receipt/delete/<int:pk>', ReceiptDelete.as_view(), name="Receipt-Delete"),
	path('Receipt/update/<int:pk>', ReceiptUpdate.as_view(), name="Receipt-update"),
	path('ReportBuy', ReceiptReportBuy.as_view(), name="Receipt-ReportBuy"),
	path('ReportSale', ReceiptReportSale.as_view(), name="Receipt-ReportSale"),
	path('ReportStoreroomBuy/<int:IdStoreroom>', ReceiptReportStoreroomBuy.as_view(), name="Receipt-ReportStoreroomBuy"),
	path('ReportStoreroomSale/<int:IdStoreroom>', ReceiptReportStoreroomSale.as_view(), name="Receipt-ReportStoreroomSale"),
	

	path('homeSA', SettlementArrivedList.as_view(), name="homeSA"),
	path('SettlementArrived/Create', SettlementArrivedCreate.as_view(), name="SettlementArrived-Create"),
	path('SettlementArrived/delete/<int:pk>', SettlementArrivedDelete.as_view(), name="SettlementArrived-Delete"),
	path('SettlementArrived/update/<int:pk>', SettlementArrivedUpdate.as_view(), name="SettlementArrived-update"),

	path('homePPR', PurchaseRequestList.as_view(), name="homePPR"),
	path('PurchaseRequest/Create', PurchaseRequestCreate.as_view(), name="PurchaseRequest-Create"),
	path('PurchaseRequest/delete/<int:pk>', PurchaseRequestDelete.as_view(), name="PurchaseRequest-Delete"),
	path('PurchaseRequest/update/<int:pk>', PurchaseRequestUpdate.as_view(), name="PurchaseRequest-update"),
	path('PurchaseRequest/<int:IdCommodity>', PurchaseRequestListReport.as_view(), name="PurchaseRequest-Report"),
	path('PurchaseRequestSR/<int:IdStoreroom>', PurchaseRequestListSRReport.as_view(), name="PurchaseRequestSR-Report"),
]