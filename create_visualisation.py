# %% codecell
import IPython
# %% codecell
depth2_dic = {'Depth1_18': ['Depth2_17', 'Depth2_18', 'Depth2_19'],
 'Depth1_11': ['Depth2_29',
  'Depth2_30',
  'Depth2_31',
  'Depth2_32',
  'Depth2_33'],
 'Depth1_60': ['Depth2_11', 'Depth2_12', 'Depth2_13'],
 'Depth1_73': ['Depth2_24', 'Depth2_25', 'Depth2_26'],
 'Depth1_44': ['Depth2_1',
  'Depth2_2',
  'Depth2_3'],
 'Depth1_5': ['Depth2_8', 'Depth2_9', 'Depth2_10'],
 'Depth1_1': ['Depth2_14', 'Depth2_15', 'Depth2_16'],
 'Depth1_6': ['Depth2_34', 'Depth2_35', 'Depth2_36', 'Depth2_37'],
 'Depth1_23': ['Depth2_20', 'Depth2_21', 'Depth2_22', 'Depth2_23'],
 'Depth1_17': ['Depth2_27', 'Depth2_28'],
 'Depth1_53': ['Depth2_39', 'Depth2_40', 'Depth2_41'],
 'Depth1_9': ['Depth2_38'],
 'Depth1_68': ['Depth2_4', 'Depth2_5', 'Depth2_6', 'Depth2_7'],
 'Depth1_66': ['Depth2_42', 'Depth2_43', 'Depth2_44'],
'Depth1_4': ['Depth2_45',
  'Depth2_46',
  'Depth2_47',
  'Depth2_48',
  'Depth2_49']}
depth3_dic = {'Depth2_10': ['Depth3_156', 'Depth3_165'],
 'Depth2_29': ['Depth3_14', 'Depth3_24'],
 'Depth2_19': ['Depth3_56', 'Depth3_71', 'Depth3_91'],
 'Depth2_22': ['Depth3_113', 'Depth3_121', 'Depth3_131'],
 'Depth2_21': ['Depth3_86', 'Depth3_94', 'Depth3_102'],
 'Depth2_1': ['Depth3_11', 'Depth3_21', 'Depth3_31'],
 'Depth2_49': ['Depth3_196', 'Depth3_203'],
 'Depth2_48': ['Depth3_176', 'Depth3_186', 'Depth3_195', 'Depth3_202'],
 'Depth2_2': ['Depth3_16', 'Depth3_26'],
 'Depth2_25': ['Depth3_166'],
 'Depth2_15': ['Depth3_85', 'Depth3_93', 'Depth3_101'],
 'Depth2_30': ['Depth3_36', 'Depth3_43', 'Depth3_53'],
 'Depth2_40': ['Depth3_44', 'Depth3_54'],
 'Depth2_41': ['Depth3_63'],
 'Depth2_43': ['Depth3_96', 'Depth3_104'],
 'Depth2_5': ['Depth3_76'],
 'Depth2_45': ['Depth3_136', 'Depth3_143'],
 'Depth2_8': ['Depth3_124', 'Depth3_133', 'Depth3_141'],
 'Depth2_34': ['Depth3_114'],
 'Depth2_3': ['Depth3_45'],
 'Depth2_18': ['Depth3_35', 'Depth3_42', 'Depth3_52'],
 'Depth2_37': ['Depth3_172', 'Depth3_182', 'Depth3_191'],
 'Depth2_46': ['Depth3_155', 'Depth3_164'],
 'Depth2_42': ['Depth3_75', 'Depth3_84', 'Depth3_92'],
 'Depth2_23': ['Depth3_125', 'Depth3_134', 'Depth3_142'],
 'Depth2_12': ['Depth3_34', 'Depth3_41', 'Depth3_51'],
 'Depth2_28': ['Depth3_171', 'Depth3_181'],
 'Depth2_16': ['Depth3_106'],
 'Depth2_14': ['Depth3_64', 'Depth3_73', 'Depth3_82'],
 'Depth2_13': ['Depth3_46', 'Depth3_55', 'Depth3_61'],
 'Depth2_26': ['Depth3_174', 'Depth3_184', 'Depth3_193', 'Depth3_201'],
 'Depth2_31': ['Depth3_62', 'Depth3_72', 'Depth3_81'],
 'Depth2_38': ['Depth3_175', 'Depth3_185', 'Depth3_194'],
 'Depth2_9': ['Depth3_144', 'Depth3_151', 'Depth3_161'],
 'Depth2_36': ['Depth3_154', 'Depth3_163'],
 'Depth2_33': ['Depth3_95', 'Depth3_103', 'Depth3_111'],
 'Depth2_7': ['Depth3_116', 'Depth3_123'],
 'Depth2_39': ['Depth3_15', 'Depth3_25'],
 'Depth2_44': ['Depth3_122', 'Depth3_132', 'Depth3_115'],
 'Depth2_32': ['Depth3_66'],
 'Depth2_17': ['Depth3_13', 'Depth3_23', 'Depth3_33'],
 'Depth2_35': ['Depth3_126', 'Depth3_135'],
 'Depth2_27': ['Depth3_146', 'Depth3_153', 'Depth3_162'],
 'Depth2_47': ['Depth3_173', 'Depth3_183', 'Depth3_192'],
 'Depth2_24': ['Depth3_145', 'Depth3_152'],
 'Depth2_20': ['Depth3_65', 'Depth3_74', 'Depth3_83'],
 'Depth2_11': ['Depth3_12', 'Depth3_22', 'Depth3_32'],
 'Depth2_6': ['Depth3_105', 'Depth3_112']}

