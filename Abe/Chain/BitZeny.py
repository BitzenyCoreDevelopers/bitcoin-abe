from .YescryptChain import YescryptChain

class BitZeny(YescryptChain):
    def __init__(chain, **kwargs):
        chain.name = 'BitZeny'
        chain.code3 = 'ZNY'
        chain.address_version = '\x51'
        chain.script_addr_vers = '\x05'
        chain.magic = '\xda\xa5\xbe\xf9'
        YescryptChain.__init__(chain, **kwargs)

    datadir_conf_file_name = "bitzeny.conf"
    datadir_rpcport = 9252
