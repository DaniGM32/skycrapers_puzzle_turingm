TESTS = {
    "3212#2:2143:2#2:3412:2#3:1324:1#1:4231:3#1322" : (True, True, True),
    "1111#1:1234:1#1:2123:1#1:4341:1#1:3412:1#1111" : (False, True, False),
    "3212#3:2341:2#4:1234:1#2:3412:2#1:4123:2#1232" : (True, True, True),
    "1223#1:4321:4#2:3142:2#4:1234:1#2:2413:2#3132" : (True, True, True),
    "3132#2:2431:3#2:3214:1#1:4123:2#3:1342:2#2323" : (True, True, False),
    "2321#3:3214:3#2:2341:2#4:1432:4#1:4123:3#3231" : (True, True, False),
    "1222#1:4213:3#2:1432:3#3:3124:1#3:2341:2#2322" : (True, True, False),
    "1122#2:1432:3#2:3124:1#3:1342:2#2:2413:2#1122" : (True, False, False),
    "1232#1:4213:2#2:1432:3#2:3124:1#3:2341:2#3212" : (True, True, True),
    "1213#2:3241:2#2:1432:3#2:3244:1#1:4123:2#1322" : (False, False, False),
    "2111#3:1231:2#1:4132:3#1:2214:1#2:2413:2#1112" : (False, False, False),
    "2231#3:1214:1#1:4132:3#2:3423:2#3:2341:2#3213" : (False, True, True),
    "2312#3:1243:2#1:4321:4#2:1432:3#2:3124:1#2231" : (True, False, True),
    "2231#2:3124:1#2:2413:2#1:4231:3#3:1342:2#2213" : (True, True, True),
    "3111#1:1234:1#1:2231:2#3:3432:1#1:2143:3#1221" : (False, False, False),
    "2123#2:2431:3#1:4312:3#2:3124:1#3:1243:2#3312" : (True, True, True),
    "1223#1:4132:3#2:2413:2#2:3241:2#3:1324:1#3221" : (True, True, True),
    "2312#2:3241:2#3:1324:1#2:2413:2#1:4132:3#1222" : (True, True, False),
    "1222#1:4123:2#2:3412:2#3:2341:2#4:1234:1#3321" : (True, True, False),
    "3221#3:2134:1#2:1423:2#2:3241:2#1:4312:3#1123" : (True, True, False),
    "2311#2:3142:2#3:2314:1#2:1423:2#1:4231:3#1223" : (True, True, False),
    "3321#3:2134:1#2:3241:2#1:4312:3#2:1423:2#2122" : (True, True, False),
    "2241#3:2314:1#2:1423:2#1:4132:3#2:3241:2#2213" : (True, True, False),
    "1322#1:4132:3#3:2341:2#2:3214:1#2:1423:2#2122" : (True, True, False),
    "2311#2:3241:2#3:1324:1#1:4132:3#2:2413:2#2132" : (True, True, False),
    "2332#3:3123:4#1:4214:3#2:1432:2#4:2341:1#2213" : (False, True, False),
    "2314#3:1324:1#3:2134:1#1:4312:3#2:3421:3#2123" : (True, False, False),
    "4123#2:1432:2#4:2341:1#3:3123:4#1:4214:3#1331" : (False, True, False),
    "1223#2:3241:2#3:2134:1#1:4213:2#2:3124:1#1232" : (True, False, False),
    "2321#3:2314:1#2:3241:2#1:4134:1#2:2142:2#4124" : (False, False, False),
}