depth4_dic = {
 'Depth3_203': ['Depth4_1179', 'Depth4_1180', 'Depth4_1181'],
 'Depth3_54': ['Depth4_290',
  'Depth4_291',
  'Depth4_292',
  'Depth4_295',
  'Depth4_298'],
 'Depth3_73': ['Depth4_403', 'Depth4_404', 'Depth4_405'],
 'Depth3_22': ['Depth4_92', 'Depth4_95', 'Depth4_96'],
 'Depth3_92': ['Depth4_516', 'Depth4_517', 'Depth4_518'],
 'Depth3_56': ['Depth4_312', 'Depth4_315', 'Depth4_318'],
 'Depth3_81': ['Depth4_440', 'Depth4_446', 'Depth4_447'],
 'Depth3_181': ['Depth4_1040'],
 'Depth3_85': ['Depth4_484', 'Depth4_486'],
 'Depth3_153': ['Depth4_880', 'Depth4_882', 'Depth4_883'],
 'Depth3_122': ['Depth4_689', 'Depth4_691', 'Depth4_698'],
 'Depth3_152': ['Depth4_872', 'Depth4_875', 'Depth4_878'],
 'Depth3_185': ['Depth4_1081', 'Depth4_1083', 'Depth4_1085'],
 'Depth3_95': ['Depth4_540', 'Depth4_544', 'Depth4_545'],
 'Depth3_35': ['Depth4_181', 'Depth4_186'],
 'Depth3_164': ['Depth4_949', 'Depth4_950', 'Depth4_955'],
 'Depth3_25': ['Depth4_120', 'Depth4_123', 'Depth4_126'],
 'Depth3_113': ['Depth4_646', 'Depth4_647', 'Depth4_648'],
 'Depth3_145': ['Depth4_839', 'Depth4_845', 'Depth4_848'],
 'Depth3_166': ['Depth4_969', 'Depth4_972', 'Depth4_974', 'Depth4_977'],
 'Depth3_162': ['Depth4_931', 'Depth4_935', 'Depth4_936'],
 'Depth3_66': ['Depth4_369', 'Depth4_375'],
 'Depth3_101': ['Depth4_561', 'Depth4_562', 'Depth4_564'],
 'Depth3_53': ['Depth4_279', 'Depth4_287', 'Depth4_288'],
 'Depth3_174': ['Depth4_1009', 'Depth4_1010', 'Depth4_1015'],
 'Depth3_191': ['Depth4_1102', 'Depth4_1104', 'Depth4_1105'],
 'Depth3_194': ['Depth4_1132', 'Depth4_1133'],
 'Depth3_161': ['Depth4_920', 'Depth4_921', 'Depth4_927'],
 'Depth3_96': ['Depth4_550', 'Depth4_553', 'Depth4_558'],
 'Depth3_151': ['Depth4_860', 'Depth4_862', 'Depth4_866'],
 'Depth3_165': ['Depth4_959',
  'Depth4_960',
  'Depth4_964',
  'Depth4_966',
  'Depth4_967'],
 'Depth3_26': ['Depth4_132', 'Depth4_134', 'Depth4_136', 'Depth4_138'],
 'Depth3_201': ['Depth4_1162', 'Depth4_1163', 'Depth4_1165'],
 'Depth3_51': ['Depth4_267', 'Depth4_268'],
 'Depth3_143': ['Depth4_820', 'Depth4_821', 'Depth4_824'],
 'Depth3_31': ['Depth4_139', 'Depth4_142'],
 'Depth3_16': ['Depth4_66', 'Depth4_77', 'Depth4_78'],
 'Depth3_112': ['Depth4_633', 'Depth4_635', 'Depth4_636'],
 'Depth3_41': ['Depth4_201', 'Depth4_203'],
 'Depth3_63': ['Depth4_339', 'Depth4_341', 'Depth4_343'],
 'Depth3_172': ['Depth4_990', 'Depth4_992', 'Depth4_993', 'Depth4_995'],
 'Depth3_192': ['Depth4_1112', 'Depth4_1116', 'Depth4_1117'],
 'Depth3_83': ['Depth4_462', 'Depth4_465', 'Depth4_466'],
 'Depth3_44': ['Depth4_235', 'Depth4_236', 'Depth4_238'],
 'Depth3_33': ['Depth4_160', 'Depth4_161', 'Depth4_162'],
 'Depth3_114': ['Depth4_653', 'Depth4_656', 'Depth4_657'],
 'Depth3_131': ['Depth4_740', 'Depth4_744', 'Depth4_748'],
 'Depth3_175': ['Depth4_1022', 'Depth4_1023', 'Depth4_1025'],
 'Depth3_156': ['Depth4_910', 'Depth4_917', 'Depth4_918'],
 'Depth3_202': ['Depth4_1170', 'Depth4_1174'],
 'Depth3_171': ['Depth4_980', 'Depth4_984', 'Depth4_986'],
 'Depth3_52': ['Depth4_269', 'Depth4_271', 'Depth4_273'],
 'Depth3_11': ['Depth4_1', 'Depth4_3', 'Depth4_7'],
 'Depth3_111': ['Depth4_620', 'Depth4_622', 'Depth4_625'],
 'Depth3_74': ['Depth4_412', 'Depth4_416', 'Depth4_417', 'Depth4_418'],
 'Depth3_93': ['Depth4_523', 'Depth4_526', 'Depth4_528'],
 'Depth3_134': ['Depth4_773', 'Depth4_774'],
 'Depth3_65': ['Depth4_364', 'Depth4_368'],
 'Depth3_36': ['Depth4_192', 'Depth4_196', 'Depth4_197'],
 'Depth3_71': ['Depth4_380', 'Depth4_382', 'Depth4_386'],
 'Depth3_146': ['Depth4_852', 'Depth4_855', 'Depth4_858'],
 'Depth3_86': ['Depth4_491', 'Depth4_492', 'Depth4_496'],
 'Depth3_42': ['Depth4_212', 'Depth4_215', 'Depth4_217'],
 'Depth3_141': ['Depth4_799', 'Depth4_801', 'Depth4_804'],
 'Depth3_135': ['Depth4_785'],
 'Depth3_144': ['Depth4_831', 'Depth4_833', 'Depth4_835'],
 'Depth3_173': ['Depth4_1004', 'Depth4_1006'],
 'Depth3_23': ['Depth4_102', 'Depth4_104', 'Depth4_108'],
 'Depth3_124': ['Depth4_712', 'Depth4_716', 'Depth4_717'],
 'Depth3_126': ['Depth4_735', 'Depth4_736'],
 'Depth3_14': ['Depth4_40', 'Depth4_44', 'Depth4_52'],
 'Depth3_46': ['Depth4_251', 'Depth4_253', 'Depth4_256'],
 'Depth3_176': ['Depth4_1032', 'Depth4_1033', 'Depth4_1036'],
 'Depth3_91': ['Depth4_500', 'Depth4_504', 'Depth4_505'],
 'Depth3_106': ['Depth4_609', 'Depth4_611'],
 'Depth3_62': ['Depth4_330', 'Depth4_336', 'Depth4_338'],
 'Depth3_163': ['Depth4_939', 'Depth4_944'],
 'Depth3_121': ['Depth4_679', 'Depth4_681', 'Depth4_687'],
 'Depth3_15': ['Depth4_57', 'Depth4_61', 'Depth4_62'],
 'Depth3_132': ['Depth4_749', 'Depth4_750', 'Depth4_751'],
 'Depth3_94': ['Depth4_533', 'Depth4_535', 'Depth4_538'],
 'Depth3_13': ['Depth4_27', 'Depth4_29', 'Depth4_32', 'Depth4_35'],
 'Depth3_105': ['Depth4_605', 'Depth4_606'],
 'Depth3_123': ['Depth4_699', 'Depth4_702', 'Depth4_703', 'Depth4_707'],
 'Depth3_64': ['Depth4_349', 'Depth4_353', 'Depth4_357'],
 'Depth3_55': ['Depth4_301', 'Depth4_303', 'Depth4_308'],
 'Depth3_184': ['Depth4_1070', 'Depth4_1071', 'Depth4_1078'],
 'Depth3_115': ['Depth4_659', 'Depth4_666', 'Depth4_667'],
 'Depth3_196': ['Depth4_1153', 'Depth4_1154', 'Depth4_1155', 'Depth4_1157'],
 'Depth3_155': ['Depth4_902', 'Depth4_906', 'Depth4_907'],
 'Depth3_182': ['Depth4_1053', 'Depth4_1054', 'Depth4_1058'],
 'Depth3_34': ['Depth4_172', 'Depth4_176', 'Depth4_177'],
 'Depth3_103': ['Depth4_582', 'Depth4_583', 'Depth4_585'],
 'Depth3_142': ['Depth4_811', 'Depth4_813', 'Depth4_814'],
 'Depth3_125': ['Depth4_724', 'Depth4_726', 'Depth4_727'],
 'Depth3_24': ['Depth4_109', 'Depth4_110', 'Depth4_115', 'Depth4_116'],
 'Depth3_84': ['Depth4_470', 'Depth4_471', 'Depth4_476'],
 'Depth3_21': ['Depth4_79', 'Depth4_84', 'Depth4_88'],
 'Depth3_72': ['Depth4_389', 'Depth4_390', 'Depth4_393'],
 'Depth3_195': ['Depth4_1142', 'Depth4_1146', 'Depth4_1147'],
 'Depth3_45': ['Depth4_245'],
 'Depth3_12': ['Depth4_15', 'Depth4_16', 'Depth4_19'],
 'Depth3_75': ['Depth4_423', 'Depth4_426', 'Depth4_427'],
 'Depth3_102': ['Depth4_571', 'Depth4_572', 'Depth4_575', 'Depth4_576'],
 'Depth3_183': ['Depth4_1059', 'Depth4_1065', 'Depth4_1067'],
 'Depth3_104': ['Depth4_589', 'Depth4_591', 'Depth4_593'],
 'Depth3_61': ['Depth4_321', 'Depth4_325', 'Depth4_327'],
 'Depth3_193': ['Depth4_1122', 'Depth4_1123', 'Depth4_1125'],
 'Depth3_136': ['Depth4_793', 'Depth4_794', 'Depth4_796', 'Depth4_797'],
 'Depth3_43': ['Depth4_220', 'Depth4_223', 'Depth4_226'],
 'Depth3_133': ['Depth4_764', 'Depth4_766', 'Depth4_767'],
 'Depth3_76': ['Depth4_433', 'Depth4_434', 'Depth4_436'],
 'Depth3_32': ['Depth4_149', 'Depth4_152'],
 'Depth3_116': ['Depth4_669', 'Depth4_673', 'Depth4_674']}

