#!/usr/bin/env python
# -*- coding: utf-8 -*-


import base58
import utils


OP_0 = chr(0)

ADDR_PREFIX = chr(55)
SCRIPT_PREFIX = chr(16)

ADDR_PREFIX_TEST = chr(140)
SCRIPT_PREFIX_TEST = chr(19)


# p2pkh
def pubkey_to_legacy_address(pubkey, main_net=True):
    pubkey = pubkey.decode("hex")

    addr_prefix = ADDR_PREFIX
    if not main_net:
        addr_prefix = ADDR_PREFIX_TEST

    h20 = utils.hash160(pubkey)
    d21 = addr_prefix + h20
    c4 = utils.checksum(d21)

    d25 = d21 + c4
    return base58.b58encode(d25)


# p2sh
def redeemscript_to_p2sh_address(redeem_script, main_net=True):
    redeem_script = redeem_script.decode("hex")

    script_prefix = SCRIPT_PREFIX
    if not main_net:
        script_prefix = SCRIPT_PREFIX_TEST

    h20 = utils.hash160(redeem_script)
    d21 = script_prefix + h20
    c4 = utils.checksum(d21)

    d25 = d21 + c4
    return base58.b58encode(d25)


def func_test():
    # txid:
    #
    print pubkey_to_legacy_address("")

    # txid:
    #
    print redeemscript_to_p2sh_address("")


if __name__ == "__main__":
    func_test()

