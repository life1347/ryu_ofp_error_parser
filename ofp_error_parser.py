# all following information come from OpenFlow Spec v1.3
# https://www.opennetworking.org/images/stories/downloads/sdn-resources/onf-specifications/openflow/openflow-spec-v1.3.0.pdf

OFPET_HELLO_FAILED = {
    0: 'OFPHFC_INCOMPATIBLE, No compatible version.',
    1: 'OFPHFC_EPERM, Permissions error.'
}


OFPET_BAD_REQUEST = {
    0: 'OFPBRC_BAD_VERSION, ofp_header.version not supported.',
    1: 'OFPBRC_BAD_TYPE, ofp_header.type not supported.',
    2: 'OFPBRC_BAD_MULTIPART, ofp_multipart_request.type not supported.',
    3: 'OFPBRC_BAD_EXPERIMENTER, Experimenter id not supported.',
    4: 'OFPBRC_BAD_EXP_TYPE, Experimenter type not supported.',
    5: 'OFPBRC_EPERM, Permissions error.',
    6: 'OFPBRC_BAD_LEN, Wrong request length for type.',
    7: 'OFPBRC_BUFFER_EMPTY, Specified buffer has already been used.',
    8: 'OFPBRC_BUFFER_UNKNOWN, Specified buffer does not exist.',
    9: 'OFPBRC_BAD_TABLE_ID, Specified table-id invalid or does not exist.',
    10: 'OFPBRC_IS_SLAVE0, Denied because controller is slave.',
    11: 'OFPBRC_BAD_PORT, Invalid port.',
    12: 'OFPBRC_BAD_PACKET, Invalid packet in packet-out.',
    13: 'OFPBRC_MULTIPART_BUFFER_OVERFLOW, ofp_multipart_request overflowed the assigned buffer.'
}


OFPET_BAD_ACTION = {
    0: 'OFPBAC_BAD_TYPE, Unknown action type.',
    1: 'OFPBAC_BAD_LEN, Length problem in actions.',
    2: 'OFPBAC_BAD_EXPERIMENTER, Unknown experimenter id specified.',
    3: 'OFPBAC_BAD_EXP_TYPE, Unknown action for experimenter id.',
    4: 'OFPBAC_BAD_OUT_PORT, Problem validating output port.',
    5: 'OFPBAC_BAD_ARGUMENT, Bad action argument.',
    6: 'OFPBAC_EPERM, Permissions error.',
    7: 'OFPBAC_TOO_MANY, Can not handle this many actions.',
    8: 'OFPBAC_BAD_QUEUE, Problem validating output queue.',
    9: 'OFPBAC_BAD_OUT_GROUP, Invalid group id in forward action.',
    10: 'OFPBAC_MATCH_INCONSISTENT, Action can not apply for this match, or Set-Field missing prerequisite.',
    11: 'OFPBAC_UNSUPPORTED_ORDER, Action order is unsupported for the action list in an Apply-Actions instruction.',
    12: 'OFPBAC_BAD_TAG, Actions uses an unsupported tag / encap.',
    13: 'OFPBAC_BAD_SET_TYPE, Unsupported type in SET_FIELD action.',
    14: 'OFPBAC_BAD_SET_LEN, Length problem in SET_FIELD action.',
    15: 'OFPBAC_BAD_SET_ARGUMENT, Bad argument in SET_FIELD action.'
}


OFPET_BAD_INSTRUCTION = {
    0: 'OFPBIC_UNKNOWN_INST: Unknown instruction.',
    1: 'OFPBIC_UNSUP_INST: Switch or table does not support the instruction.',
    2: 'OFPBIC_BAD_TABLE_ID: Invalid Table-ID specified.',
    3: 'OFPBIC_UNSUP_METADATA: Metadata value unsupported by datapath.',
    4: 'OFPBIC_UNSUP_METADATA_MASK: Metadata mask value unsupported by datapath.',
    5: 'OFPBIC_BAD_EXPERIMENTER: Unknown experimenter id specified.',
    6: 'OFPBIC_BAD_EXP_TYPE: Unknown instruction for experimenter id.',
    7: 'OFPBIC_BAD_LEN: Length problem in instructions.',
    8: 'OFPBIC_EPERM: Permissions error.'
}


