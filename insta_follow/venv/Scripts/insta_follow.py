from selenium import webdriver
import time


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome("C:/chromedriver.exe")
        self.username = username
        self.password = password

    # def pobierz_haslo(self):
    #     plik = open('hasla.txt')
    #     x = plik.read()
    #     x_str = str(x)
    #     return x_str

    def scroll(self):
        fBody = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        i += 1
        while scroll < 5:  # scroll 5 times
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                       fBody)
            time.sleep(1)
            scroll += 1


    def login(self):
        plik = open('hasla.txt')
        x = plik.read()
        x_str = str(x)

        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        self.driver.find_element_by_name('username').send_keys("ma7inowy")
        self.driver.find_element_by_name('password').send_keys(x_str)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        time.sleep(2)
        ###likes

        self.driver.get("https://www.instagram.com/czekoladalodz/?hl=pl")
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[@href="/czekoladalodz/followers/"]').click()
        time.sleep(4)
        i = 0
        j = 0
        # find all li elements in list
        self.scroll()
        time.sleep(1)
        for count in range(1, 10000):
            try:
                j = j + 1
                print(j)
                if i % 3 == 0:
                    self.scroll()
                    i=i+1
                self.driver.find_element_by_xpath(
                        '/html/body/div[3]/div/div[2]/ul/div/li[' + str(count) + ']/div/div[1]/div[1]/span/img').click()
                time.sleep(1)
                # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/section/div[2]/button[2]/div/span').click()
                self.driver.find_element_by_class_name('Szr5J').click()
            # time.sleep(0.1)
            except Exception:
                print('x')

            try:
                # scroll = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li['+str(count)+']/div/div[1]/div[1]/span/img')
                time.sleep(1)
                if i % 3 == 0:
                    self.scroll()
                    i = i + 1
                self.driver.find_element_by_xpath(
                    '/html/body/div[4]/div/div[2]/ul/div/li[' + str(count) + ']/div/div[1]/div[1]/span/img').click()
                time.sleep(1)
                self.driver.find_element_by_class_name('Szr5J').click()
            # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/section/div[2]/button[2]/div/span').click()
            # time.sleep(1)
            except Exception:
                print('Error in scrolling!')
                continue


zmienna = InstaBot("abc", "abc")
zmienna.login()
