from application.models import dungeonx

def monster_list():
    dungeons = list( monster.objects.aggregate(*[
            {
                '$lookup': {
                    'from': 'populate', 
                    'localField': 'monster_id', 
                    'foreignField': 'monster_id', 
                    'as': 'r1'
                }
            }, {
                '$unwind': {
                    'path': '$r1', 
                    'includeArrayIndex': 'r1_id', 
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$lookup': {
                    'from': 'dungeonx', 
                    'localField': 'r1.dungeonID', 
                    'foreignField': 'dungeonID', 
                    'as': 'r2'
                }
            }, {
                '$unwind': {
                    'path': '$r2', 
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$match': {
                    'monster_id': monster_id
                }
            }, {
                '$sort': {
                    'dungeonID': 1
                }
            }
        ]))
    return dungeons