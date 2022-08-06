from fastapi import APIRouter, HTTPException, status, Request
from app.utils.mktik import * # get_mk_address_list, add_mk_ip_to_address_list, del_mk_address_list_by_ip
from app.schemas.mk_schemas import PostResponse, AddrList, Message
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def health_check(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})
    # return {"Hello": "World"}


@router.get("/addr_lst", response_model=Message,
            responses={400:{"model":Message}})
async def get_addr_lst(filter_list: str = ""):
    resp = get_mk_address_list(filter_list)
    if resp.code == 400:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=resp.message)
    return resp


@router.get("/dhcp_leases", response_model=Message,
            responses={400:{"model":Message}})
async def get_dhcp_leases(filter_address: str = ""):
    resp = get_mk_dhcp_leases(filter_address)
    if resp.code == 400:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=resp.message)
    return resp


##########################################################################################################


@router.post("/addr_lst", response_model=PostResponse, status_code=status.HTTP_201_CREATED,
             responses={404: {"model": Message}, 400: {"model": Message}})
async def post_addr_lst(addr_lst: AddrList):
    resp = add_mk_ip_to_address_list(addr_lst)
    if resp.get('code') == 400:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=resp.get('message'))
    return resp

