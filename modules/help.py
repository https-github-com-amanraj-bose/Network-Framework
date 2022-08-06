from modules.color import bright


helps = f"""\n\033[1;37m
+-------------------------------------------------------------------------------------------------------------------------------------+
| S.no |    Name    |       Parameters      |                                   Description                                           |
+------|------------|-----------------------|-----------------------------------------------------------------------------------------+
|  0   |    tool    |  [ No Arguments ]     |  Seeing the Tools list                                                                  |  
|-------------------------------------------------------------------------------------------------------------------------------------|
|  1   |    help    |  [ Attribute Name ]   |   If you are not understand any function of this tool then use \033[0;32mhelp {bright.white}then space and write|
|      |            |                       |   the function name. example: \033[0;32mhelp {bright.white}honeypot.                                            |
|-------------------------------------------------------------------------------------------------------------------------------------|
|  2   |    cls     |    [ No Arguments ]   |   this function clearing the console.                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------|  
|  3   |    use     |   [ Function name ]   |   Using Any function like use honeypot                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------|
|  4   |    set     | [ Argument ][ Input ] |   Set the tools argument                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------+
"""

tools = """
+---------------------------------------------------------------------------------------------------------+
| S.no  |   Name    |       Parameters      |                      Description                            |
+---------------------------------------------------------------------------------------------------------+
|   0   |  honeypot | [ IP ]  [ Template ]  |  This Tool is using for capture attacker Information that's |
|       |           |                       |  use your browser. more information                         |
|       |           |                       |  (\033[0;35mhttps://github.com/amanraj-bose \033[1;37m).\t\t\t  |
|---------------------------------------------------------------------------------------------------------|
|   1   | ip_locate |     [ Public IP ]     |   This Tool locate the Victim Location By public Ip address |
|       |           |                       |   More Information                                          | 
|       |           |                       |   (\033[0;35mhttps://github.com/amanraj-bose \033[1;37m).   \t\t\t  |
|---------------------------------------------------------------------------------------------------------|
|   2   | phone_no  |   [ Mobile Number ]   | This Tool extract data from Victim Phone Number             |
|---------------------------------------------------------------------------------------------------------|
|   3   | email_sc  |  [ Email Address ]    | This Tool using For Extracting Data From an Email.          |
|---------------------------------------------------------------------------------------------------------|
|   4   | web_sc_adv|   [ Url ]             | Scanning Url With Advance Features.                         |
|---------------------------------------------------------------------------------------------------------|
|   5   | web_sc    |   [ Url ]             | Scanning Url With Basic Features.                           |
|---------------------------------------------------------------------------------------------------------|
|   6   | url_scr   |   [ Url ]             | Scarping Urls from the Webistes url.                        | 
|---------------------------------------------------------------------------------------------------------|
|   7   | url_cp    |   [ Url ] [ Tag ]     | Capturing Website Tag From Websites.                        |
|---------------------------------------------------------------------------------------------------------|
|   8   | MAC_Locater |   [ MAC ]             | Extracting Information From Given MAC address.            |
|---------------------------------------------------------------------------------------------------------|
| \033[1;37mNote : \033[0;31m setting arguments by \033[0;32mset < Arguments > < Value >\033[1;37m and \033[0;32m show options\033[1;37m For showing Tool Options \t  |
| when you in tool.                                                                                       |            
+---------------------------------------------------------------------------------------------------------+
"""

tools_temux = """
+-----------------------------------------------------------------------------------------------------------------------+
| S.no  |   Name    |       Parameters      |                      Description                            | Permissions |
+-----------------------------------------------------------------------------------------------------------------------+
|   0   |  honeypot | [ IP ]  [ Template ]  |  This Tool is using for capture attacker Information that's |   Denied    |
|       |           |                       |  use your browser. more information                         |             |
|       |           |                       |  (\033[0;35mhttps://github.com/amanraj-bose \033[1;37m).\t\t\t  |         \t|
|-----------------------------------------------------------------------------------------------------------------------|
|   1   | ip_locate |     [ Public IP ]     |   This Tool locate the Victim Location By public Ip address |   Access    |
|       |           |                       |   More Information                                          |             |
|       |           |                       |   (\033[0;35mhttps://github.com/amanraj-bose \033[1;37m).   \t\t\t  |     \t|
|-----------------------------------------------------------------------------------------------------------------------|
|   2   | phone_no  |   [ Mobile Number ]   | This Tool extract data from Victim Phone Number             |   Access    |
|-----------------------------------------------------------------------------------------------------------------------|
|   3   | email_sc  |  [ Email Address ]    | This Tool using For Extracting Data From an Email.          |   Access    |
|-----------------------------------------------------------------------------------------------------------------------|
|   4   | web_sc_adv|   [ Url ]             | Scanning Url With Advance Features.                         |   Access    |
|-----------------------------------------------------------------------------------------------------------------------|
|   5   | web_sc    |   [ Url ]             | Scanning Url With Basic Features.                           |   Access    |
|-----------------------------------------------------------------------------------------------------------------------|
|   6   | url_scr   |   [ Url ]             | Scarping Urls from the Webistes url.                        |   Access    | 
|-----------------------------------------------------------------------------------------------------------------------|
|   7   | url_cp    |   [ Url ] [ Tag ]     | Capturing Website Tag From Websites.                        |   Access    |
|-----------------------------------------------------------------------------------------------------------------------+
| \033[1;37mNote : \033[0;31m setting arguments by \033[0;32mset < Arguments > < Value >\033[1;37m and \033[0;32m show options\033[1;37m For showing Tool Options \t  |
| when you in tool.                                                                                       |            
+---------------------------------------------------------------------------------------------------------+
"""
