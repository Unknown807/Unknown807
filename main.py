import os
import random as rand
from github import Github
from get_cards import AsyncRequests

card_ids = {
    "classic": ['EX1_621', 'EX1_607', 'EX1_145', 'EX1_144', 'EX1_332', 'CS2_231', 'CS2_188', 'EX1_009', 'EX1_008', 'EX1_549', 'EX1_363', 'CS2_059', 'NEW1_025', 'EX1_243', 'EX1_245', 'EX1_132', 'EX1_319', 'EX1_544', 'EX1_251', 'NEW1_017', 'CS1_129', 'EX1_029', 'EX1_238', 'EX1_001', 'NEW1_012', 'EX1_509', 'EX1_130', 'EX1_136', 'EX1_379', 'EX1_578', 'EX1_080', 'EX1_410', 'EX1_405', 'CS2_146', 'EX1_409', 'EX1_010', 'CS2_169', 'EX1_004', 'EX1_393', 'CS2_038', 
                'EX1_045', 'EX1_362', 'EX1_402', 'EX1_392', 'EX1_126', 'CS2_233', 'EX1_012', 'NEW1_018', 'CS2_073', 'NEW1_036', 'EX1_059', 'EX1_603', 'EX1_131', 'EX1_596', 'EX1_162', 'NEW1_021', 'EX1_124', 'EX1_610', 'NEW1_023', 'EX1_611', 'NEW1_019', 'EX1_341', 'EX1_096', 'EX1_100', 'EX1_082', 'EX1_055', 'EX1_616', 'NEW1_037', 'NEW1_029', 'EX1_533', 'EX1_557', 'EX1_522', 'EX1_076', 
                'EX1_160', 'CS2_104', 'EX1_531', 'EX1_625', 'EX1_391', 'EX1_554', 'EX1_609', 'EX1_608', 'EX1_247', 'EX1_058', 'EX1_339', 'NEW1_020', 'EX1_154', 'EX1_049', 'EX1_006', 'EX1_382', 'EX1_089', 'EX1_590', 'EX1_103', 'EX1_275', 'EX1_287', 'EX1_617', 'EX1_102', 'EX1_536', 'CS2_117', 'EX1_613', 'EX1_170', 'EX1_619', 'CS2_053', 'EX1_301', 'EX1_248', 'tt_004', 'EX1_604', 'EX1_556', 'EX1_137', 'EX1_289', 'EX1_597', 'CS2_181', 'CS2_203', 'EX1_017', 'EX1_014', 'EX1_612', 'EX1_241', 'EX1_259', 'EX1_335', 'EX1_575', 'EX1_155', 'EX1_294', 'EX1_507', 'EX1_133', 'EX1_044', 'EX1_412', 'EX1_020', 'EX1_317', 'EX1_334', 'EX1_134', 'NEW1_027', 'tt_010', 'EX1_366', 'EX1_390', 'EX1_021', 'EX1_083', 'EX1_258', 'EX1_538', 'EX1_594', 'EX1_304', 'EX1_057', 'EX1_584', 'EX1_398', 'EX1_005', 'EX1_570', 'EX1_595', 'EX1_046', 'EX1_093', 
                'NEW1_022', 'EX1_274', 'EX1_166', 'EX1_626', 'NEW1_014', 'EX1_345', 'EX1_396', 'EX1_408', 'EX1_313', 'EX1_303', 'EX1_023', 'EX1_158', 'EX1_315', 'EX1_043', 'NEW1_026', 'EX1_097', 'EX1_320', 'EX1_355', 'EX1_407', 'NEW1_024', 'EX1_567', 'EX1_165', 'EX1_250', 'EX1_537', 'EX1_564', 'CS1_069', 'EX1_571', 'EX1_558', 'EX1_365', 'CS2_151', 'EX1_309', 'CS2_221', 'NEW1_041', 'NEW1_007', 'EX1_028', 'EX1_623', 'CS2_227', 'EX1_067', 'EX1_384', 'CS2_028', 'EX1_091', 'EX1_110', 'EX1_283', 'EX1_095', 'NEW1_040', 'NEW1_005', 'EX1_164', 'EX1_583', 'EX1_534', 'EX1_032', 'EX1_577', 'EX1_002', 'EX1_033', 'EX1_614', 'NEW1_008', 'EX1_178', 'EX1_559', 'EX1_249', 'DS1_188', 'EX1_411', 'CS2_161', 'NEW1_010', 'EX1_573', 'EX1_414', 'NEW1_038', 'EX1_354', 'EX1_383', 'EX1_312', 'EX1_561', 'EX1_543', 'EX1_323', 'EX1_563', 'EX1_560', 
                'EX1_562', 'EX1_572', 'NEW1_030', 'EX1_279', 'EX1_586'],

    "grandt": ['AT_004', 'AT_059', 'AT_029', 'AT_073', 'AT_055', 'AT_133', 'AT_105', 'AT_037', 'AT_061', 'AT_082', 'AT_013', 'AT_097', 'AT_071', 'AT_053', 'AT_077', 'AT_109', 'AT_060', 'AT_068', 'AT_089', 'AT_016', 'AT_015', 'AT_031', 'AT_038', 'AT_024', 'AT_042', 'AT_003', 'AT_094', 'AT_080', 'AT_058', 'AT_084', 'AT_069', 'AT_021', 'AT_052', 'AT_030', 'AT_026', 'AT_116', 'AT_087', 'AT_064', 'AT_035', 'AT_033', 'AT_110', 'AT_083', 'AT_063t', 'AT_002', 'AT_051', 'AT_131', 'AT_115', 'AT_129', 'AT_048', 'AT_092', 'AT_065', 'AT_106', 'AT_117', 'AT_044', 'AT_066', 'AT_005', 'AT_056', 'AT_086', 'AT_074', 
                'AT_014', 'AT_032', 'AT_095', 'AT_100', 'AT_007', 'AT_057', 'AT_046', 'AT_075', 'AT_108', 'AT_043', 'AT_050', 'AT_121', 'AT_006', 'AT_047', 'AT_019', 'AT_114', 'AT_022', 'AT_093', 'AT_122', 'AT_011', 'AT_067', 'AT_085', 'AT_076', 'AT_034', 'AT_111', 'AT_039', 'AT_012', 'AT_091', 'AT_017', 'AT_040', 'AT_096', 'AT_001', 'AT_119', 'AT_090', 'AT_127', 'AT_101', 'AT_010', 
                'AT_113', 'AT_028', 'AT_049', 'AT_104', 'AT_062', 'AT_124', 'AT_008', 'AT_025', 'AT_078', 'AT_118', 'AT_132', 'AT_099', 'AT_112', 'AT_088', 'AT_079', 'AT_130', 'AT_098', 'AT_054', 'AT_128', 'AT_023', 'AT_027', 'AT_063', 'AT_102', 'AT_123', 'AT_018', 'AT_081', 'AT_020', 'AT_041', 'AT_070', 'AT_009', 'AT_036', 'AT_125', 'AT_103', 'AT_045', 'AT_120', 'AT_072'],

    "wotog": ['OG_086', 'OG_198', 'OG_114', 'OG_101', 'OG_070', 'OG_314', 'OG_223', 'OG_027', 'OG_179', 'OG_051', 'OG_072', 'OG_312', 'OG_061', 'OG_241', 'OG_023', 'OG_221', 'OG_123', 'OG_151', 'OG_006', 'OG_158', 'OG_311', 'OG_281', 'OG_156', 'OG_303', 'OG_109', 'OG_326', 'OG_104', 'OG_026', 'OG_048', 'OG_338', 'OG_118', 'OG_081', 'OG_206', 'OG_284', 'OG_247', 'OG_330', 'OG_313', 'OG_248', 'OG_276', 'OG_315', 'OG_325', 'OG_113', 'OG_162', 'OG_047', 'OG_292', 'OG_045', 'OG_222', 'OG_149', 'OG_176', 'OG_034', 'OG_256', 'OG_116', 'OG_327', 'OG_310', 'OG_286', 'OG_083', 'OG_150', 'OG_322', 'OG_218', 'OG_283', 'OG_337', 'OG_085', 'OG_254', 'OG_082', 'OG_174', 'OG_044', 'OG_024', 'OG_334', 'OG_249', 'OG_216', 'OG_188', 'OG_328', 'OG_320', 'OG_202', 'OG_323', 'OG_100', 'OG_335', 'OG_267', 'OG_272', 'OG_080', 'OG_090', 'OG_147', 'OG_321', 'OG_295', 'OG_234', 'OG_102', 'OG_209', 'OG_031', 'OG_094', 'OG_309', 'OG_145', 'OG_087', 'OG_291', 'OG_273', 'OG_033', 'OG_096', 'OG_302', 'OG_200', 'OG_290', 'OG_161', 'OG_293', 'OG_207', 'OG_316', 'OG_122', 'OG_138', 'OG_271', 'OG_339', 'OG_028', 'OG_073', 'OG_301', 'OG_153', 'OG_121', 'OG_152', 'OG_318', 'OG_220', 'OG_131', 'OG_195', 'OG_120', 'OG_211', 'OG_255', 'OG_142', 'OG_308', 'OG_229', 'OG_300', 'OG_282', 'OG_173', 'OG_340', 'OG_280', 'OG_317', 'OG_239', 'OG_141', 'OG_133', 'OG_042', 'OG_134'],
}

