ESC = '\u001b'

RESET = ESC + '[0m'
RESET_DEVISE = ESC + 'c'

ERASE_SCREEN = ESC + '[0J'

BRIGHT     = ESC + '[1m'
DIM        = ESC + '[2m'
ITALIC     = ESC + '[3m'
UNDERSCORE = ESC + '[4m'
BLINK      = ESC + '[5m'
REVERSE    = ESC + '[7m'
HIDDEN     = ESC + '[8m'

TXT_BLACK           = ESC + '[30m'
TXT_RED             = ESC + '[31m'
TXT_GREEN           = ESC + '[32m'
TXT_YELLOW          = ESC + '[33m' 
TXT_BLUE            = ESC + '[34m'
TXT_MAGENTA         = ESC + '[35m'
TXT_CYAN            = ESC + '[36m'
TXT_LIGHT_GRAY      = ESC + '[37m'
TXT_DARK_GRAY       = ESC + '[90m'
TXT_BRIGHT_RED      = ESC + '[91m'
TXT_BRIGHT_GREEN    = ESC + '[92m'
TXT_BRIGHT_YELLOW   = ESC + '[93m'
TXT_BRIGHT_BLUE     = ESC + '[94m'
TXT_BRIGHT_MAGENTA  = ESC + '[95m'
TXT_BRIGHT_CYAN     = ESC + '[96m'
TXT_WHITE           = ESC + '[97m'

BG_BLACK           = '\u001b[40m'
BG_RED             = '\u001b[41m'
BG_GREEN           = '\u001b[42m'
BG_YELLOW          = '\u001b[43m'
BG_BLUE            = '\u001b[44m'
BG_MAGENTA         = '\u001b[45m'
BG_CYAN            = '\u001b[46m'
BG_LIGHT_GRAY      = '\u001b[47m'
BG_DARK_GRAY       = '\u001b[100m'
BG_BRIGHT_RED      = '\u001b[101m'
BG_BRIGHT_GREEN    = '\u001b[102m'
BG_BRIGHT_YELLOW   = '\u001b[103m'
BG_RIGHT_BLUE      = '\u001b[104m'
BG_BRIGHT_MAGENTA  = '\u001b[105m'
BG_BRIGHT_CYAN     = '\u001b[106m'
BG_WHITE           = '\u001b[107m'