depth5_dic = {'Depth4_1': ['Depth5_1', 'Depth5_2', 'Depth5_4'],
 'Depth4_1004': ['Depth5_1404', 'Depth5_1405'],
 'Depth4_1006': ['Depth5_1466', 'Depth5_1467', 'Depth5_1468', 'Depth5_1469'],
 'Depth4_1009': ['Depth5_1415'],
 'Depth4_1010': ['Depth5_1444'],
 'Depth4_1015': ['Depth5_1471', 'Depth5_1472'],
 'Depth4_102': ['Depth5_98', 'Depth5_99'],
 'Depth4_1022': ['Depth5_1416', 'Depth5_1418', 'Depth5_1419', 'Depth5_1420'],
 'Depth4_1023': ['Depth5_1446', 'Depth5_1449'],
 'Depth4_1025': ['Depth5_1480'],
 'Depth4_1032': ['Depth5_1424', 'Depth5_1425'],
 'Depth4_1033': ['Depth5_1451', 'Depth5_1454'],
 'Depth4_1036': ['Depth5_1483', 'Depth5_1484', 'Depth5_1485'],
 'Depth4_104': ['Depth5_126', 'Depth5_128', 'Depth5_129'],
 'Depth4_1040': ['Depth5_1428', 'Depth5_1429'],
 'Depth4_1053': ['Depth5_1456', 'Depth5_1459'],
 'Depth4_1054': ['Depth5_1486', 'Depth5_1487', 'Depth5_1488'],
 'Depth4_1058': ['Depth5_1431', 'Depth5_1433', 'Depth5_1434'],
 'Depth4_1059': ['Depth5_1462', 'Depth5_1464', 'Depth5_1465'],
 'Depth4_1065': ['Depth5_1491', 'Depth5_1492', 'Depth5_1495'],
 'Depth4_1067': ['Depth5_1710'],
 'Depth4_1070': ['Depth5_1496', 'Depth5_1498'],
 'Depth4_1071': ['Depth5_1533', 'Depth5_1535', 'Depth5_1537'],
 'Depth4_1078': ['Depth5_1569', 'Depth5_1571'],
 'Depth4_108': ['Depth5_156', 'Depth5_159', 'Depth5_160'],
 'Depth4_1081': ['Depth5_1503', 'Depth5_1504', 'Depth5_1506', 'Depth5_1507'],
 'Depth4_1083': ['Depth5_1540', 'Depth5_1542'],
 'Depth4_1085': ['Depth5_1574', 'Depth5_1577'],
 'Depth4_109': ['Depth5_102', 'Depth5_105'],
 'Depth4_110': ['Depth5_132', 'Depth5_133'],
 'Depth4_1102': ['Depth5_1510'],
 'Depth4_1104': ['Depth5_1545', 'Depth5_1546', 'Depth5_1548'],
 'Depth4_1105': ['Depth5_1579', 'Depth5_1580', 'Depth5_1581'],
 'Depth4_1112': ['Depth5_1516'],
 'Depth4_1116': ['Depth5_1551', 'Depth5_1553', 'Depth5_1554', 'Depth5_1555'],
 'Depth4_1117': ['Depth5_1584', 'Depth5_1585', 'Depth5_1586'],
 'Depth4_1122': ['Depth5_1520', 'Depth5_1521', 'Depth5_1525'],
 'Depth4_1123': ['Depth5_1557', 'Depth5_1560', 'Depth5_1561'],
 'Depth4_1132': ['Depth5_1526', 'Depth5_1530'],
 'Depth4_1133': ['Depth5_1563', 'Depth5_1564', 'Depth5_1567'],
 'Depth4_1142': ['Depth5_1594', 'Depth5_1596', 'Depth5_1597'],
 'Depth4_1146': ['Depth5_1608', 'Depth5_1609', 'Depth5_1612'],
 'Depth4_1147': ['Depth5_1638', 'Depth5_1640'],
 'Depth4_115': ['Depth5_161', 'Depth5_162', 'Depth5_164'],
 'Depth4_1153': ['Depth5_1674', 'Depth5_1675', 'Depth5_1676'],
 'Depth4_1154': ['Depth5_1614', 'Depth5_1616', 'Depth5_1617'],
 'Depth4_1155': ['Depth5_1643', 'Depth5_1644'],
 'Depth4_1157': ['Depth5_1730', 'Depth5_1732'],
 'Depth4_116': ['Depth5_1633', 'Depth5_1634', 'Depth5_1635'],
 'Depth4_1162': ['Depth5_1618', 'Depth5_1620', 'Depth5_1622'],
 'Depth4_1163': ['Depth5_1648', 'Depth5_1649', 'Depth5_1650'],
 'Depth4_1165': ['Depth5_1681'],
 'Depth4_1170': ['Depth5_1623', 'Depth5_1625'],
 'Depth4_1174': ['Depth5_1653', 'Depth5_1654'],
 'Depth4_1179': ['Depth5_1683', 'Depth5_1684', 'Depth5_1685'],
 'Depth4_1180': ['Depth5_1735', 'Depth5_1737'],
 'Depth4_1181': ['Depth5_1716', 'Depth5_1717'],
 'Depth4_120': ['Depth5_110'],
 'Depth4_123': ['Depth5_136', 'Depth5_138'],
 'Depth4_126': ['Depth5_166', 'Depth5_167', 'Depth5_169'],
 'Depth4_132': ['Depth5_111', 'Depth5_113', 'Depth5_114'],
 'Depth4_134': ['Depth5_143'],
 'Depth4_136': ['Depth5_174', 'Depth5_175'],
 'Depth4_139': ['Depth5_118', 'Depth5_119', 'Depth5_120'],
 'Depth4_142': ['Depth5_148', 'Depth5_149'],
 'Depth4_149': ['Depth5_176', 'Depth5_177', 'Depth5_179'],
 'Depth4_15': ['Depth5_6', 'Depth5_7', 'Depth5_10'],
 'Depth4_152': ['Depth5_812', 'Depth5_813', 'Depth5_816'],
 'Depth4_16': ['Depth5_39'],
 'Depth4_160': ['Depth5_183', 'Depth5_184'],
 'Depth4_161': ['Depth5_217', 'Depth5_218', 'Depth5_222'],
 'Depth4_162': ['Depth5_256', 'Depth5_257'],
 'Depth4_172': ['Depth5_190', 'Depth5_191', 'Depth5_192'],
 'Depth4_176': ['Depth5_223', 'Depth5_224', 'Depth5_227'],
 'Depth4_177': ['Depth5_258', 'Depth5_259'],
 'Depth4_181': ['Depth5_193', 'Depth5_194', 'Depth5_195'],
 'Depth4_186': ['Depth5_229', 'Depth5_231', 'Depth5_233'],
 'Depth4_19': ['Depth5_67'],
 'Depth4_192': ['Depth5_265', 'Depth5_266', 'Depth5_267'],
 'Depth4_196': ['Depth5_203'],
 'Depth4_197': ['Depth5_238', 'Depth5_240'],
 'Depth4_201': ['Depth5_272'],
 'Depth4_212': ['Depth5_242', 'Depth5_244', 'Depth5_245'],
 'Depth4_215': ['Depth5_273', 'Depth5_274', 'Depth5_276'],
 'Depth4_217': ['Depth5_212', 'Depth5_214'],
 'Depth4_220': ['Depth5_248', 'Depth5_251'],
 'Depth4_223': ['Depth5_279', 'Depth5_281', 'Depth5_282'],
 'Depth4_226': ['Depth5_1669', 'Depth5_1671', 'Depth5_1672'],
 'Depth4_235': ['Depth5_284', 'Depth5_285', 'Depth5_287'],
 'Depth4_236': ['Depth5_314'],
 'Depth4_238': ['Depth5_345'],
 'Depth4_245': ['Depth5_289', 'Depth5_292'],
 'Depth4_251': ['Depth5_318', 'Depth5_320', 'Depth5_321'],
 'Depth4_253': ['Depth5_348', 'Depth5_351', 'Depth5_352'],
 'Depth4_256': ['Depth5_294', 'Depth5_297'],
 'Depth4_267': ['Depth5_325', 'Depth5_326'],
 'Depth4_268': ['Depth5_353', 'Depth5_355', 'Depth5_357'],
 'Depth4_269': ['Depth5_298'],
 'Depth4_27': ['Depth5_12', 'Depth5_15'],
 'Depth4_271': ['Depth5_328', 'Depth5_331', 'Depth5_332'],
 'Depth4_273': ['Depth5_358', 'Depth5_360', 'Depth5_362'],
 'Depth4_279': ['Depth5_303', 'Depth5_304', 'Depth5_307'],
 'Depth4_287': ['Depth5_334', 'Depth5_335', 'Depth5_337'],
 'Depth4_288': ['Depth5_363', 'Depth5_365', 'Depth5_367'],
 'Depth4_29': ['Depth5_42', 'Depth5_43', 'Depth5_44'],
 'Depth4_290': ['Depth5_311', 'Depth5_312'],
 'Depth4_291': ['Depth5_338'],
 'Depth4_292': ['Depth5_339', 'Depth5_368', 'Depth5_369', 'Depth5_372'],
 'Depth4_295': ['Depth5_342', 'Depth5_376', 'Depth5_377'],
 'Depth4_298': ['Depth5_406'],
 'Depth4_3': ['Depth5_31'],
 'Depth4_301': ['Depth5_433', 'Depth5_434', 'Depth5_436'],
 'Depth4_303': ['Depth5_381'],
 'Depth4_308': ['Depth5_408', 'Depth5_412'],
 'Depth4_312': ['Depth5_440'],
 'Depth4_315': ['Depth5_384', 'Depth5_386', 'Depth5_387'],
 'Depth4_318': ['Depth5_417'],
 'Depth4_32': ['Depth5_72', 'Depth5_74'],
 'Depth4_321': ['Depth5_445'],
 'Depth4_325': ['Depth5_391'],
 'Depth4_327': ['Depth5_420'],
 'Depth4_330': ['Depth5_449', 'Depth5_451'],
 'Depth4_336': ['Depth5_394', 'Depth5_396'],
 'Depth4_338': ['Depth5_425', 'Depth5_426', 'Depth5_427'],
 'Depth4_339': ['Depth5_454', 'Depth5_456', 'Depth5_457', 'Depth5_458'],
 'Depth4_341': ['Depth5_398', 'Depth5_399', 'Depth5_402'],
 'Depth4_343': ['Depth5_431'],
 'Depth4_349': ['Depth5_460', 'Depth5_461', 'Depth5_462'],
 'Depth4_35': ['Depth5_1601', 'Depth5_1602'],
 'Depth4_353': ['Depth5_464', 'Depth5_467'],
 'Depth4_357': ['Depth5_495', 'Depth5_498'],
 'Depth4_364': ['Depth5_526', 'Depth5_527'],
 'Depth4_368': ['Depth5_472'],
 'Depth4_369': ['Depth5_499', 'Depth5_500'],
 'Depth4_375': ['Depth5_530'],
 'Depth4_380': ['Depth5_474', 'Depth5_476', 'Depth5_477'],
 'Depth4_382': ['Depth5_508'],
 'Depth4_386': ['Depth5_535', 'Depth5_536', 'Depth5_537'],
 'Depth4_389': ['Depth5_479', 'Depth5_482', 'Depth5_483'],
 'Depth4_390': ['Depth5_512', 'Depth5_513'],
 'Depth4_393': ['Depth5_542', 'Depth5_543'],
 'Depth4_40': ['Depth5_17'],
 'Depth4_403': ['Depth5_484', 'Depth5_486', 'Depth5_488'],
 'Depth4_404': ['Depth5_515', 'Depth5_516', 'Depth5_518'],
 'Depth4_405': ['Depth5_546'],
 'Depth4_412': ['Depth5_489', 'Depth5_490', 'Depth5_492'],
 'Depth4_416': ['Depth5_520', 'Depth5_521', 'Depth5_523'],
 'Depth4_417': ['Depth5_551', 'Depth5_552'],
 'Depth4_418': ['Depth5_1688', 'Depth5_1690', 'Depth5_1691'],
 'Depth4_423': ['Depth5_556', 'Depth5_557'],
 'Depth4_426': ['Depth5_584', 'Depth5_585', 'Depth5_588'],
 'Depth4_427': ['Depth5_615', 'Depth5_617', 'Depth5_618'],
 'Depth4_433': ['Depth5_559', 'Depth5_561', 'Depth5_563'],
 'Depth4_434': ['Depth5_590', 'Depth5_592', 'Depth5_593'],
 'Depth4_436': ['Depth5_619', 'Depth5_620', 'Depth5_622'],
 'Depth4_440': ['Depth5_565', 'Depth5_568'],
 'Depth4_446': ['Depth5_594', 'Depth5_595', 'Depth5_598'],
 'Depth4_447': ['Depth5_627', 'Depth5_628'],
 'Depth4_462': ['Depth5_569', 'Depth5_571'],
 'Depth4_465': ['Depth5_602', 'Depth5_603'],
 'Depth4_466': ['Depth5_629', 'Depth5_633'],
 'Depth4_470': ['Depth5_574', 'Depth5_577', 'Depth5_578'],
 'Depth4_471': ['Depth5_606', 'Depth5_607', 'Depth5_608'],
 'Depth4_476': ['Depth5_636', 'Depth5_637', 'Depth5_638'],
 'Depth4_484': ['Depth5_579'],
 'Depth4_486': ['Depth5_610', 'Depth5_613'],
 'Depth4_491': ['Depth5_639', 'Depth5_640', 'Depth5_642'],
 'Depth4_492': ['Depth5_647'],
 'Depth4_496': ['Depth5_674', 'Depth5_675', 'Depth5_677', 'Depth5_678'],
 'Depth4_500': ['Depth5_710', 'Depth5_712', 'Depth5_714'],
 'Depth4_504': ['Depth5_650', 'Depth5_651', 'Depth5_653'],
 'Depth4_505': ['Depth5_681', 'Depth5_682', 'Depth5_683', 'Depth5_685'],
 'Depth4_516': ['Depth5_715', 'Depth5_717', 'Depth5_719'],
 'Depth4_517': ['Depth5_655', 'Depth5_656', 'Depth5_658'],
 'Depth4_518': ['Depth5_686', 'Depth5_687', 'Depth5_688'],
 'Depth4_52': ['Depth5_77'],
 'Depth4_523': ['Depth5_720', 'Depth5_721'],
 'Depth4_526': ['Depth5_660', 'Depth5_661', 'Depth5_663'],
 'Depth4_528': ['Depth5_693', 'Depth5_694', 'Depth5_697'],
 'Depth4_533': ['Depth5_727'],
 'Depth4_535': ['Depth5_665', 'Depth5_666', 'Depth5_668'],
 'Depth4_538': ['Depth5_698', 'Depth5_699', 'Depth5_703'],
 'Depth4_540': ['Depth5_732'],
 'Depth4_544': ['Depth5_671'],
 'Depth4_545': ['Depth5_707', 'Depth5_708'],
 'Depth4_550': ['Depth5_737'],
 'Depth4_553': ['Depth5_740', 'Depth5_741'],
 'Depth4_558': ['Depth5_782', 'Depth5_785', 'Depth5_786'],
 'Depth4_561': ['Depth5_819'],
 'Depth4_562': ['Depth5_747', 'Depth5_748', 'Depth5_750'],
 'Depth4_57': ['Depth5_22', 'Depth5_25'],
 'Depth4_571': ['Depth5_824', 'Depth5_826'],
 'Depth4_572': ['Depth5_754', 'Depth5_756'],
 'Depth4_575': ['Depth5_792', 'Depth5_796'],
 'Depth4_576': ['Depth5_1694', 'Depth5_1696'],
 'Depth4_582': ['Depth5_761', 'Depth5_762', 'Depth5_765', 'Depth5_767'],
 'Depth4_583': ['Depth5_797', 'Depth5_798', 'Depth5_800'],
 'Depth4_585': ['Depth5_828', 'Depth5_829'],
 'Depth4_589': ['Depth5_769', 'Depth5_770', 'Depth5_774'],
 'Depth4_591': ['Depth5_804'],
 'Depth4_593': ['Depth5_832', 'Depth5_833', 'Depth5_835'],
 'Depth4_605': ['Depth5_777'],
 'Depth4_606': ['Depth5_807', 'Depth5_808', 'Depth5_810'],
 'Depth4_609': ['Depth5_840'],
 'Depth4_61': ['Depth5_51', 'Depth5_53'],
 'Depth4_611': ['Depth5_843', 'Depth5_844', 'Depth5_846'],
 'Depth4_62': ['Depth5_81'],
 'Depth4_620': ['Depth5_872', 'Depth5_873', 'Depth5_876'],
 'Depth4_622': ['Depth5_903', 'Depth5_905', 'Depth5_906'],
 'Depth4_625': ['Depth5_847', 'Depth5_850', 'Depth5_851'],
 'Depth4_633': ['Depth5_879'],
 'Depth4_635': ['Depth5_908', 'Depth5_909', 'Depth5_910'],
 'Depth4_636': ['Depth5_852', 'Depth5_854'],
 'Depth4_646': ['Depth5_882', 'Depth5_884'],
 'Depth4_647': ['Depth5_915', 'Depth5_916'],
 'Depth4_648': ['Depth5_860', 'Depth5_861'],
 'Depth4_653': ['Depth5_888', 'Depth5_891'],
 'Depth4_656': ['Depth5_919'],
 'Depth4_657': ['Depth5_863', 'Depth5_866'],
 'Depth4_659': ['Depth5_893', 'Depth5_894', 'Depth5_895'],
 'Depth4_66': ['Depth5_30'],
 'Depth4_666': ['Depth5_926'],
 'Depth4_667': ['Depth5_870', 'Depth5_871'],
 'Depth4_674': ['Depth5_934', 'Depth5_936', 'Depth5_937'],
 'Depth4_679': ['Depth5_970'],
 'Depth4_681': ['Depth5_1008'],
 'Depth4_687': ['Depth5_938'],
 'Depth4_691': ['Depth5_1009', 'Depth5_1010', 'Depth5_1013'],
 'Depth4_698': ['Depth5_946', 'Depth5_948', 'Depth5_949'],
 'Depth4_699': ['Depth5_980', 'Depth5_984'],
 'Depth4_7': ['Depth5_62', 'Depth5_63', 'Depth5_64'],
 'Depth4_702': ['Depth5_1015', 'Depth5_1016', 'Depth5_1017'],
 'Depth4_703': ['Depth5_950', 'Depth5_953', 'Depth5_954'],
 'Depth4_707': ['Depth5_1698'],
 'Depth4_712': ['Depth5_957', 'Depth5_958', 'Depth5_960'],
 'Depth4_716': ['Depth5_990', 'Depth5_991'],
 'Depth4_717': ['Depth5_1020', 'Depth5_1022', 'Depth5_1023'],
 'Depth4_724': ['Depth5_962', 'Depth5_964', 'Depth5_966'],
 'Depth4_726': ['Depth5_994', 'Depth5_995', 'Depth5_996'],
 'Depth4_727': ['Depth5_1024', 'Depth5_1025', 'Depth5_1026', 'Depth5_1028'],
 'Depth4_735': ['Depth5_999', 'Depth5_1002'],
 'Depth4_736': ['Depth5_1029', 'Depth5_1033'],
 'Depth4_740': ['Depth5_1035', 'Depth5_1036', 'Depth5_1037', 'Depth5_1038'],
 'Depth4_744': ['Depth5_1064', 'Depth5_1065', 'Depth5_1067'],
 'Depth4_748': ['Depth5_1095', 'Depth5_1097', 'Depth5_1098'],
 'Depth4_749': ['Depth5_1039', 'Depth5_1041', 'Depth5_1042'],
 'Depth4_750': ['Depth5_1069', 'Depth5_1070', 'Depth5_1071', 'Depth5_1072'],
 'Depth4_751': ['Depth5_1099', 'Depth5_1100', 'Depth5_1101'],
 'Depth4_764': ['Depth5_1044', 'Depth5_1046', 'Depth5_1048'],
 'Depth4_766': ['Depth5_1076', 'Depth5_1077'],
 'Depth4_767': ['Depth5_1104',
  'Depth5_1105',
  'Depth5_1106',
  'Depth5_1107',
  'Depth5_1108'],
 'Depth4_77': ['Depth5_57', 'Depth5_58', 'Depth5_60'],
 'Depth4_773': ['Depth5_1049', 'Depth5_1051', 'Depth5_1053'],
 'Depth4_774': ['Depth5_1079', 'Depth5_1082'],
 'Depth4_78': ['Depth5_87', 'Depth5_88', 'Depth5_89'],
 'Depth4_785': ['Depth5_1109', 'Depth5_1110', 'Depth5_1113'],
 'Depth4_79': ['Depth5_1603', 'Depth5_1605', 'Depth5_1606'],
 'Depth4_793': ['Depth5_1054'],
 'Depth4_794': ['Depth5_1085', 'Depth5_1087'],
 'Depth4_796': ['Depth5_1114', 'Depth5_1115', 'Depth5_1118'],
 'Depth4_797': ['Depth5_1718', 'Depth5_1719', 'Depth5_1722'],
 'Depth4_799': ['Depth5_1060', 'Depth5_1061', 'Depth5_1063'],
 'Depth4_801': ['Depth5_1089', 'Depth5_1090'],
 'Depth4_804': ['Depth5_1119', 'Depth5_1120', 'Depth5_1121'],
 'Depth4_811': ['Depth5_1124', 'Depth5_1126', 'Depth5_1128'],
 'Depth4_813': ['Depth5_1154', 'Depth5_1155', 'Depth5_1156'],
 'Depth4_814': ['Depth5_1184', 'Depth5_1185', 'Depth5_1189'],
 'Depth4_820': ['Depth5_1129', 'Depth5_1131', 'Depth5_1133'],
 'Depth4_821': ['Depth5_1162'],
 'Depth4_824': ['Depth5_1191', 'Depth5_1192', 'Depth5_1194'],
 'Depth4_831': ['Depth5_1134', 'Depth5_1138'],
 'Depth4_833': ['Depth5_1165', 'Depth5_1166', 'Depth5_1167'],
 'Depth4_835': ['Depth5_1199', 'Depth5_1201'],
 'Depth4_839': ['Depth5_1139', 'Depth5_1141', 'Depth5_1143'],
 'Depth4_84': ['Depth5_1630', 'Depth5_1632'],
 'Depth4_845': ['Depth5_1169', 'Depth5_1170', 'Depth5_1173'],
 'Depth4_848': ['Depth5_1205'],
 'Depth4_852': ['Depth5_1144'],
 'Depth4_855': ['Depth5_1174', 'Depth5_1177', 'Depth5_1178'],
 'Depth4_858': ['Depth5_1210', 'Depth5_1212', 'Depth5_1213'],
 'Depth4_860': ['Depth5_1149', 'Depth5_1152'],
 'Depth4_862': ['Depth5_1179', 'Depth5_1180', 'Depth5_1181', 'Depth5_1183'],
 'Depth4_866': ['Depth5_1215', 'Depth5_1217'],
 'Depth4_872': ['Depth5_1220', 'Depth5_1221', 'Depth5_1222'],
 'Depth4_875': ['Depth5_1250', 'Depth5_1252', 'Depth5_1253'],
 'Depth4_878': ['Depth5_1280', 'Depth5_1281', 'Depth5_1282'],
 'Depth4_88': ['Depth5_1660', 'Depth5_1661'],
 'Depth4_880': ['Depth5_1227', 'Depth5_1229'],
 'Depth4_882': ['Depth5_1258', 'Depth5_1259'],
 'Depth4_883': ['Depth5_1290'],
 'Depth4_902': ['Depth5_1231'],
 'Depth4_906': ['Depth5_1260', 'Depth5_1262'],
 'Depth4_907': ['Depth5_1294', 'Depth5_1295', 'Depth5_1296'],
 'Depth4_910': ['Depth5_1237', 'Depth5_1239'],
 'Depth4_917': ['Depth5_1265', 'Depth5_1268'],
 'Depth4_918': ['Depth5_1299', 'Depth5_1300', 'Depth5_1301', 'Depth5_1303'],
 'Depth4_92': ['Depth5_91', 'Depth5_93', 'Depth5_95'],
 'Depth4_920': ['Depth5_1242', 'Depth5_1243', 'Depth5_1244'],
 'Depth4_921': ['Depth5_1241', 'Depth5_1272', 'Depth5_1273'],
 'Depth4_927': ['Depth5_1307'],
 'Depth4_931': ['Depth5_1246', 'Depth5_1247', 'Depth5_1248'],
 'Depth4_935': ['Depth5_1275', 'Depth5_1276', 'Depth5_1277'],
 'Depth4_936': ['Depth5_1310'],
 'Depth4_939': ['Depth5_1318', 'Depth5_1319', 'Depth5_1320'],
 'Depth4_944': ['Depth5_1347'],
 'Depth4_949': ['Depth5_1377', 'Depth5_1379'],
 'Depth4_95': ['Depth5_122', 'Depth5_124'],
 'Depth4_950': ['Depth5_1321', 'Depth5_1322', 'Depth5_1325'],
 'Depth4_955': ['Depth5_1352', 'Depth5_1354'],
 'Depth4_959': ['Depth5_1355', 'Depth5_1382', 'Depth5_1383', 'Depth5_1384'],
 'Depth4_96': ['Depth5_151', 'Depth5_154', 'Depth5_155'],
 'Depth4_964': ['Depth5_1360'],
 'Depth4_966': ['Depth5_1705'],
 'Depth4_967': ['Depth5_1724', 'Depth5_1725', 'Depth5_1726'],
 'Depth4_969': ['Depth5_1331', 'Depth5_1335'],
 'Depth4_972': ['Depth5_1362', 'Depth5_1365'],
 'Depth4_974': ['Depth5_1386', 'Depth5_1387', 'Depth5_1389', 'Depth5_1390'],
 'Depth4_977': ['Depth5_1336', 'Depth5_1337', 'Depth5_1339'],
 'Depth4_980': ['Depth5_1368', 'Depth5_1369', 'Depth5_1370'],
 'Depth4_984': ['Depth5_1392', 'Depth5_1393', 'Depth5_1394', 'Depth5_1395'],
 'Depth4_986': ['Depth5_1345'],
 'Depth4_990': ['Depth5_1373', 'Depth5_1374'],
 'Depth4_992': ['Depth5_1396', 'Depth5_1397', 'Depth5_1399', 'Depth5_1400'],
 'Depth4_993': ['Depth5_1406', 'Depth5_1409'],
 'Depth4_995': ['Depth5_1436', 'Depth5_1439']}


