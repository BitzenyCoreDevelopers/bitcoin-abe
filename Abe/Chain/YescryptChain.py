from . import BaseChain
import zny_yescrypt
import binascii


class YescryptChain(BaseChain):
    def block_header_hash(chain, header):
        return zny_yescrypt.getPoWHash(header)
