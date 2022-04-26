def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key]=='zielone':
            stoplight[key]='żółte'
        elif stoplight[key]=='żółte':
            stoplight[key]='czerwone'
        elif stoplight[key]=='czerwone':
            stoplight[key]='zielone'
