from collections import OrderedDict


CHAIN_IDS_TO_NAMES = OrderedDict([
  (1, 'sol'),
  (2, 'eth'),
  (3, 'terra'),
  (4, 'bsc'),
  (5, 'matic'),
  (6, 'avax'),
  (7, 'oasis'),
  (9, "safe")
])
CHAIN_NAMES_TO_IDS = OrderedDict([(v, k) for (k, v) in CHAIN_IDS_TO_NAMES.items()])

SOURCE_INFO = OrderedDict([
  ('sol', ('Solana', 'so', "https://solscan.io", "https://solscan.io/account/wormDTUJ6AWPNvk59vGQbDvGJmqbDTdgWgAqcLBCgUb")),
  ('eth', ('Ethereum', 'et', "https://etherscan.io", "https://etherscan.io/address/0x3ee18B2214AFF97000D974cf647E7C347E8fa585")),
  ('bsc', ('BSC', 'bs', "https://bscscan.com", "https://bscscan.com/address/0xB6F6D86a8f9879A9c87f643768d9efc38c1Da6E7")),
  ('terra', ('Terra', 'te', "https://finder.terra.money/columbus-5", "https://finder.terra.money/columbus-5/address/terra10nmmwe8r3g99a9newtqa7a75xfgs2e8z87r2sf")),
  ('matic', ('Polygon', 'po', "https://polygonscan.com", "https://polygonscan.com/address/0x5a58505a96d1dbf8df91cb21b54419fc36e93fde")),
  ('avax', ('Avalanche', 'av', "https://snowtrace.io", "https://snowtrace.io/address/0x0e082f06ff657d94310cb8ce8b0d9a04541d8052")),
  ('oasis', ('Oasis', 'oa', "https://explorer.oasis.updev.si", "https://explorer.oasis.updev.si/address/0x5848C791e09901b40A9Ef749f2a6735b418d7564")),
  ('safe', ('SafeCoin', 'sf', "https://safecoin.org", "https://explorer.safecoin.org/account/wormDTUJ6AWPNvk59vGQbDvGJmqbDTdgWgAqcLBCgUb")),
])

SUFFIXES = [x[1] for x in SOURCE_INFO.values()]
ABBREVS_TO_CHAINS = {y[1]: x for (x, y) in SOURCE_INFO.items()}