def main():
    
    bgs = {'BG_BLACK'          : BG_BLACK,
           'BG_RED'            : BG_RED,
           'BG_GREEN'          : BG_GREEN,
           'BG_YELLOW'         : BG_YELLOW,
           'BG_BLUE'           : BG_BLUE,
           'BG_MAGENTA'        : BG_MAGENTA,
           'BG_CYAN'           : BG_CYAN,        
           'BG_LIGHT_GRAY'     : BG_LIGHT_GRAY,
           'BG_DARK_GRAY'      : BG_DARK_GRAY,
           'BG_BRIGHT_RED'     : BG_BRIGHT_RED,
           'BG_BRIGHT_GREEN'   : BG_BRIGHT_GREEN,
           'BG_BRIGHT_YELLOW'  : BG_BRIGHT_YELLOW,
           'BG_RIGHT_BLUE'     : BG_RIGHT_BLUE,
           'BG_BRIGHT_MAGENTA' : BG_BRIGHT_MAGENTA,
           'BG_BRIGHT_CYAN'    : BG_BRIGHT_CYAN,
           'BG_WHITE'          : BG_WHITE   
         }
    
    txts = {'TXT_BLACK          ' : TXT_BLACK         ,
            'TXT_RED            ' : TXT_RED           ,
            'TXT_GREEN          ' : TXT_GREEN         ,
            'TXT_YELLOW         ' : TXT_YELLOW        ,
            'TXT_BLUE           ' : TXT_BLUE          ,
            'TXT_MAGENTA        ' : TXT_MAGENTA       ,
            'TXT_CYAN           ' : TXT_CYAN          ,
            'TXT_LIGHT_GRAY     ' : TXT_LIGHT_GRAY    ,
            'TXT_DARK_GRAY      ' : TXT_DARK_GRAY     ,
            'TXT_BRIGHT_RED     ' : TXT_BRIGHT_RED    ,
            'TXT_BRIGHT_GREEN   ' : TXT_BRIGHT_GREEN  ,
            'TXT_BRIGHT_YELLOW  ' : TXT_BRIGHT_YELLOW ,
            'TXT_BRIGHT_BLUE    ' : TXT_BRIGHT_BLUE   ,
            'TXT_BRIGHT_MAGENTA ' : TXT_BRIGHT_MAGENTA,
            'TXT_BRIGHT_CYAN    ' : TXT_BRIGHT_CYAN   ,
            'TXT_WHITE          ' : TXT_WHITE         
           }
    
   
    #print(RESET_DEVISE)
    #print(ERASE_SCREEN)
     
    print(RESET)
    print('_____________________________')
    for bg_name ,bg_color in bgs.items():
        print( BG_BLUE +'\n\n',bg_name)
        print('--------------------------------------------------------------')
        for txt_name, txt_color in txts.items():
            print(ITALIC + txt_color,txt_name,end='')
        
    print('_____________________________')
    print(RESET)
    # print(f'{TXT_BLACK}TXT_BLACK')       
    # print(f'{TXT_RED}TXT_RED')            
    # print(f'{TXT_GREEN}TXT_GREEN')       
    # print(f'{TXT_YELLOW}TXT_YELLOW')        
    # print(f'{TXT_BLUE}TXT_BLUE')          
    # print(f'{TXT_MAGENTA}G_MAGENTA')       
    # print(f'{TXT_CYAN}TXT_CYAN')          
    # print(f'{TXT_LIGHT_GRAY}TXT_LIGHT_GRAY')   
    # print(f'{TXT_DARK_GRAY}TXT_DARK_GRAY')     
    # print(f'{TXT_BRIGHT_RED}TXT_BRIGHT_RED')    
    # print(f'{TXT_BRIGHT_GREEN}TXT_BRIGHT_GREEN')  
    # print(f'{TXT_BRIGHT_YELLOW}TXT_BRIGHT_YELLOW') 
    # print(f'{TXT_BRIGHT_BLUE}TXT_BRIGHT_BLUE')   
    # print(f'{TXT_BRIGHT_MAGENTA}TXT_BRIGHT_MAGENTA')
    # print(f'{TXT_BRIGHT_CYAN}TXT_BRIGHT_CYAN')   
    # print(f'{TXT_WHITE}TXT_WHITE')

#     print(f'{BG_BLACK}TXT_BLACK')       
#     print(f'{BG_RED}TXT_RED')            
#     print(f'{BG_GREEN}TXT_GREEN')       
#     print(f'{BG_YELLOW}TXT_YELLOW')        
#     print(f'{BG_BLUE}TXT_BLUE')          
#     print(f'{BG_MAGENTA}G_MAGENTA')       
#     print(f'{BG_CYAN}TXT_CYAN')          
#     print(f'{BG_LIGHT_GRAY}TXT_LIGHT_GRAY')   
#     print(f'{BG_DARK_GRAY}TXT_DARK_GRAY')     
#     print(f'{BG_BRIGHT_RED}TXT_BRIGHT_RED')
#     print(f'{BG_BRIGHT_GREEN}TXT_BRIGHT_GREEN')  
#     print(f'{BG_BRIGHT_YELLOW}TXT_BRIGHT_YELLOW') 
#     print(f'{BG_RIGHT_BLUE}TXT_BRIGHT_BLUE')   
#     print(f'{BG_BRIGHT_MAGENTA}TXT_BRIGHT_MAGENTA')
#     print(f'{BG_BRIGHT_CYAN}TXT_BRIGHT_CYAN')   
#     print(f'{BG_WHITE}TXT_WHITE')
if __name__ == '__main__':
    main()

