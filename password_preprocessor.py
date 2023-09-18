import json

def pattern_calc(pswd: str) -> tuple[int, int]:
    KEYBOARD_LAYOUT = {}
    with open("./kb_data.json", 'r') as kb_data_cnfg:
        KEYBOARD_LAYOUT = json.load(kb_data_cnfg) 
    with open("./weights.json", 'r') as weights_config:
        diff_weight, diff_bios,\
        smbls_weight, smbls_bios,\
        kbrd_weight, kbrd_bios = map(float, json.load(weights_config))

    patt_of_diff_cache = {}
    patt_of_smbls_cache = {}
    patt_of_rev_smbls_cache = {}
    patt_of_kbrd_cache = {}


    for patt_len in range(1, len(pswd) // 2):
        for patt_start_index in range(len(pswd) - patt_len):
            patt_of_smbls = pswd[patt_start_index:patt_start_index + patt_len]
            kbrd_data_patt = [KEYBOARD_LAYOUT.get(char.lower()) for char in patt_of_smbls]
            if not(patt_of_smbls in patt_of_smbls_cache.keys() and patt_of_smbls in patt_of_rev_smbls_cache.keys()):
                patt_of_rev_smbls_cache[patt_of_smbls], patt_of_smbls_cache[patt_of_smbls] =\
                    pswd.count(patt_of_smbls[::-1]) - 1 if patt_of_smbls[::-1] in pswd else 0, pswd.count(patt_of_smbls) - 1    
            diff_patt = sum([abs(ord(patt_of_smbls[part_index]) - ord(patt_of_smbls[part_index + 1]))
                                                          for part_index in range(len(patt_of_smbls) - 1)])
            if diff_patt not in patt_of_diff_cache.keys():
                patt_of_diff_cache[diff_patt] = 0
            else:
                patt_of_diff_cache[diff_patt] += 1

            for start_char_index in range(len(patt_of_smbls)):
                for end_char_index in range(len(patt_of_smbls), start_char_index, -1):
                    for pos_data in kbrd_data_patt[start_char_index:end_char_index]:
                        for new_pos_data in kbrd_data_patt[start_char_index:end_char_index]:
                            try: 
                                possible_patt = sum([sum([round(((pos[0] - pos2[0]) ** 2 + (pos[1] - pos2[1]) ** 2) ** 0.5, 1)
                                                        for pos2 in new_pos_data]) // len(new_pos_data) for pos in pos_data]) // len(pos_data)
                            except TypeError: 
                                possible_patt = -1
                        if possible_patt in patt_of_kbrd_cache.keys():
                            patt_of_kbrd_cache[possible_patt] += 1
                        patt_of_kbrd_cache[possible_patt] = 0
                            

    diff_coef = (sum([key * value for key, value in patt_of_diff_cache.items()]) + diff_bios) * diff_weight
    smbl_coef = smbls_bios
    for key, value in patt_of_smbls_cache.items():
        if key[::-1] in patt_of_rev_smbls_cache:
            value += patt_of_rev_smbls_cache[key[::-1]]
        smbl_coef += value / len(patt_of_rev_smbls_cache)
    smbl_coef *= smbls_weight
    smbl_coef += (sum([value * key / len(patt_of_kbrd_cache) for key, value in patt_of_kbrd_cache.items()]) + kbrd_bios) * kbrd_weight
    return (diff_coef, smbl_coef)

def analyse(pswd: str) -> tuple[int, int, int]:
    try:
        res_classic = (len(pswd), *pattern_calc(pswd))
        return res_classic
    except ValueError as e:
        print(e, pswd)
    return (0, 0, 0)