OFPET_BAD_MATCH = {
    0: 'OFPBMC_BAD_TYPE: Unsupported match type specified by the match',
    1: 'OFPBMC_BAD_LEN: Length problem in match.',
    2: 'OFPBMC_BAD_TAG: Match uses an unsupported tag / encap.',
    3: 'OFPBMC_BAD_DL_ADDR_MASK: Unsupported datalink addr mask - switch does not support arbitrary datalink address mask. ',
    4: 'OFPBMC_BAD_NW_ADDR_MASK: Unsupported network addr mask - switch does not support arbitrary network address mask.',
    5: 'OFPBMC_BAD_WILDCARDS: Unsupported combination of fields masked or omitted in the match.',
    6: 'OFPBMC_BAD_FIELD: Unsupported field type in the match.',
    7: 'OFPBMC_BAD_VALUE: Unsupported value in a match field.',
    8: 'OFPBMC_BAD_MASK: Unsupported mask specified in the match, field is not dl-address or nw-address.',
    9: 'OFPBMC_BAD_PREREQ: A prerequisite was not met.',
    10: 'OFPBMC_DUP_FIELD: A field type was duplicated.',
    11: 'OFPBMC_EPERM: Permissions error.'
}


OFPET_FLOW_MOD_FAILED = {
    0: 'OFPFMFC_UNKNOWN: Unspecified error.',
    1: 'OFPFMFC_TABLE_FULL: Flow not added because table was full.',
    2: 'OFPFMFC_BAD_TABLE_ID: Table does not exist',
    3: 'OFPFMFC_OVERLAP: Attempted to add overlapping flow with CHECK_OVERLAP flag set.',
    4: 'OFPFMFC_EPERM: Permissions error.',
    5: 'OFPFMFC_BAD_TIMEOUT Flow not added because of unsupported idle / hard timeout.',
    6: 'OFPFMFC_BAD_COMMAND: Unsupported or unknown command.',
    7: 'OFPFMFC_BAD_FLAGS: Unsupported or unknown flags.'
}


OFPET_GROUP_MOD_FAILED = {
    0: 'OFPGMFC_GROUP_EXISTS: Group not added because a group ADD attempted to replace an already-present group.',
    1: 'OFPGMFC_INVALID_GROUP: Group not added because Group specified is invalid.',
    2: 'OFPGMFC_WEIGHT_UNSUPPORTED: Switch does not support unequal load sharing with select groups.',
    3: 'OFPGMFC_OUT_OF_GROUPS: The group table is full.',
    4: 'OFPGMFC_OUT_OF_BUCKETS: The maximum number of action buckets for a group has been exceeded.',
    5: 'OFPGMFC_CHAINING_UNSUPPORTED: Switch does not support groups that forward to groups.',
    6: 'OFPGMFC_WATCH_UNSUPPORTED: This group can not watch the watch_port or watch_group specified.',
    7: 'OFPGMFC_LOOP: Group entry would cause a loop.',
    8: 'OFPGMFC_UNKNOWN_GROUP: Group not modified because a group MODIFY attempted to modify a non-existent group.',
    9: 'OFPGMFC_CHAINED_GROUP: Group not deleted because another group is forwarding to it.',
    10: 'OFPGMFC_BAD_TYPE: Unsupported or unknown group type.',
    11: 'OFPGMFC_BAD_COMMAND: Unsupported or unknown command.',
    12: 'OFPGMFC_BAD_BUCKET: Error in bucket.',
    13: 'OFPGMFC_BAD_WATCH: Error in watch port / group.',
    14: 'OFPGMFC_EPERM: Permissions error.'
}


OFPET_PORT_MOD_FAILED = {
    0: 'OFPPMFC_BAD_PORT, Specified port number does not exist.',
    1: 'OFPPMFC_BAD_HW_ADDR, Specified hardware address does not match the port number.',
    2: 'OFPPMFC_BAD_CONFIG, Specified config is invalid.',
    3: 'OFPPMFC_BAD_ADVERTISE, Specified advertise is invalid.',
    4: 'OFPPMFC_EPERM, Permissions error.'
}


OFPET_TABLE_MOD_FAILED = {
    0: 'OFPTMFC_BAD_TABLE, Specified table does not exist.',
    1: 'OFPTMFC_BAD_CONFIG, Specified config is invalid.',
    2: 'OFPTMFC_EPERM, Permissions error.'
}


