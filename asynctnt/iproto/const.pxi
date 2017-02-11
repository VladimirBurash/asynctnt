DEF _BUFFER_FREELIST_SIZE = 256
DEF _BUFFER_INITIAL_SIZE = 1024
DEF _BUFFER_MAX_GROW = 65536

DEF HEADER_CONST_LEN = 5 + 1 + 1 + 1 + 1 + 5 + 1 + 9  # pkt_len +
                                                      # mp_sizeof_map(2) +
                                                      # mp_sizeof_uint(TP_CODE) +
                                                      # mp_sizeof_uint(TP COMMAND) +
                                                      # mp_sizeof_uint(TP_SYNC) +
                                                      # sync len +
                                                      # mp_sizeof_uint(TP_SCHEMA_ID) +
                                                      # schema_id len

DEF IPROTO_GREETING_SIZE = 128
DEF TARANTOOL_VERSION_LENGTH = 64
DEF SALT_LENGTH = 44
DEF SCRAMBLE_SIZE = 20


DEF SPACE_VSPACE = 281
DEF SPACE_VINDEX = 289
