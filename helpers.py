from os.path import abspath, dirname, join, exists

__ROOT__ = dirname(abspath(__file__))


def get_ss7_attacks_dos_prgms_payload(): return join(__ROOT__, 'ss7', 'attacks', 'dos', 'prgms', 'PurgeMS.jar')
def get_ss7_attacks_fraud_cl_payload(): return join(__ROOT__, 'ss7', 'attacks', 'fraud', 'cl', 'CancelLocation.jar')
def get_ss7_attacks_fraud_mtsms_payload(): return join(__ROOT__, 'ss7', 'attacks', 'fraud', 'mtsms', 'MTForwardSMS.jar')
def get_ss7_attacks_fraud_simsi_payload(): return join(__ROOT__, 'ss7', 'attacks', 'fraud', 'simsi', 'SendIMSI.jar')
def get_ss7_attacks_interception_ul_payload(): return join(__ROOT__, 'ss7', 'attacks', 'interception', 'ul', 'UpdateLocation.jar')
def get_ss7_attacks_tracking_ati_payload(): return join(__ROOT__, 'ss7', 'attacks', 'tracking', 'ati', 'AnyTimeInterrogation.jar')
def get_ss7_attacks_tracking_psi_payload(): return join(__ROOT__, 'ss7', 'attacks', 'tracking', 'psi', 'ProvideSubscriberInfo.jar')
def get_ss7_attacks_tracking_sri_payload(): return join(__ROOT__, 'ss7', 'attacks', 'tracking', 'sri', 'SendRoutingInfo.jar')
def get_ss7_attacks_tracking_srism_payload(): return join(__ROOT__, 'ss7', 'attacks', 'tracking', 'srism', 'SendRoutingInfoForSM.jar')


if __name__ == '__main__':
    assert exists(get_ss7_attacks_tracking_srism_payload())
    assert exists(get_ss7_attacks_tracking_sri_payload())
    assert exists(get_ss7_attacks_tracking_psi_payload())
    assert exists(get_ss7_attacks_tracking_ati_payload())
    assert exists(get_ss7_attacks_fraud_cl_payload())
    assert exists(get_ss7_attacks_fraud_mtsms_payload())
    assert exists(get_ss7_attacks_fraud_simsi_payload())
    assert exists(get_ss7_attacks_interception_ul_payload())
    assert exists(get_ss7_attacks_dos_prgms_payload())
