'''
This file was automatically generated by rmib_compiler.py.
 DO NOT EDIT.
'''


import json
from rest_framework import status, viewsets
from rest_framework.response import Response
from sal.sal import *
from common.log import *


'''
 Define Class SysetmUsage
'''
class SysetmUsageViewSet(viewsets.ViewSet):
  def list(self, request):
    log_info(LOG_MODULE_APSERVER, "*** SysetmUsage list() ***")
    data = sal_system_usage(SAL_METHOD_LIST, request.data, None)
    return Response(data, content_type='application/json')

  def retrieve(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** SysetmUsage retrieve(), pk = " + pk + " ***")
    data = sal_system_usage(SAL_METHOD_RETRIEVE, request.data, pk)
    return Response(data, content_type='application/json')


'''
 Define Class SysetmConfig
'''
class SysetmConfigViewSet(viewsets.ViewSet):
  def list(self, request):
    log_info(LOG_MODULE_APSERVER, "*** SysetmConfig list() ***")
    data = sal_system_config(SAL_METHOD_LIST, request.data, None)
    return Response(data, content_type='application/json')

  def create(self, request):
    log_info(LOG_MODULE_APSERVER, "*** SysetmConfig create() ***")
    data = sal_system_config(SAL_METHOD_CREATE, request.data, None)
    return Response(data, content_type='application/json')

  def update(self, request):
    log_info(LOG_MODULE_APSERVER, "*** SysetmConfig update() ***")
    data = sal_system_config(SAL_METHOD_UPDATE, request.data, None)
    return Response(data, content_type='application/json')

  def retrieve(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** SysetmConfig retrieve(), pk = " + pk + " ***")
    data = sal_system_config(SAL_METHOD_RETRIEVE, request.data, pk)
    return Response(data, content_type='application/json')

  def detail_create(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** SysetmConfig detail_create(), pk = " + pk + " ***")
    data = sal_system_config(SAL_METHOD_DETAIL_CREATE, request.data, pk)
    return Response(data, content_type='application/json')

  def detail_update(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** SysetmConfig detail_update(), pk = " + pk + " ***")
    data = sal_system_config(SAL_METHOD_DETAIL_UPDATE, request.data, pk)
    return Response(data, content_type='application/json')


'''
 Define Class InterfaceConfig
'''
class InterfaceConfigViewSet(viewsets.ViewSet):
  def list(self, request):
    log_info(LOG_MODULE_APSERVER, "*** InterfaceConfig list() ***")
    data = sal_interface_config(SAL_METHOD_LIST, request.data, None)
    return Response(data, content_type='application/json')

  def create(self, request):
    log_info(LOG_MODULE_APSERVER, "*** InterfaceConfig create() ***")
    data = sal_interface_config(SAL_METHOD_CREATE, request.data, None)
    return Response(data, content_type='application/json')

  def update(self, request):
    log_info(LOG_MODULE_APSERVER, "*** InterfaceConfig update() ***")
    data = sal_interface_config(SAL_METHOD_UPDATE, request.data, None)
    return Response(data, content_type='application/json')

  def retrieve(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** InterfaceConfig retrieve(), pk = " + pk + " ***")
    data = sal_interface_config(SAL_METHOD_RETRIEVE, request.data, pk)
    return Response(data, content_type='application/json')

  def detail_create(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** InterfaceConfig detail_create(), pk = " + pk + " ***")
    data = sal_interface_config(SAL_METHOD_DETAIL_CREATE, request.data, pk)
    return Response(data, content_type='application/json')

  def detail_update(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** InterfaceConfig detail_update(), pk = " + pk + " ***")
    data = sal_interface_config(SAL_METHOD_DETAIL_UPDATE, request.data, pk)
    return Response(data, content_type='application/json')


'''
 Define Class VlanConfig
'''
class VlanConfigViewSet(viewsets.ViewSet):
  def list(self, request):
    log_info(LOG_MODULE_APSERVER, "*** VlanConfig list() ***")
    data = sal_vlan_config(SAL_METHOD_LIST, request.data, None)
    return Response(data, content_type='application/json')

  def create(self, request):
    log_info(LOG_MODULE_APSERVER, "*** VlanConfig create() ***")
    data = sal_vlan_config(SAL_METHOD_CREATE, request.data, None)
    return Response(data, content_type='application/json')

  def update(self, request):
    log_info(LOG_MODULE_APSERVER, "*** VlanConfig update() ***")
    data = sal_vlan_config(SAL_METHOD_UPDATE, request.data, None)
    return Response(data, content_type='application/json')

  def retrieve(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** VlanConfig retrieve(), pk = " + pk + " ***")
    data = sal_vlan_config(SAL_METHOD_RETRIEVE, request.data, pk)
    return Response(data, content_type='application/json')

  def detail_create(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** VlanConfig detail_create(), pk = " + pk + " ***")
    data = sal_vlan_config(SAL_METHOD_DETAIL_CREATE, request.data, pk)
    return Response(data, content_type='application/json')

  def detail_update(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** VlanConfig detail_update(), pk = " + pk + " ***")
    data = sal_vlan_config(SAL_METHOD_DETAIL_UPDATE, request.data, pk)
    return Response(data, content_type='application/json')


'''
 Define Class DhcpCommonConfig
'''
class DhcpCommonConfigViewSet(viewsets.ViewSet):
  def list(self, request):
    log_info(LOG_MODULE_APSERVER, "*** DhcpCommonConfig list() ***")
    data = sal_dhcp_common_config(SAL_METHOD_LIST, request.data, None)
    return Response(data, content_type='application/json')

  def create(self, request):
    log_info(LOG_MODULE_APSERVER, "*** DhcpCommonConfig create() ***")
    data = sal_dhcp_common_config(SAL_METHOD_CREATE, request.data, None)
    return Response(data, content_type='application/json')

  def update(self, request):
    log_info(LOG_MODULE_APSERVER, "*** DhcpCommonConfig update() ***")
    data = sal_dhcp_common_config(SAL_METHOD_UPDATE, request.data, None)
    return Response(data, content_type='application/json')


'''
 Define Class DhcpPoolConfig
'''
class DhcpPoolConfigViewSet(viewsets.ViewSet):
  def list(self, request):
    log_info(LOG_MODULE_APSERVER, "*** DhcpPoolConfig list() ***")
    data = sal_dhcp_pool_config(SAL_METHOD_LIST, request.data, None)
    return Response(data, content_type='application/json')

  def create(self, request):
    log_info(LOG_MODULE_APSERVER, "*** DhcpPoolConfig create() ***")
    data = sal_dhcp_pool_config(SAL_METHOD_CREATE, request.data, None)
    return Response(data, content_type='application/json')

  def update(self, request):
    log_info(LOG_MODULE_APSERVER, "*** DhcpPoolConfig update() ***")
    data = sal_dhcp_pool_config(SAL_METHOD_UPDATE, request.data, None)
    return Response(data, content_type='application/json')

  def retrieve(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** DhcpPoolConfig retrieve(), pk = " + pk + " ***")
    data = sal_dhcp_pool_config(SAL_METHOD_RETRIEVE, request.data, pk)
    return Response(data, content_type='application/json')

  def detail_create(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** DhcpPoolConfig detail_create(), pk = " + pk + " ***")
    data = sal_dhcp_pool_config(SAL_METHOD_DETAIL_CREATE, request.data, pk)
    return Response(data, content_type='application/json')

  def detail_update(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** DhcpPoolConfig detail_update(), pk = " + pk + " ***")
    data = sal_dhcp_pool_config(SAL_METHOD_DETAIL_UPDATE, request.data, pk)
    return Response(data, content_type='application/json')


'''
 Define Class DhcpStaticLeasesConfig
'''
class DhcpStaticLeasesConfigViewSet(viewsets.ViewSet):
  def list(self, request):
    log_info(LOG_MODULE_APSERVER, "*** DhcpStaticLeasesConfig list() ***")
    data = sal_dhcp_static_leases_config(SAL_METHOD_LIST, request.data, None)
    return Response(data, content_type='application/json')

  def create(self, request):
    log_info(LOG_MODULE_APSERVER, "*** DhcpStaticLeasesConfig create() ***")
    data = sal_dhcp_static_leases_config(SAL_METHOD_CREATE, request.data, None)
    return Response(data, content_type='application/json')

  def update(self, request):
    log_info(LOG_MODULE_APSERVER, "*** DhcpStaticLeasesConfig update() ***")
    data = sal_dhcp_static_leases_config(SAL_METHOD_UPDATE, request.data, None)
    return Response(data, content_type='application/json')

  def retrieve(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** DhcpStaticLeasesConfig retrieve(), pk = " + pk + " ***")
    data = sal_dhcp_static_leases_config(SAL_METHOD_RETRIEVE, request.data, pk)
    return Response(data, content_type='application/json')

  def detail_create(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** DhcpStaticLeasesConfig detail_create(), pk = " + pk + " ***")
    data = sal_dhcp_static_leases_config(SAL_METHOD_DETAIL_CREATE, request.data, pk)
    return Response(data, content_type='application/json')

  def detail_update(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** DhcpStaticLeasesConfig detail_update(), pk = " + pk + " ***")
    data = sal_dhcp_static_leases_config(SAL_METHOD_DETAIL_UPDATE, request.data, pk)
    return Response(data, content_type='application/json')


'''
 Define Class FirmwareMgt
'''
class FirmwareMgtViewSet(viewsets.ViewSet):
  def list(self, request):
    log_info(LOG_MODULE_APSERVER, "*** FirmwareMgt list() ***")
    data = sal_firmware_management(SAL_METHOD_LIST, request.data, None)
    return Response(data, content_type='application/json')

  def create(self, request):
    log_info(LOG_MODULE_APSERVER, "*** FirmwareMgt create() ***")
    data = sal_firmware_management(SAL_METHOD_CREATE, request.data, None)
    return Response(data, content_type='application/json')


'''
 Define Class ConfigMgt
'''
class ConfigMgtViewSet(viewsets.ViewSet):
  def list(self, request):
    log_info(LOG_MODULE_APSERVER, "*** ConfigMgt list() ***")
    data = sal_config_management(SAL_METHOD_LIST, request.data, None)
    return Response(data, content_type='application/json')

  def create(self, request):
    log_info(LOG_MODULE_APSERVER, "*** ConfigMgt create() ***")
    data = sal_config_management(SAL_METHOD_CREATE, request.data, None)
    return Response(data, content_type='application/json')


'''
 Define Class IfStatistics
'''
class IfStatisticsViewSet(viewsets.ViewSet):
  def list(self, request):
    log_info(LOG_MODULE_APSERVER, "*** IfStatistics list() ***")
    data = sal_if_statistics(SAL_METHOD_LIST, request.data, None)
    return Response(data, content_type='application/json')

  def retrieve(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** IfStatistics retrieve(), pk = " + pk + " ***")
    data = sal_if_statistics(SAL_METHOD_RETRIEVE, request.data, pk)
    return Response(data, content_type='application/json')


'''
 Define Class DockerImages
'''
class DockerImagesViewSet(viewsets.ViewSet):
  def list(self, request):
    log_info(LOG_MODULE_APSERVER, "*** DockerImages list() ***")
    data = sal_docker_images(SAL_METHOD_LIST, request.data, None)
    return Response(data, content_type='application/json')

  def retrieve(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** DockerImages retrieve(), pk = " + pk + " ***")
    data = sal_docker_images(SAL_METHOD_RETRIEVE, request.data, pk)
    return Response(data, content_type='application/json')

  def create(self, request):
    log_info(LOG_MODULE_APSERVER, "*** DockerImages create() ***")
    data = sal_docker_images(SAL_METHOD_CREATE, request.data, None)
    return Response(data, content_type='application/json')

  def detail_create(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** DockerImages detail_create(), pk = " + pk + " ***")
    data = sal_docker_images(SAL_METHOD_DETAIL_CREATE, request.data, pk)
    return Response(data, content_type='application/json')

  def destroy(self, request):
    log_info(LOG_MODULE_APSERVER, "*** DockerImages destroy() ***")
    data = sal_docker_images(SAL_METHOD_DESTROY, request.data, None)
    return Response(data, content_type='application/json')

  def detail_destroy(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** DockerImages detail_destroy(), pk = " + pk + " ***")
    data = sal_docker_images(SAL_METHOD_DETAIL_DESTROY, request.data, pk)
    return Response(data, content_type='application/json')


'''
 Define Class ContainerCreation
'''
class ContainerCreationViewSet(viewsets.ViewSet):
  def create(self, request):
    log_info(LOG_MODULE_APSERVER, "*** ContainerCreation create() ***")
    data = sal_container_creation(SAL_METHOD_CREATE, request.data, None)
    return Response(data, content_type='application/json')

  def detail_create(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** ContainerCreation detail_create(), pk = " + pk + " ***")
    data = sal_container_creation(SAL_METHOD_DETAIL_CREATE, request.data, pk)
    return Response(data, content_type='application/json')


'''
 Define Class ContainerGet
'''
class ContainerGetViewSet(viewsets.ViewSet):
  def list(self, request):
    log_info(LOG_MODULE_APSERVER, "*** ContainerGet list() ***")
    data = sal_container_get(SAL_METHOD_LIST, request.data, None)
    return Response(data, content_type='application/json')

  def retrieve(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** ContainerGet retrieve(), pk = " + pk + " ***")
    data = sal_container_get(SAL_METHOD_RETRIEVE, request.data, pk)
    return Response(data, content_type='application/json')


'''
 Define Class ContainerManagement
'''
class ContainerManagementViewSet(viewsets.ViewSet):
  def create(self, request):
    log_info(LOG_MODULE_APSERVER, "*** ContainerManagement create() ***")
    data = sal_container_management(SAL_METHOD_CREATE, request.data, None)
    return Response(data, content_type='application/json')

  def detail_create(self, request, pk):
    log_info(LOG_MODULE_APSERVER, "*** ContainerManagement detail_create(), pk = " + pk + " ***")
    data = sal_container_management(SAL_METHOD_DETAIL_CREATE, request.data, pk)
    return Response(data, content_type='application/json')

