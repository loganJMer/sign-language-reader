def find_letter(lms):

    if len(lms) != 21:
        return None

    #Check fingers are curled and thumb top above fingers
    if all(lms[i][1] > lms[i-2][1] for i in (8, 12, 16, 20)) and lms[4][1] < lms[6][1] and lms[17][0] < lms[0][0] and lms[4][0] > lms[6][0]:
        return 'A'
    
    #Check fingers are straight and thumb across index
    if all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (8, 12, 16, 20)) and lms[4][0] < lms[5][0] and lms[17][0] < lms[5][0] :
        return 'B'
    
    #Check fingers are curled, thumb tip below index tip, wrist rotated slightly, and fingers not touching
    if all(lms[4][1] > lms[i][1] > lms[i-2][1] for i in (8, 12, 16, 20)) and lms[20][0] > lms[5][0] and (lms[3][1] - lms[4][1]) * 2 < lms[4][1] - lms[12][1] and lms[1][0] > lms[0][0]:
        return 'C'
    
    #Check index straight and rest curled
    if all(lms[i][1] > lms[i-2][1] for i in (12, 16, 20)) and lms[8][1] < lms[7][1] < lms[6][1] and (lms[4][0] < lms[2][0] or lms[4][0] < lms[3][0]) and lms[8][0] > lms[12][0] and lms[5][0] > lms[17][0]:
        return 'D'

    #Check all curved and thumb below tips
    if all(lms[4][1] > lms[i][1] > lms[i-2][1] for i in (8, 12, 16, 20)) and lms[8][0] > lms[4][0] < lms[3][0] and lms[5][0] > lms[17][0]:
        return 'E'
    
    #O but back three fingers straight
    if all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (12, 16, 20)) and lms[4][1] > lms[8][1] > lms[7][1] and (lms[3][1] - lms[4][1]) * 2.5 > lms[4][1] - lms[8][1] and lms[7][0] > lms[17][0]:
        return 'F'
    
    #Check index above middle etc., bottom three curled and index straight, and ring base below thumb base
    if all(lms[i][1] > lms[i-4][1] and lms[i][0] < lms[i-2][0] for i in (12, 16, 20)) and lms[8][0] > lms[7][0] > lms[6][0] and lms[1][1] < lms[13][1]:
        return 'G'
    
    #G but middle also straight
    if all(lms[i][1] > lms[i-4][1] and lms[i][0] < lms[i-2][0] for i in (16, 20)) and lms[8][0] > lms[7][0] and lms[12][0] > lms[11][0] and lms[13][1] > lms[1][1]:
        return 'H'
    
    #D but pinky
    if all(lms[i][1] > lms[i-2][1] for i in (8, 12, 16)) and lms[20][1] < lms[19][1] < lms[18][1] < lms[4][1] and (lms[4][0] < lms[2][0] or lms[4][0] < lms[3][0]) and lms[8][0] > lms[20][0]:
        return 'I'
    
    #I but flipped
    if all(lms[i][1] > lms[i-2][1] for i in (8, 12, 16)) and lms[20][1] < lms[19][1] < lms[18][1] and (lms[4][0] > lms[2][0] or lms[4][0] > lms[3][0]) and lms[8][0] < lms[20][0]:
        return 'J'
    
    #Pinky and ring curled, middle and index straight, thumb tip above pinky tip, thumb across index
    if all(lms[i][1] > lms[i-2][1] for i in (16, 20)) and all(lms[i][1] < lms[i-1][1] for i in (8, 12)) and lms[4][1] < lms[15][1] and lms[4][0] < lms[8][0] and  lms[8][1] < lms[4][1] < lms[9][1] and lms[5][0] > lms[17][0]  and lms[8][0] > lms[12][0]:
        return 'K'
    
    #D but thumb out
    if all(lms[i][1] > lms[i-2][1] for i in (12, 16, 20)) and lms[8][1] < lms[7][1] < lms[6][1] and (lms[4][0] > lms[3][0] > lms[2][0]) and lms[8][0] > lms[20][0] and lms[4][1] > lms[5][1]:
        return 'L'
    
    #A but thumb across ring and above pinky
    if all(lms[i][1] > lms[i-2][1] for i in (8, 12, 16, 20)) and lms[14][1] < lms[4][1] < lms[18][1] and lms[4][0] < lms[15][0] and lms[17][0] < lms[0][0]:
        return 'M'
    
    #M but across middle
    if all(lms[i][1] > lms[i-2][1] for i in (8, 12, 16, 20)) and lms[14][1] > lms[4][1] < lms[19][1] and lms[4][0] < lms[10][0] and lms[17][0] < lms[0][0] and lms[3][1] > lms[6][1]:
        return 'N'
    
    #Check fingers are curled, thumb tip below index tip, wrist rotated, and fingers touching
    if all(lms[4][1] > lms[i][1] > lms[i-2][1] for i in (8, 12, 16, 20)) and lms[20][0] > lms[5][0] and (lms[3][1] - lms[4][1]) * 2.5 > lms[4][1] - lms[12][1] and lms[1][0] > lms[0][0]:
        return 'O'

    #Check pinky ring curled, middle index thumb straight down, and fingers below wrist
    if all(lms[i][1] < lms[i-2][1] for i in (16, 20)) and all(lms[i][1] > lms[i-1][1] > lms[0][1] for i in (4, 8, 12)):
        return 'P'
    
    #P but middle curled
    if all(lms[i][1] < lms[i-2][1] for i in (12, 16, 20)) and all(lms[i][1] > lms[i-1][1] > lms[0][1] for i in (4, 8)):
        return 'Q'
    
    #U but fingers crossed
    if all(lms[i][1] > lms[i-2][1] for i in (16, 20)) and all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (8, 12)) and (lms[4][0] < lms[2][0] or lms[4][0] < lms[3][0]) and lms[8][0] > lms[20][0] and lms[8][0] < lms[12][0]:
        return 'R'
    
    #E but thumb above tips and thumb across middle
    if all(lms[4][1] < lms[i-1][1] > lms[i-2][1] for i in (8, 12, 16, 20)) and lms[6][0] > lms[4][0] > lms[14][0] and lms[4][1] > lms[14][1]:
        return 'S'
    
    #S but thumb not across middle
    if all(lms[4][1] < lms[i-1][1] > lms[i-2][1] for i in (8, 12, 16, 20)) and lms[10][0] < lms[4][0] < lms[3][0] and lms[4][1] < lms[14][1]:
        return 'T'

    #D but middle straight and fingers touching
    if all(lms[i][1] > lms[i-2][1] for i in (16, 20)) and all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (8, 12)) and (lms[4][0] < lms[2][0] or lms[4][0] < lms[3][0]) and lms[8][0] > lms[20][0] and (lms[8][0] - lms[12][0] < lms[5][0] - lms[9][0]) and lms[8][0] > lms[12][0]:
        return 'U'
    
    #U but fingers seperated
    if all(lms[i][1] > lms[i-2][1] for i in (16, 20)) and all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (8, 12)) and (lms[4][0] < lms[2][0] or lms[4][0] < lms[3][0]) and lms[8][0] > lms[20][0] and (lms[8][0] - lms[12][0] > lms[5][0] - lms[9][0]):
        return 'V'
    
    #V but 3 fingers up
    if lms[20][1] > lms[18][1] and all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (8, 12, 16)) and (lms[4][0] < lms[2][0] or lms[4][0] < lms[3][0]) and lms[8][0] > lms[20][0]:
        return 'W'
    
    #D but finger curled slightly
    if all(lms[i][1] > lms[i-2][1] for i in (12, 16, 20)) and lms[8][1] > lms[7][1] < lms[5][1] and (lms[4][0] < lms[2][0] or lms[4][0] < lms[3][0]) and lms[8][0] > lms[20][0] and (lms[11][1] - lms[4][1] < lms[4][1] - lms[5][1]):
        return 'X'
    
    #I but thumb straight out
    if all(lms[i][1] > lms[i-2][1] for i in (8, 12, 16)) and lms[20][1] < lms[19][1] < lms[18][1] and (lms[4][0] > lms[2][0] or lms[4][0] > lms[3][0]) and lms[8][0] > lms[20][0]:
        return 'Y'
    
    #D but tilted
    if all(lms[i][1] > lms[i-2][1] for i in (12, 16, 20)) and lms[8][1] < lms[7][1] < lms[6][1] and (lms[4][0] < lms[2][0] or lms[4][0] < lms[3][0]) and lms[8][0] < lms[12][0] and lms[5][0] > lms[17][0]:
        return 'Z'
    
    #B but flipped
    if all(lms[i][1] < lms[i-1][1] < lms[i-2][1] < lms[4][0] for i in (8, 12, 16, 20)) and lms[4][0] > lms[5][0] and lms[17][0] < lms[5][0] :
        return ' '
    
    #X but thumb touching index
    if all(lms[i][1] > lms[i-2][1] for i in (12, 16, 20)) and lms[8][1] > lms[7][1] < lms[5][1] and (lms[4][0] < lms[2][0] or lms[4][0] < lms[3][0]) and lms[8][0] > lms[20][0] and (lms[11][1] - lms[4][1] > lms[4][1] - lms[5][1]) and lms[5][0] > lms[17][0]:
        return '.'
    
    #D but facing away
    if all(lms[i][1] > lms[i-2][1] for i in (12, 16, 20)) and lms[8][1] < lms[7][1] < lms[6][1] and lms[4][0] > lms[2][0] and lms[5][0] < lms[17][0]:
        return '1'
    
    #1 but middle up
    if all(lms[i][1] > lms[i-2][1] for i in (16, 20)) and all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (8, 12)) and lms[4][0] > lms[2][0] and lms[5][0] < lms[17][0]:
        return '2'
    
    #2 but thumb out
    if all(lms[i][1] > lms[i-2][1] for i in (16, 20)) and all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (8, 12)) and lms[4][0] < lms[2][0] and lms[5][0] < lms[17][0]:
        return '3'
    
    #2 but all up
    if all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (8, 12, 16, 20)) and lms[4][0] > lms[2][0] and lms[5][0] < lms[17][0]:
        return '4'
    
    #4 but thumb out
    if all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (8, 12, 16, 20)) and lms[4][0] < lms[2][0] and lms[5][0] < lms[17][0]:
        return '5'
    
    #4 but pinky down
    if all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (8, 12, 16)) and lms[20][1] > lms[18][1] and lms[4][0] > lms[2][0] and lms[5][0] < lms[17][0]:
        return '6'
    
    #4 but ring down
    if all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (8, 12, 20)) and lms[16][1] > lms[14][1] and lms[4][0] > lms[2][0] and lms[5][0] < lms[17][0]:
        return '7'
    
    #4 but middle down
    if all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (8, 16, 20)) and lms[12][1] > lms[10][1] and lms[4][0] > lms[2][0] and lms[5][0] < lms[17][0]:
        return '8'
    
    #F but facing away
    if all(lms[i][1] < lms[i-1][1] < lms[i-2][1] for i in (12, 16, 20)) and lms[4][1] > lms[8][1] > lms[7][1] and (lms[3][1] - lms[4][1]) * 2.5 > (lms[4][1] - lms[8][1]):
        return '9'
    
    #Thumb tip higher than everything else and fingers curled horizontally
    if all(lms[4][1] < lms[i][1] for i in range(5, 21)) and all(lms[i][0] < lms[i+3][0] < lms[i+1][1] for i in (5, 9, 13, 17)):
        return '10'
    
    #Back facing fist with thumb out
    if lms[4][0] < lms[3][0] < lms[2][0] < lms[5][0] < lms[17][0] and all(lms[i][1] < lms[i+2][1] for i in (5, 9, 13, 17)):
        return '0'



