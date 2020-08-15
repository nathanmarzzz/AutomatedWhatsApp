from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    count = 3
    print('Scan the QR code from your phone to connect to web application.')

    # get name of group
    name = input("Enter name of user/group")

    #get mssg
    mess = input("Enter your message: ")

    input("enter anything after scanning.")
    try:
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        # click on name of user/group chat
        user.click()
    except Exception as e:
        print(e)

    # got to message box
    # input container is message box text

    messBox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    # driver.find_element_by_class_name("_3u328 copyable-text selectable-text")

    for i in range(count):
        try:
            messBox.send_keys(mess)
            button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
            button.click()
        except Exception as e:
            print(e)

    # create while loop for text with bool value
    '''
    con = True

    while con:
        # message to send to group
        mess = input("enter message to send to group/user")

        # send message to group
        messBox.send_keys(mess)

        # find botton to send
        button = driver.find_element_by_class_name("compose-btn-send")
        button.click()
        print('message sent')

        # to continue
        decide = int(input("Enter -1 to quit and anything else to continue."))

        # set con bool variable to change if user dont messaging
        if decide == -1:
            con = False
'''
    # end
    print("done")


# call main
if __name__ == "__main__":
    main()