depth1_keys = depth2_dic.keys()
depth1_dic = {}
depth1_dic['a0'] = list(depth1_keys)
depth1_dic
all_depths = {**depth5_dic, **depth4_dic, **depth3_dic, **depth2_dic, **depth1_dic}
# %% codecell
import pandas as pd
depth1_file = 'graph_depth1.csv'
depth1_df = pd.read_csv(depth1_file,encoding='latin-1')

depth2_file = 'graph_depth2.csv'
depth2_df = pd.read_csv(depth2_file,encoding='latin-1')

depth3_file = 'graph_depth3.csv'
depth3_df = pd.read_csv(depth3_file, encoding='latin-1')

depth4_file = 'graph_depth4.csv'
depth4_df = pd.read_csv(depth4_file,encoding='latin-1')

depth5_file = 'graph_depth5.csv'
depth5_df = pd.read_csv(depth5_file,encoding='latin-1')

frames = [depth1_df, depth2_df, depth3_df, depth4_df, depth5_df]

df_all = pd.concat(frames)
arg_dic = dict(zip(df_all.arg_id, df_all.Argument))
arg_dic['a0'] = 'University fees in the UK should be kept at 9k'

df_all
# %% codecell
args1 = list(arg_dic.keys())
# %% codecell
for g in arg_dic:


    argument = arg_dic[g].split()
    chunks = [argument[x:x+6] for x in range(0, len(argument), 6)]
    argument = ' <br> '.join(' '.join(a) for a in chunks)
    arg_dic[g] = argument
    print(argument)
    print()

