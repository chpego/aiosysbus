class Connection:

    def __init__(self, access):
        self._access = access

    async def get_lan_luckyAddrAddress(self):
        ''' LAN IP Address '''
        return await self._access.post('NeMo.Intf.lan','luckyAddrAddress')

    async def get_data_luckyAddrAddress(self):
        ''' WAN IP Address '''
        return await self._access.post('NeMo.Intf.data','luckyAddrAddress')

    async def get_lo_DHCPOption(self,conf=None):
        ''' DHCP Option '''
        return await self._access.post('NeMo.Intf.lo','getDHCPOption',conf)

    async def get_dsl0_DSLStats(self,conf=None):
        ''' xDSLS Connection Statistics '''
        return await self._access.post('NeMo.Intf.dsl0','getDSLStats',conf)

    async def get_dsl0_MIBS(self,conf=None):
        ''' xDSLS information '''
        return await self._access.post('NeMo.Intf.dsl0','getMIBs',conf)

    async def get_data_MIBS(self,conf=None):
        '''
        All datas informations
        conf =  {"parameters":{"mibs":"dsl","traverse":"down"}}
        '''
        return await self._access.post('NeMo.Intf.data','getMIBs',conf)

    async def get_lan_MIBS(self,conf=None):
        ''' LAN Information '''
        return await self._access.post('NeMo.Intf.lan','getMIBs',conf)