OFPET_QUEUE_OP_FAILED = {
    0: 'OFPQOFC_BAD_PORT, Invalid port (or port does not exist).',
    1: 'OFPQOFC_BAD_QUEUE, Queue does not exist.',
    2: 'OFPQOFC_EPERM, Permissions error.'
}


OFPET_SWITCH_CONFIG_FAILED = {
    0: 'OFPSCFC_BAD_FLAGS, Specified flags is invalid.',
    1: 'OFPSCFC_BAD_LEN, Specified len is invalid.',
    2: 'OFPQCFC_EPERM, Permissions error.'
}


OFPET_ROLE_REQUEST_FAILED = {
    0: 'OFPRRFC_STALE, Stale Message: old generation_id.',
    1: 'OFPRRFC_UNSUP, Controller role change unsupported.',
    2: 'OFPRRFC_BAD_ROLE, Invalid role.'
}

OFPET_METER_MOD_FAILED = {
    0: 'OFPMMFC_UNKNOWN, Unspecified error.',
    1: 'OFPMMFC_METER_EXISTS, Meter not added because a Meter ADD attempted to replace an existing Meter.',
    2: 'OFPMMFC_INVALID_METER, Meter not added because Meter specified is invalid.',
    3: 'OFPMMFC_UNKNOWN_METER, Meter not modified because a Meter MODIFY attempted to modify a non-existent Meter.',
    4: 'OFPMMFC_BAD_COMMAND, Unsupported or unknown command.',
    5: 'OFPMMFC_BAD_FLAGS, Flag configuration unsupported.',
    6: 'OFPMMFC_BAD_RATE, Rate unsupported.',
    7: 'OFPMMFC_BAD_BURST, Burst size unsupported.',
    8: 'OFPMMFC_BAD_BAND, Band unsupported.',
    9: 'OFPMMFC_BAD_BAND_VALUE, Band value unsupported.',
    10: 'OFPMMFC_OUT_OF_METERS, No more meters available.',
    11: 'OFPMMFC_OUT_OF_BANDS, The maximum number of properties for a meter has been exceeded.'
}
OFPET_TABLE_FEATURES_FAILED = {
    0: 'OFPTFFC_BAD_TABLE, Specified table does not exist.',
    1: 'OFPTFFC_BAD_METADATA, Invalid metadata mask.',
    2: 'OFPTFFC_BAD_TYPE, Unknown property type.',
    3: 'OFPTFFC_BAD_LEN, Length problem in properties.',
    4: 'OFPTFFC_BAD_ARGUMENT, Unsupported property value.',
    5: 'OFPTFFC_EPERM, Permissions error.'
}


# OFPET_EXPERIMENTER = {}


of_error_msg = {
    0: ('OFPET_HELLO_FAILED', OFPET_HELLO_FAILED),
    1: ('OFPET_BAD_REQUEST', OFPET_BAD_REQUEST),
    2: ('OFPET_BAD_ACTION', OFPET_BAD_ACTION),
    3: ('OFPET_BAD_INSTRUCTION', OFPET_BAD_INSTRUCTION),
    4: ('OFPET_BAD_MATCH', OFPET_BAD_MATCH),
    5: ('OFPET_FLOW_MOD_FAILED', OFPET_FLOW_MOD_FAILED),
    6: ('OFPET_GROUP_MOD_FAILED', OFPET_GROUP_MOD_FAILED),
    7: ('OFPET_PORT_MOD_FAILED', OFPET_PORT_MOD_FAILED),
    8: ('OFPET_TABLE_MOD_FAILED', OFPET_TABLE_MOD_FAILED),
    9: ('OFPET_QUEUE_OP_FAILED', OFPET_QUEUE_OP_FAILED),
    10: ('OFPET_SWITCH_CONFIG_FAILED', OFPET_SWITCH_CONFIG_FAILED),
    11: ('OFPET_ROLE_REQUEST_FAILED', OFPET_ROLE_REQUEST_FAILED),
    12: ('OFPET_METER_MOD_FAILED', OFPET_METER_MOD_FAILED),
    13: ('OFPET_TABLE_FEATURES_FAILED', OFPET_TABLE_FEATURES_FAILED),
    # 65535: ('OFPET_EXPERIMENTER', OFPET_EXPERIMENTER)
}


def parse_ofp_err_msg(err_type, err_code):
    err_type, err_codes = of_error_msg.get(err_type)
    err_code = err_codes.get(err_code)
    return (err_type, err_code)

