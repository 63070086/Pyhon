"""time"""
def time():
    """time input"""
    s_time = int(input())
    s_hor = s_time//3600
    s_horex = s_time%3600
    s_min = s_horex//60
    s_minex = s_horex%60
    print("%d hour(s) %d minute(s) %d second(s)."%(s_hor, s_min, s_minex))
time()