# %% codecell

# %% codecell
from pyvis.network import Network

# %% codecell
#arg_net = Network(notebook=True, height="750px", width="100%", bgcolor="#111111", font_color="white")
arg_net = Network(notebook=True, height="750px", width="100%", font_color="black")

#arg_net.barnes_hut(gravity=-1000, central_gravity=-2)
arg_net.force_atlas_2based(gravity=-400, central_gravity=0.001, damping=1)
# %% codecell

# %% codecell
for arg in args1:
    argument = arg_dic[arg]

    arg_net.add_node(arg, label=arg, title=argument, color='black', size=20)

for arg in args1:
    try:
        edges = all_depths[arg]
        for e in edges:
            arg_net.add_edge(e,arg, value=10)
    except:
        pass
arg_net.show('arg.html')
# %% codecell

# %% codecell
argument = "a1"

arg_dic = {
    'a1': 'argument 1',
    'a21': 'attack a1 a',
    'a22': 'attack- a1 b',
    'a23': 'attack- a1 c',
    'a31': 'attack a21 a ',
    'a32': 'attack a21 b ',
    'a33': 'attack a23 a ',
    'a34': 'attack a23 b ',
    'a41': 'attack a34 a '

}

arg_depth2 =  {
    'a1': ['a21', 'a23', 'a22']
}


arg_depth3 = {
    'a21': ['a31', 'a32'],
    'a23': ['a33', 'a34']
}

arg_depth4 = {
    'a33': ['a41']
}


all_depths = {**arg_depth2, **arg_depth3, **arg_depth4}
print(all_depths)

args1 = list(arg_dic.keys())
args1
# %% codecell
dummy_net = Network(notebook=True, height="1550px", width="100%", bgcolor="#222222", font_color="white")
dummy_net.barnes_hut(gravity=100)
for arg in args1:
    argument = arg_dic[arg]
    dummy_net.add_node(arg, label=arg, title=argument, value=10)

for arg in args1:
    try:
        edges = all_depths[arg]
        for e in edges:
            dummy_net.add_edge(e,arg)
    except:
        pass



# %% codecell
dummy_net.show('dummy.html')
# %% codecell

# %% codecell
