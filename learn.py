import json

def pattern_calc(pswd: str) -> tuple[int, int]:
    KEYBOARD_LAYOUT = {}
    with open("./kb_data.json", 'r') as kb_data_cnfg:
        KEYBOARD_LAYOUT = json.load(kb_data_cnfg) 
    patt_of_diff_cache = {}
    patt_of_smbls_cache = {}
    patt_of_rev_smbls_cache = {}
    patt_of_kbrd_cache = {}


    def smbls_calc(smbls_data_patt: str, kbrd_data_patt: list, patt_length: int) -> None:
        if smbls_data_patt in patt_of_smbls_cache.keys() and smbls_data_patt in patt_of_rev_smbls_cache.keys():
            return
        patt_of_rev_smbls_cache[smbls_data_patt], patt_of_smbls_cache[smbls_data_patt] =\
              pswd.count(smbls_data_patt[::-1]) - 1 if smbls_data_patt[::-1] in pswd else 0, pswd.count(smbls_data_patt) - 1    

        for start_char_index in range(patt_length):
            for end_char_index in range(patt_length, start_char_index, -1):
                for pos_data in kbrd_data_patt[start_char_index:end_char_index]:
                    for new_pos_data in kbrd_data_patt[start_char_index:end_char_index]:
                        possible_patt = sum([sum([round(((pos[0] - pos2[0]) ** 2 + (pos[1] - pos2[1]) ** 2) ** 0.5, 1)
                                                   for pos2 in new_pos_data]) // len(new_pos_data) for pos in pos_data]) // len(pos_data)
                    if possible_patt in patt_of_kbrd_cache.keys():
                        patt_of_kbrd_cache[possible_patt] += 1
                    patt_of_kbrd_cache[possible_patt] = 0


    for patt_len in range(1, len(pswd) // 2):
        for patt_start_index in range(len(pswd) - patt_len):
            patt_of_smbls = pswd[patt_start_index:patt_start_index + patt_len]
            smbls_calc(patt_of_smbls, [KEYBOARD_LAYOUT[char.lower()] for char in patt_of_smbls], len(patt_of_smbls))
    print(patt_of_diff_cache, patt_of_smbls_cache, patt_of_rev_smbls_cache, patt_of_kbrd_cache)

    return 0, 0

def analyse(pswd: str) -> tuple[int, int, int]:
    import time
    st1 = time.time()
    res_classic = (len(pswd), 
                   *pattern_calc(pswd))
    print(time.time() - st1)
    return res_classic


if __name__ == '__main__':
    data = {'0': ['ch4nged', 'joseop7', 'pfy3iof', 'bmiki18'],
            '1': ['wkcirly85'],
            '2': ['fRUqufDQ0NwSC9uG', 'DfXe1wDM0OANv8uu', '1.01.61.82.02.2s']}

    data1 = {'0': ['m3ller', 'atblxp6'],
            '1': ['12345QWERT', 'mumaracay1', 'acgjdhrm326'],
            '2': ['uJXGbvDE2OAssdIM', '714amULImodIsUJ', '8Uo2NXDQwOQKODYX', 'xJEsvDDI4OQKRtlk']}

    # for x in data["2"]:
    #     print(analyse(x))
    print(analyse(data["2"][0]))