headers = {
	"x-rapidapi-key": os.environ["api_key"],
	"x-rapidapi-host": "omgvamp-hearthstone-v1.p.rapidapi.com",
	"useQueryString": "true"
}

issue_title = os.environ["issue_title"]
issue_title = issue_title.split("|")[1].lower()

urls = [
    "https://omgvamp-hearthstone-v1.p.rapidapi.com/cards/"+rand.choice(card_ids[issue_title]) for i in range(5)
]

# 10% chance for a card to be golden
golden_prob = [False,]*9+[True,]

def get_card_imgs():
    try:
        cards = AsyncRequests.run(urls, headers=headers)
    except:
        issue_body = "Sorry, there was an error requesting the api, try again later."
        return (False, issue_body)

    card_imgs = []

    for card in cards:
        card_data=card[0][0]
        if "imgGold" in card_data:
            if (rand.choice(golden_prob)):
                card_imgs.append(card_data["imgGold"])
                continue
        
        card_imgs.append(card_data["img"])
    
    return (True, card_imgs)
                
if __name__ == "__main__":
    data = get_card_imgs()
    
    try:
        g = Github(os.environ["access_token"])

        repo = g.get_repo("Unknown807/Unknown807")
        issue = repo.get_issue(number=int(os.environ["issue_num"]))

        if (data[0]):
            issue.create_comment("""Here are your cards:
            ![No Image, Sorry]({})
            ![No Image, Sorry]({})
            ![No Image, Sorry]({})
            ![No Image, Sorry]({})
            ![No Image, Sorry]({})
            """.format(*data[1]))
        else:
            issue.create_comment(data[1])
        
        issue.edit(state="closed")
    except:
        pass