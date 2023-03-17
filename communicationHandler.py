import logging
import telepot
import colorlog
import os, psutil
#process = psutil.Process(os.getpid())
#print(psutil.Process(os.getpid()).memory_info().rss)


#<----------------------------BASIC-BOT-SETUP---------------------------->
user_id= 1903052290
admin_com_bot_token = '5383795528:AAGNZYif6FcA1XAhbeTh_IfdH-4FvbG4IVw'
admin_com = telepot.Bot(admin_com_bot_token)

logger = logging.getLogger('lokk')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("mainLOG.log")

formatter = logging.Formatter('%(asctime)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.propagate = False

#<----------------------------------------------------COMMUNICATION-FUNCTION---------------------------------------------------->
def com(msg,typ='INFO', log=True, logfile='mainLOG.log',contact_admin=False,contact_client_with_id=0):
    #logging.basicConfig(filename=logfile, level=logging.INFO, filemode='a',format='%(asctime)s - %(levelname)s - %(message)s')



    if log==True:
        match typ:
            case 'INFO':
                logger.info(str(msg)+' || RAM('+str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)+'MB)')
            case 'ERROR':
                logging.error(msg)
                contact_admin = True

    #<-------------------TELEPOT-HANDLING------------------->
    if contact_client_with_id !=0:
        admin_com.sendMessage(contact_client_with_id, msg)

    if contact_admin == True:
        admin_com.sendMessage(user_id,msg)



com('egg')
#com('Backend Failed',typ='ERROR',contact_client_with_id=1903052290)