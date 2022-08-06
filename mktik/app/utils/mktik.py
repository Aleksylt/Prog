import routeros_api
from app.schemas.mk_schemas import AddrList, PostResponse, Message
from app.config import MKTIK_IP, MKTIK_PASS, MKTIK_USER
from routeros_api.exceptions import RouterOsApiConnectionError


def get_mk_address_list(filter_list: str = "") -> Message:
    connection = routeros_api.RouterOsApiPool(MKTIK_IP, username=MKTIK_USER, password=MKTIK_PASS,
                                              port=8728, plaintext_login=True)
    try:
        api = connection.get_api()
    except TypeError:
        resp = Message(
            code=400,
            message=["error connection to mikrotik"]
        )
        return resp
    except RouterOsApiConnectionError as err:
        resp = Message(
            code=400,
            message=["error : " + str(err)]
        )
        return resp

    try:
        list_address = api.get_resource('/ip/firewall/address-list/')
    except TypeError:
        resp = Message(
            code=400,
            message=["error get address list"]
        )
        return resp
    result = Message(
        code=200,
        message=[]
    )
    if filter_list == "":
        result.message=list(list_address.get())
    else:
        result.message=list(list_address.get(list=filter_list))

    connection.disconnect()
    return result


def get_mk_dhcp_leases(filter_address: str = "") -> Message:
    connection = routeros_api.RouterOsApiPool(MKTIK_IP, username=MKTIK_USER, password=MKTIK_PASS,
                                              port=8728, plaintext_login=True)
    try:
        api = connection.get_api()
    except TypeError:
        resp = Message(
            code=400,
            message=["error connection to mikrotik"]
        )
        return resp
    except RouterOsApiConnectionError as err:
        resp = Message(
            code=400,
            message=["error : " + str(err)]
        )
        return resp

    try:
        dhcp_leases = api.get_resource('/ip/dhcp-server/lease/')
    except TypeError:
        resp = Message(
            code=400,
            message=["error get leases"]
        )
        return resp
    result = Message(
        code=200,
        message=[]
    )
    if filter_address == "":
        result.message=list(dhcp_leases.get())
    else:
        result.message=list(dhcp_leases.get(address=filter_address))

    connection.disconnect()
    return result


def del_mk_address_list_by_ip():
    connection = routeros_api.RouterOsApiPool(MKTIK_IP, username=MKTIK_USER, password=MKTIK_PASS,
                                              port=8728, plaintext_login=True)

    try:
        api = connection.get_api()
    except TypeError:
        resp = {
            "code": 400,
            "message": "error connection to mikrotik"
        }
        return resp

    list_address = api.get_resource('/ip/firewall/address-list/')
    if list_address.get(address='192.168.88.88'):
        lst = list_address.get(address='192.168.88.88')
        for id_item in lst:
            list_address.remove(id=id_item['id'])
    connection.disconnect()


def add_mk_ip_to_address_list(addr_lst: AddrList):
    connection = routeros_api.RouterOsApiPool(MKTIK_IP, username=MKTIK_USER, password=MKTIK_PASS,
                                              port=8728, plaintext_login=True)
    try:
        api = connection.get_api()
    except TypeError:
        resp = {
            "code": 400,
            "message": "error connection to mikrotik"
        }
        return resp
    list_address = api.get_resource('/ip/firewall/address-list/')
    if not list_address.get(address=str(addr_lst.address), list=str(addr_lst.list)):

        list_address.add(list=str(addr_lst.list), address=str(addr_lst.address))

        connection.disconnect()

        resp = {'code': '201', 'msg': f'address {addr_lst.address} added to address list {addr_lst.list}'}
        return resp
    else:

        connection.disconnect()
        resp = {'code': 400, 'msg': f'address {addr_lst.address} already in address list {addr_lst.list}'}
        return resp


if __name__ == '__main__':
    # get_mk_address_list()
    # del_mk_address_list_by_ip()
    al = AddrList(address='10.10.1.1', list='lst')
    add_mk_ip_to_address_list(al)
