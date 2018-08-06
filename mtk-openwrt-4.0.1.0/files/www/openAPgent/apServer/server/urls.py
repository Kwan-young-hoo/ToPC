'''
This file was automatically generated by rmib_compiler.py.
DO NOT EDIT.
'''


from apServer.server import views
from common.generic_defs import CustomRouter

custom_router = CustomRouter()

custom_router.register(r'v1/infos/usages', views.SysetmUsageViewSet, base_name='system_usage')
custom_router.register(r'v1/configs/system', views.SysetmConfigViewSet, base_name='system_config')
custom_router.register(r'v1/configs/interfaces', views.InterfaceConfigViewSet, base_name='interface_config')
custom_router.register(r'v1/configs/vlans', views.VlanConfigViewSet, base_name='vlan_config')
custom_router.register(r'v1/configs/dhcp/common', views.DhcpCommonConfigViewSet, base_name='dhcp_common_config')
custom_router.register(r'v1/configs/dhcp/pools', views.DhcpPoolConfigViewSet, base_name='dhcp_pool_config')
custom_router.register(r'v1/configs/dhcp/static-leases', views.DhcpStaticLeasesConfigViewSet, base_name='dhcp_static_leases_config')
custom_router.register(r'v1/management/firmware', views.FirmwareMgtViewSet, base_name='firmware_management')
custom_router.register(r'v1/management/configuration', views.ConfigMgtViewSet, base_name='config_management')
custom_router.register(r'v1/statistics', views.IfStatisticsViewSet, base_name='if_statistics')